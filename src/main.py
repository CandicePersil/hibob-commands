import sys
import os

from datetime import date

import api
from extractor import csv_dump
from models.employees import Employee, CompanyEmployees


def main():
    employees_search_results = api.extract_employees_data()
    employees_data: dict[str, list[dict[str, str | None]]] = CompanyEmployees(
        employees=[Employee(**employee) for employee in employees_search_results]
    ).model_dump()

    os.path.exists("./results") or os.mkdir("./results")
    file_path = f"./results/employees_{date.today().strftime('%Y%m%d')}.csv"
    if not os.path.exists(file_path):
        csv_dump.CsvWriter(file_path).write_to_file(lines=employees_data["employees"])


if __name__ == "__main__":
    sys.exit(main())
