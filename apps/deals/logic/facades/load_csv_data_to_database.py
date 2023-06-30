import io

from apps.deals.logic.interactors.deals__csv_data_importer import parse_csv_data, validate_csv_data, write_deals_to_db


def load_csv_data_to_database(*, file_obj: bytes) -> dict[str, str]:
    """Заргужает данные из полученного файла в базу данных."""
    try:
        csv_file = io.StringIO(file_obj.read().decode('utf-8'))
        validate_data = validate_csv_data(csv_data=parse_csv_data(csv_file=csv_file))
        write_deals_to_db(deal_object_list=validate_data)
        return {'Status': 'OK'}
    except Exception as e:
        return {'Status': 'Error', 'Desc': str(e)}
