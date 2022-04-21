from django.core.management.base import BaseCommand
from task.management.commands._utils import search_code


class Command(BaseCommand):
    help = 'Search for promo code'

    def add_arguments(self, parser):
        parser.add_argument('code', action='store')

    def handle(self, *args, **options):
        if search_code(options['code']):
            print("Code found in the group is " + options['code'].split("__")[0])
        else:
            print("Code not found")
