import csv
from datetime import date
from itertools import islice
from django.conf import settings
from django.core.management.base import BaseCommand
from analysis.models import WaterData

class Command(BaseCommand):
    help = 'Load data from Melbourne file'

    def handle(self, *args, **kwargs):
        datafile = settings.BASE_DIR / 'data' / 'Data-Melbourne_F.csv'

        with open(datafile, 'r') as csvfile:
            reader = csv.DictReader(islice(csvfile, 2, None))

            for row in reader:
                dt = date(
                month = int(row['month']),
                year = int(row['year']),
                day=1
                )
                WaterData.objects.get_or_create(date=dt,BOD=['BOD'],COD=['COD'])
