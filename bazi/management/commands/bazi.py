from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = '算八字'

    def add_arguments(self, parser):
        # parser.add_argument('poll_ids', nargs='+', type=int)
        pass

    def log_info(self, message):
        self.stdout.write(self.style.SUCCESS(message))

    def handle(self, *args, **options):
        self.log_info("还没写呢 ^_^ ")
