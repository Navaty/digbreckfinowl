create table tservicegroup (id serial primary key , name varchar(200), image varchar(500), description text, parent_id bigint
    , created timestamp default now(), creator_id bigint constraint fk_servicegroup_creator references auth_user
    , modified timestamp default now(), modifier_id bigint constraint fk_servicegroup_modifier references auth_user
    , deleted timestamp, deleter_id bigint constraint fk_servicegroup_deleter references auth_user);

alter table tservicegroup add constraint fk_servicegroup_parent foreign key (parent_id) references tservicegroup;

create table tdepartment (id serial primary key , name varchar(200), image varchar(500), description text, parent_id bigint
    , created timestamp default now(), creator_id bigint constraint fk_department_creator references auth_user
    , modified timestamp default now(), modifier_id bigint constraint fk_department_modifier references auth_user
    , deleted timestamp, deleter_id bigint constraint fk_department_deleter references auth_user);

alter table tdepartment add constraint fk_department_parent foreign key (parent_id) references tdepartment;

create table tvendorapi (id serial primary key, name varchar(200), image varchar(500), description text
    , ip_address inet, login varchar(50), password varchar(50), outgoing_code text, incoming_code text
    , created timestamp default now(), creator_id bigint constraint fk_vendorapi_creator references auth_user
    , modified timestamp default now(), modifier_id bigint constraint fk_vendorapi_modifier references auth_user
    , deleted timestamp, deleter_id bigint constraint fk_vendorapi_deleter references auth_user);

create table tobjecttype (id serial primary key , name varchar(200), image varchar(500), description text
    , vendorapi_id bigint constraint fk_vendorapi_vendor references tvendorapi
    , created timestamp default now(), creator_id bigint constraint fk_department_creator references auth_user
    , modified timestamp default now(), modifier_id bigint constraint fk_department_modifier references auth_user
    , deleted timestamp, deleter_id bigint constraint fk_department_deleter references auth_user);

drop table if exists trequeststatus cascade ;

create table trequeststatus (id serial primary key, name varchar(200), image varchar(500), description text
    , objecttype_id bigint constraint fk_requeststatus_objecttype references tobjecttype
    , created timestamp default now(), creator_id bigint constraint fk_requeststatus_creator references auth_user
    , modified timestamp default now(), modifier_id bigint constraint fk_requeststatus_modifier references auth_user
    , deleted timestamp, deleter_id bigint constraint fk_requeststatus_deleter references auth_user);




drop table if exists tvendorapi cascade ;

create table tvendorapi (id serial primary key, name varchar(200), image varchar(500), description text
    , url varchar(500), login varchar(50), password varchar(50), sertificate text, outgoing_code text, parameters_out text, incoming_code text, parameters_in text
    , created timestamp default now(), creator_id bigint constraint fk_vendorapi_creator references auth_user
    , modified timestamp default now(), modifier_id bigint constraint fk_vendorapi_modifier references auth_user
    , deleted timestamp, deleter_id bigint constraint fk_vendorapi_deleter references auth_user);

create table tpaymentapi (id serial primary key, name varchar(200), image varchar(500), description text
    , url varchar(500), login varchar(50), password varchar(50), sertificate text, outgoing_code text, parameters_out text, incoming_code text, parameters_in text
    , created timestamp default now(), creator_id bigint constraint fk_vendorapi_creator references auth_user
    , modified timestamp default now(), modifier_id bigint constraint fk_vendorapi_modifier references auth_user
    , deleted timestamp, deleter_id bigint constraint fk_vendorapi_deleter references auth_user);

create table trequesttemplate (id serial primary key, name varchar(200) not null , image varchar(500), description text
    , objecttype_id bigint constraint fk_requesttemplate_objecttype references tobjecttype not null
    , servicegroup_id bigint constraint fk_requesttemplate_servicegroup references tservicegroup not null
    , initstatus_id bigint constraint fk_requesttemplate_requeststatus references trequeststatus not null
    , department_id bigint constraint fk_requesttemplate_department references tdepartment
    , vendorapi_id bigint constraint fk_requesttemplate_vendorapi references tvendorapi
    , paymentapi_id bigint constraint fk_requesttemplate_paymentapi references tpaymentapi
    , created timestamp default now(), creator_id bigint constraint fk_requeststatus_creator references auth_user
    , modified timestamp default now(), modifier_id bigint constraint fk_requeststatus_modifier references auth_user
    , deleted timestamp, deleter_id bigint constraint fk_requeststatus_deleter references auth_user);

create table trequestfieldtype (id serial primary key , name varchar(200), image varchar(500), description text, regexp_mask varchar(500)
    , is_image int not null default 0 check (is_file in (0,1) ), is_file int not null default 0 check (is_file in (0,1) )
    , created timestamp default now(), creator_id bigint constraint fk_fieldtype_creator references auth_user
    , modified timestamp default now(), modifier_id bigint constraint fk_fieldtype_modifier references auth_user
    , deleted timestamp, deleter_id bigint constraint fk_fieldtype_deleter references auth_user);

insert into trequestfieldtype (name, regexp_mask, is_image) values ('ФИО', '[А-Я][а-я]+',0), ('Email', '[a-zA-Z_.-]]+@[a-z_.-]+',0), ('Паспорт','[0-9]{4} [0-9]{6}',0), ('Скан документа',null,1);

create table trequesttemplatefield (id serial primary key
    , requesttemplate_id bigint constraint fk_templatefield_template references trequesttemplate not null
    , requestfieldtype_id bigint constraint fk_templatefield_fieldtype references trequestfieldtype not null
    , field_index int not null default 1, name varchar(200) not null, image varchar(500), description text
    , required int not null default 0 check (required in (0,1) )
    , created timestamp default now(), creator_id bigint constraint fk_requesttemplatefield_creator references auth_user
    , modified timestamp default now(), modifier_id bigint constraint fk_requesttemplatefield_modifier references auth_user
    , deleted timestamp, deleter_id bigint constraint fk_requesttemplatefield_deleter references auth_user
    , unique (requesttemplate_id, field_index));

drop table if exists tdepartmentrule;

create table tdepartmentrule (id serial primary key
    , requeststatus_id bigint constraint fk_rule_status references trequeststatus
    , requesttemplate_id bigint constraint fk_rule_requesttemplate references trequesttemplate
    , objecttype_id bigint constraint fk_rule_objecttype references tobjecttype
    , valid_from timestamp default now(), valid_to timestamp default '4000-01-01'
    , name varchar(200), image varchar(500), description text
    , created timestamp default now(), creator_id bigint constraint fk_departmentrule_creator references auth_user
    , modified timestamp default now(), modifier_id bigint constraint fk_departmentrule_modifier references auth_user
    , deleted timestamp, deleter_id bigint constraint fk_departmentrule_deleter references auth_user);
