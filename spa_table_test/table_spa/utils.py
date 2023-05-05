import datetime
import random
import string

from .constants import AUTO_GEN_AMOUNT
from .models import TableRow


def populate_empty_table():
    """
    If db table is empty - creates new rows.
    Amount of rows controlled by constant AUTO_GEN_AMOUNT.
    Preferably called from main urls.py since its imported only once.
    """
    if not TableRow.objects.all().exists():
        list_of_objects = []
        for _ in range(AUTO_GEN_AMOUNT):
            list_of_objects.append(TableRow(
                date=datetime.date(
                    random.randint(1990, 2023),
                    random.randint(1, 12),
                    random.randint(1, 25)
                ),
                name=''.join(random.choices(string.ascii_letters, k=10)),
                amount=random.randint(1, 100),
                distance=random.randint(1, 1000)
            ))
        TableRow.objects.bulk_create(list_of_objects)
