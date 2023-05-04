from django.shortcuts import render

from .models import TableRow


def spa_table_view(request):
    rows = TableRow.objects.all()
    return render(request, 'table_spa/spa.html', {'rows': rows})
