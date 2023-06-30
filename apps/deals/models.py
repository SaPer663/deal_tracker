from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Gem(models.Model):
    """Данные о драгоценных камнях."""

    name = models.CharField(verbose_name='Название', max_length=100, unique=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Драгоценный камень'
        verbose_name_plural = 'Драгоценные камни'

    def __str__(self):
        return self.name


class Deal(models.Model):
    """Данные о сделке по покупке драгоценного каммня."""

    customer = models.ForeignKey(User, verbose_name='Клиент', on_delete=models.PROTECT, related_name='deals')
    item = models.ForeignKey(Gem, verbose_name='Драгоценный камень', on_delete=models.CASCADE, related_name='deals')
    total = models.PositiveSmallIntegerField(verbose_name='Итоговая сумма сделки')
    quantity = models.PositiveSmallIntegerField(verbose_name='Общее количество камней')
    date = models.DateTimeField(verbose_name='Дата и время сделки', unique=True)

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'

    def __str__(self):
        return f'{self.customer.username}  {self.date}'
