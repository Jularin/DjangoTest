from django.core.management.base import BaseCommand
from task.management.commands._utils import add_new_promo


class Command(BaseCommand):
    help = 'Create new promo codes'

    def add_arguments(self, parser):
        parser.add_argument('amount', action='store')
        parser.add_argument('group', action='store')

    def handle(self, *args, **options):
        add_new_promo(options['amount'], options['group'])
        print("All is good")
