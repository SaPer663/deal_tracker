from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.deals.logic.facades import extract_top_spending_customers, load_csv_data_to_database


@extend_schema(
    # request={'multipart/form-data': OpenApiTypes.BINARY},
    operation_id='upload_csv',
    request={
        'multipart/form-data': {
            'type': 'object',
            'properties': {
                'deals': {'description': 'csv-файл с данными по сделкам', 'type': 'string', 'format': 'binary'}
            },
        }
    },
    responses=inline_serializer(name='InlineFormSerializer', fields={'Status': serializers.CharField()}),
)
@api_view(['POST'])
def upload_csv(request) -> Response:
    """Загружает данные о сделках из csv-файла."""
    deals_file = request.FILES.get('deals')
    if deals_file is None:
        return Response({'Status': 'Error', 'Desc': 'No file provided'})
    result = load_csv_data_to_database(file_obj=deals_file)
    if result.get('Status') == 'OK':
        return Response(result, status=status.HTTP_201_CREATED)
    return Response(result, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    operation_id='extract_top_five_customers',
    responses=inline_serializer(
        name='InlineOneOffSerializer',
        fields={
            'response': inline_serializer(
                name='NestedInlineOneOffSerializer',
                fields={
                    'username': serializers.CharField(),
                    'spent_money': serializers.IntegerField(),
                    'gems': serializers.ListField(),
                },
            )
        },
    ),
)
@api_view(['GET'])
def extract_top_five_customers(request) -> Response:
    """Возвращает данные по затратам на сделки 5 пользователей с самыми большими суммами."""
    return Response(extract_top_spending_customers(), status=status.HTTP_200_OK)
