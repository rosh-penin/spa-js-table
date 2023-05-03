from django.urls import path

from .views import spa_table_view

app_name = 'table_spa'

urlpatterns = [
    path('', spa_table_view)
]
