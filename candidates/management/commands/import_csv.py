from django.core.management.base import BaseCommand, CommandError

from candidates.utils import import_csv_data


class Command(BaseCommand):
    help = "Read a CSV file into to the system to add candidates and their scores to the DB."

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file_path", type=str, help="Path to the CSV file to be imported"
        )

    def handle(self, *args, **options):
        csv_file_path = options["csv_file_path"]
        try:
            import_csv_data(csv_file_path)

            self.stdout.write(self.style.SUCCESS("Data import completed successfully."))
        except Exception as e:
            raise CommandError(str(e))
