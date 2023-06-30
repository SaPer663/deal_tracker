from django.urls import path

from apps.deals.api.views import extract_top_five_customers, upload_csv

app_name = 'api'
urlpatterns = [path('upload_csv/', upload_csv), path('extract_top/', extract_top_five_customers)]
