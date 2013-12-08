from django.core.management.base import BaseCommand, CommandError
from transactions.utils import sync_figo_transactions

class Command(BaseCommand):
    def handle(self, *args, **options):
        sync_figo_transactions()
        self.stdout.write('Successfully synced transactions')
