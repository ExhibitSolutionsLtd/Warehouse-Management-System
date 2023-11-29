import openpyxl
from .models import Product


def import_from_excel(file):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):  # Assuming first row is header
        Product.objects.create(sku=row[0], item_name=row[1], category=row[2], quantity=row[3], description=row[4])