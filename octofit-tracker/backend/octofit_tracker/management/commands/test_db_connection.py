from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo.errors import ConfigurationError  # Corrected the import

class Command(BaseCommand):
    help = 'Test the database connection defined in settings.py'

    def handle(self, *args, **kwargs):
        try:
            # Attempt to connect to the database
            client = settings.DATABASES['default']['CLIENT']
            host = client['host']
            name = settings.DATABASES['default']['NAME']

            from pymongo import MongoClient
            mongo_client = MongoClient(host)
            db = mongo_client[name]

            # Check if the database is accessible
            db.list_collection_names()
            self.stdout.write(self.style.SUCCESS('Successfully connected to the database.'))
        except ConfigurationError as e:
            self.stderr.write(self.style.ERROR(f'Failed to connect to the database: {e}'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'An error occurred: {e}'))
