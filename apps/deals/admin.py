from django.contrib import admin
from django.contrib.auth import get_user_model

from apps.deals.models import Deal, Gem

User = get_user_model()


@admin.register(Gem)
class CategoriesAdmin(admin.ModelAdmin):
    """Админ панель данных о драгоценных камнях."""

    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Deal)
class DealsAdmin(admin.ModelAdmin):
    """Админ панель данных о сделках."""

    list_display = ('id', 'customer', 'item', 'total', 'quantity', 'date')
    search_fields = ('item__name', 'customer__username')
