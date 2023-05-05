from django.contrib import admin
from django.urls import include, path

from table_spa.utils import populate_empty_table

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('table_spa.urls'))
]

populate_empty_table()
