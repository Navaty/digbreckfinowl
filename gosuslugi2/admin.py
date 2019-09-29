from django.contrib import admin
from datetime import datetime
from django.utils.safestring import mark_safe
from django.utils import timezone
from gosuslugi2.models import *


class DictionaryAdmin(admin.ModelAdmin):
    def img(self, obj):
        return mark_safe("""<img width="100px" src="%s">""" % ((str(obj.image) if str(obj.image).startswith('http') else obj.image.url) if obj.image else ''))

    list_display = ['name', 'description', 'img', 'modified', 'modifier']
    readonly_fields = ['img']
    fields = ['name', 'description', 'img', 'image']
    save_as = True
    # actions = ['delete_selected']

    def get_queryset(self, request):
        qs = super(DictionaryAdmin, self).get_queryset(request)
        return qs.filter(deleted__isnull=True)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "servicegroup":
            kwargs["queryset"] = ServiceGroup.objects.filter(deleted__isnull=True)
        if db_field.name == "objecttype":
            kwargs["queryset"] = ObjectType.objects.filter(deleted__isnull=True)
        if db_field.name == "initstatus":
            kwargs["queryset"] = RequestStatus.objects.filter(deleted__isnull=True)
        if db_field.name == "department":
            kwargs["queryset"] = Department.objects.filter(deleted__isnull=True)
        if db_field.name == "vendorapi":
            kwargs["queryset"] = VendorApi.objects.filter(deleted__isnull=True)
        if db_field.name == "paymentapi":
            kwargs["queryset"] = PaymentApi.objects.filter(deleted__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def delete_model(self, request, obj):
        # dbfunction('ratingdelete', {'ratingids': [obj.id]}, request)
        obj.deleted = timezone.make_aware(datetime.now(), timezone.get_default_timezone()).astimezone(timezone.get_default_timezone())
        obj.deleter = request.user
        obj.save()

    def delete_selected(self, request, obj):
        # dbfunction('ratingdelete', {'ratingids': [o.id for o in obj.all()]}, request)
        for o in obj.all():
            o.deleted = timezone.make_naive(timezone.make_aware(datetime.now(), timezone.get_default_timezone()), timezone.get_default_timezone())
            o.deleter = request.user
            o.save()

    def save_model(self, request, obj, form, change):
        obj.modifier=request.user
        obj.modified=timezone.make_naive(timezone.make_aware(datetime.now(), timezone.get_default_timezone()), timezone.get_default_timezone())
        if not obj.creator:
            obj.creator = request.user
            obj.created = obj.modified
        obj.save()

    def has_delete_permission(self, request, obj=None):
        if getattr(request, '_editing_document', False):  # query attribute
            return False
        return super(DictionaryAdmin, self).has_delete_permission(request, obj=obj)

    def has_change_permission(self, request, obj=None):
        if getattr(request, '_editing_document', False):  # query attribute
            return False
        return super(DictionaryAdmin, self).has_delete_permission(request, obj=obj)


class VendorApiAdmin(DictionaryAdmin):
    list_display = ['name', 'url', 'login', 'outgoing_code', 'incoming_code', 'description', 'modified', 'modifier']
    fields = ['name', 'url', 'login', 'password', 'outgoing_code', 'incoming_code', 'description']


class RequestFieldTypeAdmin(DictionaryAdmin):
    fields = ['name', 'image', 'regexp_mask', 'is_image', 'is_file', 'description']
    list_display = ['name', 'img', 'regexp_mask', 'is_image', 'is_file', 'description']


class RequestTemplateFieldInline(admin.TabularInline):
    fields = ['name', 'requestfieldtype', 'field_index', 'image', 'required', 'description']
    extra = 1
    model = RequestTemplateField

    def get_queryset(self, request):
        qs = super(RequestTemplateFieldInline, self).get_queryset(request)
        return qs.filter(deleted__isnull = True)


class RequestTemplateRuleInline(admin.TabularInline):
    fields = ['name', 'prev_status', 'next_status', 'max_days', 'requiredfield', 'img', 'image', 'description', 'vendorapi', 'parameters', 'paymentapi']
    readonly_fields = ['img']

    def img(self, obj):
        return mark_safe("""<img width="100px" src="%s">""" % ((str(obj.image) if str(obj.image).startswith('http') else obj.image.url) if obj.image else ''))

    extra = 1
    model = RequestTemplateRule

    def get_queryset(self, request):
        qs = super(RequestTemplateRuleInline, self).get_queryset(request)
        return qs.filter(deleted__isnull = True)


class RequestTemplateAdmin(DictionaryAdmin):
    fields = ['name', 'image', 'objecttype', 'servicegroup', 'description', 'initstatus', 'department', 'vendorapi', 'paymentapi']
    list_display = ['name', 'img', 'objecttype', 'servicegroup', 'description', 'initstatus', 'department', 'vendorapi', 'vendorapi', 'modified', 'modifier']
    list_filter = ['objecttype', 'servicegroup', 'department']
    inlines = [RequestTemplateFieldInline, RequestTemplateRuleInline]


class ClientAdmin(DictionaryAdmin):
    fields = ['clientid', 'last_name', 'first_name', 'father_name', 'phone', 'email', 'inn', 'snils', 'image', 'djangouser']
    list_display = ['last_name', 'first_name', 'father_name', 'phone', 'email', 'img', 'djangouser']
    search_fields = ['last_name', 'first_name', 'father_name', 'phone', 'email']
    readonly_fields = ['img', 'clientid']


class DepartmentRuleAdmin(DictionaryAdmin):
    fields = ['name', 'requeststatus', 'requesttemplate', 'objecttype', 'valid_from', 'valid_to', 'image', 'description']
    list_display = ['name', 'requeststatus', 'requesttemplate', 'objecttype', 'valid_from', 'valid_to']
    list_filter = ['requeststatus', 'requesttemplate', 'objecttype']


class DepartmentRuleInline(admin.TabularInline):
    fields = ['name', 'requeststatus', 'requesttemplate', 'objecttype', 'valid_from', 'valid_to', 'image', 'description']
    extra = 1
    model = DepartmentRule


class DepartmentAdmin(DictionaryAdmin):
    fields = ['name', 'description', 'img', 'image', 'parent']
    inlines = [DepartmentRuleInline]

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        request._editing_document = object_id is not None  # add attribute
        return super(DepartmentAdmin, self).changeform_view(request, object_id=object_id, form_url=form_url, extra_context=extra_context)


class RequestFieldInline(admin.TabularInline):
    fields = ['templatefield', 'field_value', 'image', 'filename']
    extra = 1
    model = RequestField

    def get_queryset(self, request):
        qs = super(RequestFieldInline, self).get_queryset(request)
        return qs.filter(deleted__isnull = True)


class RequestStatusHistoryInline(admin.TabularInline):
    fields = ['status_date', 'creator', 'rule', 'comments', 'image', 'filename']
    readonly_fields = ['status_date', 'creator']
    extra = 1
    model = RequestStatusHistory

    # def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

        # field = super(RequestStatusHistoryInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

        # if db_field.name == 'rule':
        #     if request._obj_ is not None:
        #         field.queryset = field.queryset.filter(requesttemplate__exact = request._obj_.requesttemplate)
        #     else:
        #         field.queryset = field.queryset.none()
        #
        # return field


class RequestAdmin(admin.ModelAdmin):
    fields = ['request_number', 'client', 'request_date', 'requesttemplate', 'requeststatus', 'current_user', 'status_date', 'finish_date', 'parameters', 'client_comments', 'client_image', 'client_file', 'user_comments', 'user_image', 'user_file']
    # list_display = ['client', 'request_number', 'request_date', 'requesttemplate', 'requeststatus', 'status_date', 'finish_date']
    list_filter = ['requesttemplate', 'requeststatus', 'requesttemplate__objecttype']
    inlines = [RequestFieldInline, RequestStatusHistoryInline]
    raw_id_fields = ['client']
    readonly_fields = ['request_number', 'requeststatus', 'status_date']

    def get_form(self, request, obj=None, **kwargs):
        # just save obj reference for future processing in Inline
        request._obj_ = obj
        return super(RequestAdmin, self).get_form(request, obj, **kwargs)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        request._editing_document = object_id is not None  # add attribute
        return super(RequestAdmin, self).changeform_view(request, object_id=object_id, form_url=form_url, extra_context=extra_context)

    def get_queryset(self, request):
        qs = super(RequestAdmin, self).get_queryset(request)
        return qs.filter(deleted__isnull=True)

    def delete_model(self, request, obj):
        # dbfunction('ratingdelete', {'ratingids': [obj.id]}, request)
        obj.deleted = timezone.make_aware(datetime.now(), timezone.get_default_timezone()).astimezone(timezone.get_default_timezone())
        obj.deleter = request.user
        obj.save()

    def delete_selected(self, request, obj):
        # dbfunction('ratingdelete', {'ratingids': [o.id for o in obj.all()]}, request)
        for o in obj.all():
            o.deleted = timezone.make_naive(timezone.make_aware(datetime.now(), timezone.get_default_timezone()), timezone.get_default_timezone())
            o.deleter = request.user
            o.save()

    def save_model(self, request, obj, form, change):
        obj.modifier=request.user
        obj.modified=timezone.make_naive(timezone.make_aware(datetime.now(), timezone.get_default_timezone()), timezone.get_default_timezone())
        if not obj.creator:
            obj.creator = request.user
            obj.created = obj.modified
        if not obj.requeststatus_id:
            obj.requeststatus = obj.requesttemplate.initstatus
        obj.save()


class RequestStatusHistoryAdmin(admin.ModelAdmin):
    readonly_fields = [field.name for field in RequestStatusHistory._meta.get_fields()]
    list_display = readonly_fields
    list_filter = ['rule', 'request__requesttemplate']


class EmployeeAdmin(DictionaryAdmin):
    fields = ['user', 'department', 'date_in', 'date_out', 'priority', 'modifier', 'modified', 'comments']
    list_display = fields
    list_filter = ['department', 'user']
    readonly_fields = ['modified', 'modifier']


admin.site.register(ServiceGroup, DictionaryAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(ObjectType, DictionaryAdmin)
admin.site.register(RequestStatus, DictionaryAdmin)
admin.site.register(DepartmentRule, DepartmentRuleAdmin)
admin.site.register(VendorApi, VendorApiAdmin)

admin.site.register(PaymentApi, VendorApiAdmin)
admin.site.register(RequestTemplate, RequestTemplateAdmin)
admin.site.register(RequestFieldType, RequestFieldTypeAdmin)

admin.site.register(Client, ClientAdmin)
admin.site.register(RequestStatusHistory, RequestStatusHistoryAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Employee, EmployeeAdmin)
