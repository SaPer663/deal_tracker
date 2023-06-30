from datetime import datetime

from django.contrib.auth import get_user_model
from pydantic import BaseModel

from apps.deals.models import Gem

User = get_user_model()


class DealDto(BaseModel):
    """Данные о сделках, получаемые из csv."""

    customer: User
    item: Gem
    total: int
    quantity: int
    date: datetime

    class Config:
        arbitrary_types_allowed = True
        allow_mutation = False


class SpendingCustomersDto(BaseModel):
    """Данные о пользователях с самими большими затратами на сделки."""

    username: str
    spent_money: int
    gems: list[str]


class ResponseSpendingCustomersDto(BaseModel):
    """Данные возвращаемые в ответе на запрос о пользователях."""

    response: list[SpendingCustomersDto]
