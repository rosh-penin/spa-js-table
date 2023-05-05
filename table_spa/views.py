from django.core.paginator import Paginator
from django.shortcuts import render

from .constants import PAGE_LIMIT
from .models import TableRow


def spa_table_view(request):
    """Get all rows from db, paginate them and toss into template."""
    rows = TableRow.objects.all()
    paginated_rows = Paginator(rows, PAGE_LIMIT)
    page_num = request.GET.get('page')
    page = paginated_rows.get_page(page_num)
    return render(request, 'table_spa/spa.html', {'page': page})
