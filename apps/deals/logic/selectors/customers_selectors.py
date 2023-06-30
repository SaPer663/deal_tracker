from django.db.models import Count, QuerySet, Sum
from django.db.models.functions import Coalesce

from apps.deals.models import Deal, Gem


def extract_top_five_customers() -> QuerySet:
    """Возвращает пять имён пользователей с самими большими суммами потраченных средств на сделки."""
    return (
        Deal.objects.values('customer__username')
        .annotate(spent_money=Coalesce(Sum('total'), 0))
        .order_by('-spent_money')[:5]
    )


def extract_gem_names(customers, current_customer) -> QuerySet:
    """Возвращает списк камней, которые были куплены как минимум двумя пользователями."""
    gem_names_multiple_buyers = (
        Gem.objects.filter(
            deals__customer__username__in=[customer.get('customer__username') for customer in customers]
        )
        .annotate(num_buyers=Count('deals__customer__username', distinct=True))
        .filter(num_buyers__gte=2)
        .values_list('name', flat=True)
    )

    gem_names_current_customer = gem_names_multiple_buyers.filter(
        deals__customer__username=current_customer
    ).distinct()

    return gem_names_current_customer
