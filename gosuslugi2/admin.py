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


class RequestTemplateFieldInline(admin.TabularInline):
    fields = ['name', 'requestfieldtype', 'field_index', 'image', 'required', 'description']
    extra = 1
    model = RequestTemplateField

    def get_queryset(self, request):
        qs = super(RequestTemplateFieldInline, self).get_queryset(request)
        return qs.filter(deleted__isnull = True)


class RequestTemplateAdmin(DictionaryAdmin):
    fields = ['name', 'image', 'objecttype', 'servicegroup', 'description', 'initstatus', 'department', 'vendorapi', 'paymentapi']
    list_display = ['name', 'img', 'objecttype', 'servicegroup', 'description', 'initstatus', 'department', 'vendorapi', 'vendorapi', 'modified', 'modifier']
    list_filter = ['objecttype', 'servicegroup', 'department']
    inlines = [RequestTemplateFieldInline]


class RequestFieldTypeAdmin(DictionaryAdmin):
    fields = ['name', 'image', 'regexp_mask', 'is_image', 'is_file', 'description']
    list_display = ['name', 'img', 'regexp_mask', 'is_image', 'is_file', 'description']


admin.site.register(ServiceGroup, DictionaryAdmin)
admin.site.register(Department, DictionaryAdmin)
admin.site.register(ObjectType, DictionaryAdmin)
admin.site.register(RequestStatus, DictionaryAdmin)
admin.site.register(DepartmentRule, DictionaryAdmin)
admin.site.register(VendorApi, VendorApiAdmin)

admin.site.register(PaymentApi, VendorApiAdmin)
admin.site.register(RequestTemplate, RequestTemplateAdmin)
admin.site.register(RequestFieldType, RequestFieldTypeAdmin)