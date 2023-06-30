import csv
from collections.abc import Iterator
from datetime import datetime

from django.contrib.auth import get_user_model

from apps.deals.logic.dto import DealDto
from apps.deals.models import Deal, Gem

User = get_user_model()


def parse_csv_data(*, csv_file: str) -> Iterator[str]:
    """Читает данные из csv-файла и возвращает Dto с данными."""
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        if row:
            yield row


def validate_csv_data(*, csv_data: Iterator[str]) -> list[DealDto]:
    """Проверяет полученные из файла данные."""
    deal_object_list = []
    for row in csv_data:
        customer, item, total, quantity, date_string = row
        customer, _ = User.objects.get_or_create(username=customer)
        item, _ = Gem.objects.get_or_create(name=item)
        date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')

        deal_dto = DealDto(customer=customer, item=item, total=total, quantity=quantity, date=date)

        deal_object_list.append(
            Deal(
                customer=deal_dto.customer,
                item=deal_dto.item,
                total=deal_dto.total,
                quantity=deal_dto.quantity,
                date=deal_dto.date,
            )
        )
    return deal_object_list


def write_deals_to_db(*, deal_object_list: list[DealDto]) -> None:
    """Делает запись полученных данных о сделках в базу данных."""
    Deal.objects.bulk_create(objs=deal_object_list)
