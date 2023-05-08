import json
from django.core.management.base import BaseCommand
from analiz.models import Marketplace

class Command(BaseCommand):
    help = 'Imports marketplace data from JSON file'

    def handle(self, *args, **options):
        with open(r'C:\Users\Intern PC\Desktop\Bazaar-Analiz\analiz\management\commands\Marketplaces.json',encoding="utf8") as f:
            data = json.load(f)
        
        for item in data:
            marketplace = Marketplace.objects.create(
                marketplace_name=item['marketplace_name'],
                marketplace_addres=item['marketplace_addres'],
                lat=item['lat'],
                long=item['long'],
                day=item['day']
            )

        
        self.stdout.write(self.style.SUCCESS('Marketplace data imported successfully.'))


#python manage.py import_marketplace_data
