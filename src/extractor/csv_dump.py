import csv


class CsvWriter:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.field_names = [
            "email",
            "first_name",
            "last_name",
            "start_date",
            "end_date",
            "contract_type",
            "date_of_birth",
            "phone_number",
            "professional_category",
            "subsidy_level",
            "area",
        ]

    def write_to_file(self, lines: list[dict[str, str | None]]) -> None:
        if not lines:
            return

        with open(self.file_path, "w", newline="") as csv_file:
            writer = csv.DictWriter(
                csv_file, delimiter=",", fieldnames=self.field_names
            )
            writer.writeheader()
            writer.writerows(lines)
