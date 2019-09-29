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

create table trequestfieldtype (id serial primary key, name varchar(200), image varchar(500), description text, regexp_mask varchar(500)
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
    , department_id bigint constraint fk_rule_department references tdepartment
    , requeststatus_id bigint constraint fk_rule_status references trequeststatus
    , requesttemplate_id bigint constraint fk_rule_requesttemplate references trequesttemplate
    , objecttype_id bigint constraint fk_rule_objecttype references tobjecttype
    , valid_from timestamp default now(), valid_to timestamp default '4000-01-01'
    , name varchar(200), image varchar(500), description text
    , created timestamp default now(), creator_id bigint constraint fk_departmentrule_creator references auth_user
    , modified timestamp default now(), modifier_id bigint constraint fk_departmentrule_modifier references auth_user
    , deleted timestamp, deleter_id bigint constraint fk_departmentrule_deleter references auth_user);




create or replace function random_string_hex(integer) returns text security definer language sql as $$
SELECT  to_hex((extract(epoch from now()))::int)||array_to_string( ARRAY ( SELECT substring('0123456789abcdef' FROM least(greatest((random()*16)::int,1),16) FOR 1) FROM generate_series(1,$1) ), '' )
$$;

create table tclient (id serial primary key, clientid varchar(50) default random_string_hex(2), djangouser_id bigint constraint fk_client_user references auth_user
    , image varchar(500), last_name varchar(100), first_name varchar(100), father_name varchar(100), phone varchar(15) unique not null, email varchar(100) unique not null
    , inn bigint check ( inn between 1e12 and 1e13-1 ), snils varchar(15)
    , created timestamp default now(), creator_id bigint constraint fk_client_creator references auth_user
    , modified timestamp default now(), modifier_id bigint constraint fk_client_modifier references auth_user
    , deleted timestamp, deleter_id bigint constraint fk_client_deleter references auth_user);

create table trequest (id serial primary key, request_date date default current_date, request_number varchar(50) unique default random_string_hex(2)
    , client_id bigint constraint fk_request_client references tclient
    , requesttemplate_id bigint constraint fk_request_template references trequesttemplate
    , requeststatus_id bigint constraint fk_request_status references trequeststatus
    , current_user_id bigint constraint fk_request_user references auth_user, status_date timestamp default now(), finish_date timestamp
    , client_comments text, client_image varchar(500), client_file varchar(500), user_comments text, user_image varchar(500), user_file varchar(500), parameters text
    , created timestamp default now(), creator_id bigint constraint fk_client_creator references auth_user
    , modified timestamp default now(), modifier_id bigint constraint fk_client_modifier references auth_user
    , deleted timestamp, deleter_id bigint constraint fk_client_deleter references auth_user );

create table trequestfield (id serial primary key, request_id bigint constraint fk_request_field references trequest
    , templatefield_id bigint constraint fk_requestfield_field references trequesttemplatefield
    , field_value varchar(1000), image varchar(500), filename varchar(500)
    , created timestamp default now(), creator_id bigint constraint fk_client_creator references auth_user
    , modified timestamp default now(), modifier_id bigint constraint fk_client_modifier references auth_user
    , deleted timestamp, deleter_id bigint constraint fk_client_deleter references auth_user
                           , unique (request_id, templatefield_id));

alter table trequestfield add constraint uk_requestfield unique (request_id, templatefield_id);

drop table if exists trequesttemplaterule cascade ;

create table trequesttemplaterule (id serial primary key, name varchar(200) not null, image varchar(500), description text
    , requesttemplate_id bigint constraint fk_requestrule_request references trequesttemplate not null
    , prev_status_id bigint constraint fk_requestrule_prevstatus references trequeststatus not null
    , next_status_id bigint constraint fk_requestrule_nextstatus references trequeststatus not null
    , requiredfield_id bigint constraint fk_requestrule_field references trequesttemplatefield
    , vendorapi_id bigint constraint fk_requestrule_vendorapi references tvendorapi, parameters text
    , paymentapi_id bigint constraint fk_requestrule_paymentapi references tpaymentapi
    , max_days decimal(6,3) default 1 not null, unique (requesttemplate_id, prev_status_id, next_status_id)
    , created timestamp default now(), creator_id bigint constraint fk_client_creator references auth_user
    , modified timestamp default now(), modifier_id bigint constraint fk_client_modifier references auth_user
    , deleted timestamp, deleter_id bigint constraint fk_client_deleter references auth_user);

drop table if exists trequeststatushistory cascade ;

create table trequeststatushistory (id serial primary key
    , request_id bigint constraint fk_requesthistory_request references trequest
    , rule_id bigint constraint fk_requesthistory_rule references trequesttemplaterule not null
    , prev_status_id bigint constraint fk_requesthistory_prevstatus references trequeststatus not null
    , next_status_id bigint constraint fk_requesthistory_nextstatus references trequeststatus not null
    , comments text, image varchar(500), filename varchar(500), param_values text
    , status_date timestamp default now(), creator_id bigint constraint fk_requesthistory_creator references auth_user);


drop table if exists temployee;

create table temployee (id serial primary key, user_id bigint constraint fk_employee_user references auth_user
    , department_id bigint constraint fk_employee_department references tdepartment
    , date_in timestamp default now(), date_out timestamp default '4000-01-01', priority int, comments text
    , created timestamp default now(), creator_id bigint constraint fk_client_creator references auth_user
    , modified timestamp default now(), modifier_id bigint constraint fk_client_modifier references auth_user
    , deleted timestamp, deleter_id bigint constraint fk_client_deleter references auth_user);


create or replace function func_client(puserid bigint, pdata json, pprivileged int) returns json language sql security definer as $$
    select row_to_json(r) from tclient r where clientid=pdata->>'id' or djangouser_id =puserid
$$;


create or replace function func_requests(puserid bigint, pdata json, pprivileged int) returns json language sql security definer as $$
    select json_agg(row_to_json(r)) from (select t.name, request_number id, s.name status, to_char(r.request_date,'dd.mm.yyyy') publish_date, d.eliminate_days, to_char(r.finish_date,'dd.mm.yyyy') complete_date
        from tclient l, trequest r, trequeststatus s, trequesttemplate t, (select requesttemplate_id, sum(max_days) eliminate_days from trequesttemplaterule group by requesttemplate_id) d
        where coalesce(r.requeststatus_id,t.initstatus_id) =s.id and r.requesttemplate_id=t.id and r.requesttemplate_id=d.requesttemplate_id and l.id=r.client_id and (l.clientid=pdata->>'id' or djangouser_id =puserid)) r
$$;

select random_string_hex(1), random_string_hex(1);

create or replace function func_request(puserid bigint, pdata json, pprivileged int) returns json language sql security definer as $$
    with req as (select r.client_id, f.field_value, t.name, coalesce(nullif(trim(t.description),''), t.name) as label from trequest r, trequestfield f, trequestfieldtype t where f.request_id=r.id and f.templatefield_id=t.id and r.request_number=pdata->>'id'
        ), cli as (select l.* from tclient l where exists (select 1 from req where l.id=req.client_id))
    select json_object_agg(key, value) from
        ( select json_build_object('type','text','label','Имя','key', random_string_hex(1),'value',l.first_name) as value, 'first_name' as key from cli l
        union all select json_build_object('type','text','label','Фамилия','key', random_string_hex(1),'value',l.last_name)  as value, 'last_name' as key from cli l
        union all select json_build_object('type','text','label','Отчество','key', random_string_hex(1),'value',l.father_name)  as value, 'father_name' as key from cli l
        union all select json_build_object('type','text','label','Телефон','key', random_string_hex(1),'value',l.phone) as value, 'phone' as key from cli l
        union all select json_build_object('type','text','label','Email','key', random_string_hex(1),'value',l.email) as value, 'email' as key from cli l
        union all select json_build_object('type','text','label','Регион','key',random_string_hex(1)) as value, 'region' as key from cli l
        union all select json_build_object('type','text','label','Район','key',random_string_hex(1))  as value, 'rajon' as key from cli l
        union all select json_build_object('type','text','label','Улица','key',random_string_hex(1)) as value, 'street' as key from cli
        union all select json_build_object('type','text','label','Дом','key', random_string_hex(1))  as value, 'house' as key from cli l
        union all select json_build_object('type','text','label','Квартира','key', random_string_hex(1)) as value, 'apartment' as key from cli l
        union all select json_build_object('type','text','label','Корпус','key', random_string_hex(1))  as value, 'korpus' as key from cli l
        union all select json_build_object('type', 'text', 'label', label, 'key', random_string_hex(1), 'value', field_value) as value, name as key from req
        ) r
$$;

create or replace function func_template(puserid bigint, pdata json, pprivileged int) returns json language sql security definer as $$
    with req as (select f.name, coalesce(nullif(trim(f.description),''), f.name) as label from trequesttemplate r, trequesttemplatefield f, trequestfieldtype t
        where f.requesttemplate_id=r.id and f.requestfieldtype_id=t.id and r.servicegroup_id=(pdata->>'id')::bigint
        ), cli as (select l.* from tclient l where djangouser_id=puserid)
    select json_object_agg(key, value) from
        ( select json_build_object('type','text','label','Имя','key', random_string_hex(1),'value',l.first_name) as value, 'first_name' as key from cli l
        union all select json_build_object('type','text','label','Фамилия','key', random_string_hex(1),'value',l.last_name)  as value, 'last_name' as key from cli l
        union all select json_build_object('type','text','label','Отчество','key', random_string_hex(1),'value',l.father_name)  as value, 'father_name' as key from cli l
        union all select json_build_object('type','text','label','Телефон','key', random_string_hex(1),'value',l.phone) as value, 'phone' as key from cli l
        union all select json_build_object('type','text','label','Email','key', random_string_hex(1),'value',l.email) as value, 'email' as key from cli l
        union all select json_build_object('type','text','label','Регион','key',random_string_hex(1)) as value, 'region' as key from cli l
        union all select json_build_object('type','text','label','Район','key',random_string_hex(1))  as value, 'rajon' as key from cli l
        union all select json_build_object('type','text','label','Улица','key',random_string_hex(1)) as value, 'street' as key from cli
        union all select json_build_object('type','text','label','Дом','key', random_string_hex(1))  as value, 'house' as key from cli l
        union all select json_build_object('type','text','label','Квартира','key', random_string_hex(1)) as value, 'apartment' as key from cli l
        union all select json_build_object('type','text','label','Корпус','key', random_string_hex(1))  as value, 'korpus' as key from cli l
        union all select json_build_object('type', 'text', 'label', label, 'key', random_string_hex(1)) as value, name as key from req
--             union all select to_json(puserid), 'us'
        ) r
$$;


select ((('{"a": {"b":1}}'::json)->>'a')::json)->>'b';

create or replace function func_templates(puserid bigint, pdata json, pprivileged int) returns json language sql security definer as $$
    select json_agg(row_to_json(r)) from (select t.id, t.servicegroup_id group_id, g.name as group, t.name, '/uploads/'||t.image icon, t.description from trequesttemplate t, tservicegroup g
     where t.servicegroup_id=g.id and t.deleted is null and g.id=coalesce((pdata->>'id')::bigint, g.id)) r
$$;

create or replace function func_groups(puserid bigint, pdata json, pprivileged int) returns json language sql security definer as $$
    select json_agg(row_to_json(r)) from (select g.id, g.name, '/uploads/'||g.image icon, g.description from tservicegroup g where g.deleted is null) r
$$;

create table jj (j json);

create or replace function func_setrequest(puserid bigint, pdata json, pprvileged int) returns json language plpgsql security definer as $$
declare vRequestID bigint; vRequestNumb text;
begin
    insert into trequest(request_number, client_id, requesttemplate_id, requeststatus_id, client_comments, client_image, client_file, creator_id, created,  modifier_id, modified)
       select coalesce(pdata->>'id', random_string_hex(2)), l.id, t.id, t.initstatus_id, pdata->>'comments', json_extract_path_text(pdata,'files','image'), json_extract_path_text(pdata,'files','document'), puserid, now(), puserid, now()
           from tclient l, trequesttemplate t where t.servicegroup_id=(pdata->>'type')::bigint and l.djangouser_id=puserid on conflict (request_number) do update set
       client_comments=excluded.client_comments, client_image=excluded.client_image, client_file=excluded.client_file, modified=now()
    returning request_number, id into vRequestNumb, vRequestID;
    insert into trequestfield (request_id, templatefield_id, field_value, filename, created, creator_id, modified, modifier_id) SELECT
        vRequestID, f.id, j.value, ((pdata->>'files')::json)->>j.value::text, now(), puserid, now(), puserid from json_each(pdata) j, trequesttemplatefield f, trequesttemplate t
        where j.key=f.name and f.requesttemplate_id=t.id and t.servicegroup_id=(pdata->>'type')::bigint and j.key not in ('files', 'type', 'first_name', 'last_name', 'father_name', 'phone', 'email', 'region', 'rajon', 'street', 'house', 'apartment', 'korpus')
    on conflict (request_id, templatefield_id) do update set field_value=excluded.field_value, modified=now();
    return json_build_object('id', vRequestNumb);
end
$$;

delete from trequestfield where templatefield_id in (select id from trequesttemplatefield where requesttemplate_id=1);

delete from trequeststatushistory where rule_id in (select id from trequesttemplaterule where requesttemplate_id=1);

delete from trequesttemplaterule where requesttemplate_id=1;

delete from trequesttemplaterule where requesttemplate_id=1;

delete from trequesttemplatefield where requesttemplate_id=1;

delete from trequesttemplate where id=1 cascade;