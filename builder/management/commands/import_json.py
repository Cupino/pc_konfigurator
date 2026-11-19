import json
from django.core.management.base import BaseCommand
from builder.models import CPU, Motherboard, RAM, GPU, CPUCooler, Case, Storage, PSU

class Command(BaseCommand):
    help = 'Import components from a JSON file into the database'

    def handle(self, *args, **kwargs):
        with open('components_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        CPU.objects.all().delete()
        Motherboard.objects.all().delete()
        RAM.objects.all().delete()
        GPU.objects.all().delete()
        CPUCooler.objects.all().delete()
        Case.objects.all().delete()
        Storage.objects.all().delete()
        PSU.objects.all().delete()

        for item in data.get('cpus', []):
            CPU.objects.create(**item)

        for item in data.get('motherboards', []):
            Motherboard.objects.create(**item)

        for item in data.get('rams', []):
            RAM.objects.create(**item)

        for item in data.get('gpus', []):
            GPU.objects.create(**item)

        for item in data.get('coolers', []):
            CPUCooler.objects.create(**item)

        for item in data.get('cases', []):
            Case.objects.create(**item)

        for item in data.get('storages', []):
            Storage.objects.create(**item)

        for item in data.get('psus', []):
            PSU.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('All components from the JSON file have been successfully saved to the database!'))