import csv

from django.core.management import BaseCommand
from recipes.models import Tag


class Command(BaseCommand):

    def handle(self, *args, **options):

        print('Uploading Tags.csv to Tag table')
        fhand = open('tags.csv')
        reader = csv.reader(fhand)

        for row in reader:
            print(row)
            i, created = Tag.objects.get_or_create(
                name=row[0], slug=row[1], color=row[2])
            print(i)
