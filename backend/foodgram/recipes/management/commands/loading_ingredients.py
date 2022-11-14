import csv

from django.core.management import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):

    def handle(self, *args, **options):

        print('Uploading ingredients.csv to Ingredient table')
        fhand = open('../../data/ingredients.csv')
        reader = csv.reader(fhand)

        for row in reader:
            print(row)
            i, created = Ingredient.objects.get_or_create(
                name=row[0], measurement_unit=row[1])
            print(i)