from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime
YESNO = ((0, 'Нет'), (1, 'Да'))


class ServiceGroup(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    image = models.FileField(max_length=500, blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, verbose_name='Родитель')
    created = models.DateTimeField(blank=True, null=True, verbose_name='Создан')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Создатель')
    modified = models.DateTimeField(blank=True, null=True, verbose_name='Изменено')
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Изменил')
    deleted = models.DateTimeField(blank=True, null=True, verbose_name='Удалено')
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Удалил')

    class Meta:
        managed = False
        db_table = 'tservicegroup'
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(max_length=500, blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, verbose_name='Родитель')
    created = models.DateTimeField(blank=True, null=True, verbose_name='Создан')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Создатель')
    modified = models.DateTimeField(blank=True, null=True, verbose_name='Изменено')
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Изменил')
    deleted = models.DateTimeField(blank=True, null=True, verbose_name='Удалено')
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Удалил')

    class Meta:
        managed = False
        db_table = 'tdepartment'
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name


class VendorApi(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Название')
    image = models.CharField(max_length=500, blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    url = models.CharField(max_length=500, blank=True, null=True)
    login = models.CharField(max_length=50, blank=True, null=True, verbose_name='Логин')
    password = models.CharField(max_length=50, blank=True, null=True, verbose_name='Пароль')
    sertificate = models.TextField(blank=True, null=True, verbose_name='Сертификат')
    outgoing_code = models.TextField(blank=True, null=True, verbose_name='Действия при отправке')
    parameters_out = models.TextField(blank=True, null=True, verbose_name='Отправляемые параметры')
    incoming_code = models.TextField(blank=True, null=True, verbose_name='Действия при получении')
    parameters_in = models.TextField(blank=True, null=True, verbose_name='Получаемые параметры')
    created = models.DateTimeField(blank=True, null=True, verbose_name='Создан')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Создатель')
    modified = models.DateTimeField(blank=True, null=True, verbose_name='Изменено')
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Изменил')
    deleted = models.DateTimeField(blank=True, null=True, verbose_name='Удалено')
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Удалил')

    class Meta:
        managed = False
        db_table = 'tvendorapi'
        verbose_name = 'Внешний API'
        verbose_name_plural = 'Внешние API'

    def __str__(self):
        return self.name


class ObjectType(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(max_length=500, blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    vendorapi = models.ForeignKey(VendorApi, models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True, verbose_name='Создан')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Создатель')
    modified = models.DateTimeField(blank=True, null=True, verbose_name='Изменено')
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Изменил')
    deleted = models.DateTimeField(blank=True, null=True, verbose_name='Удалено')
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Удалил')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'tobjecttype'
        verbose_name = 'Тип сущности'
        verbose_name_plural = 'Типы сущностей'


class RequestStatus(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(max_length=500, blank=True, null=True, verbose_name='Изображение')
    objecttype = models.ForeignKey(ObjectType, models.DO_NOTHING, blank=True, null=True, verbose_name='Тип')
    created = models.DateTimeField(blank=True, null=True, verbose_name='Создан')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Создатель')
    modified = models.DateTimeField(blank=True, null=True, verbose_name='Изменено')
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Изменил')
    deleted = models.DateTimeField(blank=True, null=True, verbose_name='Удалено')
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Удалил')

    class Meta:
        managed = False
        db_table = 'trequeststatus'
        verbose_name = 'Статус заявления'
        verbose_name_plural = 'Статусы заявлений'

    def __str__(self):
        return self.name


class PaymentApi(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Название')
    image = models.CharField(max_length=500, blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    url = models.CharField(max_length=500, blank=True, null=True)
    login = models.CharField(max_length=50, blank=True, null=True, verbose_name='Логин')
    password = models.CharField(max_length=50, blank=True, null=True, verbose_name='Пароль')
    sertificate = models.TextField(blank=True, null=True, verbose_name='Сертификат')
    outgoing_code = models.TextField(blank=True, null=True, verbose_name='Действия при отправке')
    parameters_out = models.TextField(blank=True, null=True, verbose_name='Отправляемые параметры')
    incoming_code = models.TextField(blank=True, null=True, verbose_name='Действия при получении')
    parameters_in = models.TextField(blank=True, null=True, verbose_name='Получаемые параметры')
    created = models.DateTimeField(blank=True, null=True, verbose_name='Создан')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Создатель')
    modified = models.DateTimeField(blank=True, null=True, verbose_name='Изменено')
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Изменил')
    deleted = models.DateTimeField(blank=True, null=True, verbose_name='Удалено')
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Удалил')

    class Meta:
        managed = False
        db_table = 'tpaymentapi'
        verbose_name = 'Платежная система'
        verbose_name_plural = 'Платежные системы'

    def __str__(self):
        return self.name


class RequestTemplate(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(max_length=500, blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    objecttype = models.ForeignKey(ObjectType, models.DO_NOTHING, verbose_name='Тип')
    servicegroup = models.ForeignKey(ServiceGroup, models.DO_NOTHING, verbose_name='Услуга')
    initstatus = models.ForeignKey(RequestStatus, models.DO_NOTHING, verbose_name='Статус при создании')
    department = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True, verbose_name='Исполнитель')
    vendorapi = models.ForeignKey(VendorApi, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Внешний API')
    paymentapi = models.ForeignKey(PaymentApi, models.DO_NOTHING, blank=True, null=True, verbose_name='API оплаты')
    created = models.DateTimeField(blank=True, null=True, verbose_name='Создан')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Создатель')
    modified = models.DateTimeField(blank=True, null=True, verbose_name='Изменено')
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Изменил')
    deleted = models.DateTimeField(blank=True, null=True, verbose_name='Удалено')
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Удалил')

    class Meta:
        managed = False
        db_table = 'trequesttemplate'
        verbose_name = 'Шаблон заявления'
        verbose_name_plural = 'Шаблоны заявлений'

    def __str__(self):
        return self.name


class RequestFieldType(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(max_length=500, blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    regexp_mask = models.CharField(max_length=500, blank=True, null=True, verbose_name='Маска')
    is_image = models.IntegerField(choices=YESNO, verbose_name='Изображение')
    is_file = models.IntegerField(choices=YESNO, verbose_name='Документ')
    created = models.DateTimeField(blank=True, null=True, verbose_name='Создан')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Создатель')
    modified = models.DateTimeField(blank=True, null=True, verbose_name='Изменено')
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Изменил')
    deleted = models.DateTimeField(blank=True, null=True, verbose_name='Удалено')
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Удалил')

    class Meta:
        managed = False
        db_table = 'trequestfieldtype'
        verbose_name = 'Тип поля'
        verbose_name_plural = 'Типы полей'

    def __str__(self):
        return self.name



class RequestTemplateField(models.Model):
    requesttemplate = models.ForeignKey(RequestTemplate, models.DO_NOTHING, verbose_name='Шаблон')
    requestfieldtype = models.ForeignKey(RequestFieldType, models.DO_NOTHING, verbose_name='Тип поля')
    field_index = models.IntegerField(verbose_name='Позиция')
    name = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(max_length=500, blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    required = models.IntegerField(choices=YESNO, verbose_name='Обязательное поле')
    created = models.DateTimeField(blank=True, null=True, verbose_name='Создан')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Создатель')
    modified = models.DateTimeField(blank=True, null=True, verbose_name='Изменено')
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Изменил')
    deleted = models.DateTimeField(blank=True, null=True, verbose_name='Удалено')
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Удалил')

    class Meta:
        managed = False
        db_table = 'trequesttemplatefield'
        unique_together = (('requesttemplate', 'field_index'),)
        verbose_name = 'Поле шаблона'
        verbose_name_plural = 'Поля шаблона'

    def __str__(self):
        return '%s' % self.name


class DepartmentRule(models.Model):
    department = models.ForeignKey(Department, models.PROTECT, verbose_name='Отдел')
    requeststatus = models.ForeignKey(RequestStatus, models.PROTECT, blank=True, null=True, verbose_name='Статус заявления')
    requesttemplate = models.ForeignKey(RequestTemplate, models.DO_NOTHING, blank=True, null=True, verbose_name='Шаблон заявления')
    objecttype = models.ForeignKey(ObjectType, models.DO_NOTHING, blank=True, null=True, verbose_name='Тип объекта')
    valid_from = models.DateTimeField(default=timezone.make_aware(datetime.now(), timezone.get_default_timezone()).astimezone(timezone.get_default_timezone()), verbose_name='Дата от')
    valid_to = models.DateTimeField(default=datetime(4000, 1, 1), verbose_name='Дата до')
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Название')
    image = models.ImageField(max_length=500, blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    created = models.DateTimeField(blank=True, null=True, verbose_name='Создан')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Создатель')
    modified = models.DateTimeField(blank=True, null=True, verbose_name='Изменено')
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Изменил')
    deleted = models.DateTimeField(blank=True, null=True, verbose_name='Удалено')
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Удалил')

    class Meta:
        managed = False
        db_table = 'tdepartmentrule'
        verbose_name = 'Правила отдела'
        verbose_name_plural = 'Правилы отдела'

    def __str__(self):
        return '%s => %s' % (self.requeststatus, self.objecttype)


class Client(models.Model):
    clientid = models.CharField(max_length=100)
    djangouser = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, verbose_name='Пользователь')
    image = models.ImageField(max_length=500, blank=True, null=True, verbose_name='Изображение')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    father_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Отчество')
    phone = models.CharField(unique=True, max_length=15, verbose_name='Контактный номер')
    email = models.EmailField(unique=True, max_length=100)
    inn = models.BigIntegerField(blank=True, null=True, verbose_name='ИНН')
    snils = models.CharField(max_length=15, blank=True, null=True, verbose_name='СНИЛС')
    created = models.DateTimeField(blank=True, null=True, verbose_name='Создан')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Создатель')
    modified = models.DateTimeField(blank=True, null=True, verbose_name='Изменено')
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Изменил')
    deleted = models.DateTimeField(blank=True, null=True, verbose_name='Удалено')
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Удалил')

    class Meta:
        managed = False
        db_table = 'tclient'
        verbose_name = 'Гражданин'
        verbose_name_plural = 'Граждане'

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

import string
import random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Request(models.Model):
    request_date = models.DateField(default=datetime.now(), verbose_name="Дата заявления")
    request_number = models.CharField(unique=True, max_length=50, verbose_name='Номер заявления', default=id_generator(8))
    client = models.ForeignKey(Client, models.PROTECT, verbose_name='Гражданин')
    requesttemplate = models.ForeignKey(RequestTemplate, models.PROTECT, verbose_name='Шаблон')
    requeststatus = models.ForeignKey(RequestStatus, models.PROTECT, verbose_name='Статус')
    status_date = models.DateTimeField(default=datetime.now(), verbose_name='Дата присвоения')
    finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата завершения')
    client_comments = models.TextField(blank=True, null=True, verbose_name='Комментарий заявителя')
    client_image = models.ImageField(max_length=500, blank=True, null=True, verbose_name='Изображение')
    client_file = models.FileField(max_length=500, blank=True, null=True, verbose_name='Приложенный документ')
    current_user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Текущий ответственный')
    user_comments = models.TextField(blank=True, null=True, verbose_name='Ход работы')
    user_image = models.ImageField(max_length=500, blank=True, null=True, verbose_name='Изображение')
    user_file = models.FileField(max_length=500, blank=True, null=True, verbose_name='Сопроводительный документ')
    parameters = models.TextField(blank=True, null=True, verbose_name='Параметры')
    created = models.DateTimeField(blank=True, null=True, verbose_name='Создан')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Создатель')
    modified = models.DateTimeField(blank=True, null=True, verbose_name='Изменено')
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Изменил')
    deleted = models.DateTimeField(blank=True, null=True, verbose_name='Удалено')
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Удалил')

    class Meta:
        managed = False
        db_table = 'trequest'
        verbose_name = 'Заявление'
        verbose_name_plural = 'Заявления'

    def __str__(self):
        return '%s %s' % (self.requesttemplate.__str__(), self.request_number)

    def save(self, *args, **kwargs):
        self.modified = timezone.make_aware(datetime.now(), timezone.get_default_timezone()).astimezone(timezone.get_default_timezone())
        if not self.requeststatus:
            self.requeststatus = self.requesttemplate.initstatus
        super(Request, self).save(*args, **kwargs)


class RequestField(models.Model):
    request = models.ForeignKey(Request, models.DO_NOTHING, blank=True, null=True, verbose_name='Заявление')
    templatefield = models.ForeignKey(RequestTemplateField, models.PROTECT, blank=True, null=True, verbose_name='Поле шаблона')
    field_value = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Значение поля')
    image = models.ImageField(max_length=500, blank=True, null=True, verbose_name='Изображение')
    filename = models.FileField(max_length=500, blank=True, null=True, verbose_name='Имя файла')
    created = models.DateTimeField(blank=True, null=True, verbose_name='Создан')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Создатель')
    modified = models.DateTimeField(blank=True, null=True, verbose_name='Изменено')
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Изменил')
    deleted = models.DateTimeField(blank=True, null=True, verbose_name='Удалено')
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Удалил')

    class Meta:
        managed = False
        db_table = 'trequestfield'
        verbose_name = 'Поле заявления'
        verbose_name_plural = 'Поля заявления'


class RequestTemplateRule(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    image = models.CharField(max_length=500, blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    requesttemplate = models.ForeignKey(RequestTemplate, models.PROTECT, verbose_name='Шаблон')
    prev_status = models.ForeignKey(RequestStatus, models.PROTECT, related_name='+', verbose_name='Предыдущий статус')
    next_status = models.ForeignKey(RequestStatus, models.PROTECT, related_name='+', verbose_name='Следующий статус')
    requiredfield = models.ForeignKey(RequestTemplateField, models.PROTECT, blank=True, null=True, verbose_name='Требуемое поле')
    vendorapi = models.ForeignKey(VendorApi, models.PROTECT, blank=True, null=True, verbose_name='Внешний API')
    parameters = models.TextField(blank=True, null=True, verbose_name='Параметры')
    paymentapi = models.ForeignKey(PaymentApi, models.PROTECT, blank=True, null=True, verbose_name='Платежный модуль')
    max_days = models.DecimalField(max_digits=6, decimal_places=3, verbose_name='Срок')
    created = models.DateTimeField(blank=True, null=True, verbose_name='Создан')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Создатель')
    modified = models.DateTimeField(blank=True, null=True, verbose_name='Изменено')
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Изменил')
    deleted = models.DateTimeField(blank=True, null=True, verbose_name='Удалено')
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Удалил')

    class Meta:
        managed = False
        db_table = 'trequesttemplaterule'
        unique_together = (('requesttemplate', 'prev_status', 'next_status'),)
        verbose_name = 'Правило бизнес логики'
        verbose_name_plural = 'Правила бизнес логики'

    def save(self, *args, **kwargs):
        self.modified = timezone.make_aware(datetime.now(), timezone.get_default_timezone()).astimezone(timezone.get_default_timezone())
        super(RequestTemplateRule, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class RequestStatusHistory(models.Model):
    request = models.ForeignKey(Request, models.PROTECT, verbose_name='Заявление')
    rule = models.ForeignKey(RequestTemplateRule, models.PROTECT, verbose_name='Правило')
    status_date = models.DateTimeField(default=datetime.now(), verbose_name='Дата присвоения')
    prev_status = models.ForeignKey(RequestStatus, models.PROTECT, related_name='+', verbose_name='Предыдущий статус')
    next_status = models.ForeignKey(RequestStatus, models.PROTECT, related_name='+', verbose_name='Следующий статус')
    comments = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    image = models.ImageField(max_length=500, blank=True, null=True, verbose_name='Изображение')
    filename = models.FileField(max_length=500, blank=True, null=True, verbose_name='Имя файла')
    param_values = models.TextField(blank=True, null=True, verbose_name='Значения параметров')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.PROTECT, blank=True, null=True, verbose_name='Пользователь')

    def save(self, *args, **kwargs):
        self.prev_status = self.request.requeststatus if self.request.requeststatus else self.request.requesttemplate.initstatus
        self.next_status = self.rule.next_status
        self.modified = timezone.make_aware(datetime.now(), timezone.get_default_timezone()).astimezone(timezone.get_default_timezone())
        req = self.request
        req.requeststatus = self.next_status
        req.save()
        super(RequestStatusHistory, self).save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'trequeststatushistory'
        verbose_name = 'История заявления'
        verbose_name_plural = 'Истроии заявлений'

    def __str__(self):
        return '%s' % self.rule


class Employee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.PROTECT, verbose_name='Пользователь')
    department = models.ForeignKey(Department, models.PROTECT, 'Отдел')
    date_in = models.DateTimeField(default=timezone.make_aware(datetime.now(), timezone.get_default_timezone()).astimezone(timezone.get_default_timezone()), verbose_name='Дата от')
    date_out = models.DateTimeField(default=datetime(4000, 1, 1), verbose_name='Дата до')
    priority = models.IntegerField(default=5, verbose_name='Приоритет', help_text='От 1 до 10')
    comments = models.TextField(verbose_name='Комментарии', blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True, verbose_name='Создан')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Создатель')
    modified = models.DateTimeField(blank=True, null=True, verbose_name='Изменено')
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Изменил')
    deleted = models.DateTimeField(blank=True, null=True, verbose_name='Удалено')
    deleter = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True, related_name='+', verbose_name='Удалил')

    class Meta:
        managed = False
        db_table = 'temployee'
        verbose_name = 'Сотрудник отдела'
        verbose_name_plural = 'Сотрудники отделов'

