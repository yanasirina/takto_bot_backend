from django.db import models


class PromoCode(models.Model):
    name = models.CharField('Название', max_length=255, unique=True, db_index=True)
    student = models.ForeignKey('core.Student', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField('Описание', help_text='можно указать размер скидки или особые условия')
    is_active = models.BooleanField('Статус', default=True)
