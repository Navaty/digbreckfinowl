from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime
YESNO = ((0, 'Нет'), (1, 'Да'))


class ServiceGroup(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    modified = models.DateTimeField(blank=True, null=True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    deleted = models.DateTimeField(blank=True, null=True)
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')

    class Meta:
        managed = False
        db_table = 'tservicegroup'

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    modified = models.DateTimeField(blank=True, null=True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    deleted = models.DateTimeField(blank=True, null=True)
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')

    class Meta:
        managed = False
        db_table = 'tdepartment'

    def __str__(self):
        return self.name


class VendorApi(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    login = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    sertificate = models.TextField(blank=True, null=True)
    outgoing_code = models.TextField(blank=True, null=True)
    parameters_out = models.TextField(blank=True, null=True)
    incoming_code = models.TextField(blank=True, null=True)
    parameters_in = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    modified = models.DateTimeField(blank=True, null=True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    deleted = models.DateTimeField(blank=True, null=True)
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')

    class Meta:
        managed = False
        db_table = 'tvendorapi'

    def __str__(self):
        return self.name


class ObjectType(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    vendorapi = models.ForeignKey(VendorApi, models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    modified = models.DateTimeField(blank=True, null=True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    deleted = models.DateTimeField(blank=True, null=True)
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'tobjecttype'


class RequestStatus(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(max_length=500, blank=True, null=True)
    objecttype = models.ForeignKey(ObjectType, models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    modified = models.DateTimeField(blank=True, null=True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    deleted = models.DateTimeField(blank=True, null=True)
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')

    class Meta:
        managed = False
        db_table = 'trequeststatus'

    def __str__(self):
        return self.name


class PaymentApi(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    login = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    sertificate = models.TextField(blank=True, null=True)
    outgoing_code = models.TextField(blank=True, null=True)
    parameters_out = models.TextField(blank=True, null=True)
    incoming_code = models.TextField(blank=True, null=True)
    parameters_in = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    modified = models.DateTimeField(blank=True, null=True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    deleted = models.DateTimeField(blank=True, null=True)
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')

    class Meta:
        managed = False
        db_table = 'tpaymentapi'

    def __str__(self):
        return self.name


class RequestTemplate(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    objecttype = models.ForeignKey(ObjectType, models.DO_NOTHING)
    servicegroup = models.ForeignKey(ServiceGroup, models.DO_NOTHING)
    initstatus = models.ForeignKey(RequestStatus, models.DO_NOTHING)
    department = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    vendorapi = models.ForeignKey(VendorApi, blank=True, null=True, on_delete=models.PROTECT)
    paymentapi = models.ForeignKey(PaymentApi, models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    modified = models.DateTimeField(blank=True, null=True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    deleted = models.DateTimeField(blank=True, null=True)
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')

    class Meta:
        managed = False
        db_table = 'trequesttemplate'

    def __str__(self):
        return self.name


class RequestFieldType(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    regexp_mask = models.CharField(max_length=500, blank=True, null=True)
    is_image = models.IntegerField(choices=YESNO)
    is_file = models.IntegerField(choices=YESNO)
    created = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    modified = models.DateTimeField(blank=True, null=True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    deleted = models.DateTimeField(blank=True, null=True)
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')

    class Meta:
        managed = False
        db_table = 'trequestfieldtype'

    def __str__(self):
        return self.name


class RequestTemplateField(models.Model):
    requesttemplate = models.ForeignKey(RequestTemplate, models.DO_NOTHING)
    requestfieldtype = models.ForeignKey(RequestFieldType, models.DO_NOTHING)
    field_index = models.IntegerField()
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    required = models.IntegerField(choices=YESNO)
    created = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    modified = models.DateTimeField(blank=True, null=True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    deleted = models.DateTimeField(blank=True, null=True)
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')

    class Meta:
        managed = False
        db_table = 'trequesttemplatefield'
        unique_together = (('requesttemplate', 'field_index'),)

    def __str__(self):
        return '%s, %s' % (self.requesttemplate.__str__(), self.name)


class DepartmentRule(models.Model):
    requeststatus = models.ForeignKey(RequestStatus, models.DO_NOTHING, blank=True, null=True)
    requesttemplate = models.ForeignKey(RequestTemplate, models.DO_NOTHING, blank=True, null=True)
    objecttype = models.ForeignKey(ObjectType, models.DO_NOTHING, blank=True, null=True)
    valid_from = models.DateTimeField(default=timezone.make_aware(datetime.now(), timezone.get_default_timezone()).astimezone(timezone.get_default_timezone()))
    valid_to = models.DateTimeField(datetime(4000, 1, 1))
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    modified = models.DateTimeField(blank=True, null=True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')
    deleted = models.DateTimeField(blank=True, null=True)
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+')

    class Meta:
        managed = False
        db_table = 'tdepartmentrule'

    def __str__(self):
        return '%s => %s' % (self.requeststatus, self.objecttype)