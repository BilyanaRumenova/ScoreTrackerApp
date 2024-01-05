from django.core.management.base import BaseCommand, CommandError

from candidates.utils import read_json_data


class Command(BaseCommand):
    help = "Read the provided JSON file and write out a CSV file  with candidates ordered by score."

    def add_arguments(self, parser):
        parser.add_argument("json_file_path", type=str, help="Path to the JSON file")
        parser.add_argument(
            "--output",
            type=str,
            default="candidates.csv",
            help="Path to the output CSV file",
        )

    def handle(self, *args, **options):
        json_file_path = options["json_file_path"]
        output_csv_path = options["output"]
        try:
            read_json_data(json_file_path, output_csv_path)

            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully imported JSON data and created CSV file"
                )
            )

        except Exception as e:
            raise CommandError(str(e))
