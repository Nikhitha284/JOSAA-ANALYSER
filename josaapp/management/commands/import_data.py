import csv
from django.core.management.base import BaseCommand
from josaapp.models import SeatAllotment

class Command(BaseCommand):
    help = 'Import data from final_data.csv'

    def handle(self, *args, **options):
        file_path = 'data/semif1.csv'  # Replace with the actual file path

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                seat_allotment = SeatAllotment(
                    Institute_name=row['Institute'],
                    year=row['Year'],
                    branch=row['Academic Program Name'],
                    category=row['Seat Type'],
                    gender=row['Gender'],
                    opening_rank=row['Opening Rank'],
                    closing_rank=row['Closing Rank'],
                    round_no=row['Round']
                )
                seat_allotment.save()
        
        self.stdout.write(self.style.SUCCESS('Data import completed successfully.'))
