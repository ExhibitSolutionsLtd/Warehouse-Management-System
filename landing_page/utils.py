import openpyxl
from .models import Product, Location, generate_qr_code


def import_from_excel(file, user):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active


    for row in sheet.iter_rows(min_row=2, values_only=True):  # Assuming first row is header
        zone = row[3]
        item_row = row[4]
        bay = row[5]
        tier = row[6]
        location, created = Location.objects.get_or_create(zone = zone, row = item_row, bay = bay, tier = tier)
        

        product = Product(sku=row[0], item_name=row[1], category=row[2], quantity=row[7], description=row[8], location=location, user=user)
        product.save()