import xlrd

DATE_HEADERS = ["start_date", "end_date", "date_of_birth"]


class ExcelExtractor:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract(self) -> list[dict[str, str | None]]:
        workbook = xlrd.open_workbook(self.file_path)
        main_sheet = workbook.sheet_by_index(0)  # file should only contain one sheet

        header = main_sheet.row_values(0, start_colx=0, end_colx=None)
        keys = [key.strip() for key in header]

        extracted_data: list[dict[str, str | None]] = []

        for row in main_sheet.get_rows():
            row_data = {}
            for index_cell, cell in enumerate(row):
                if type(cell.value) is str:
                    row_data[keys[index_cell]] = cell.value.strip()
                if keys[index_cell] in DATE_HEADERS and type(cell.value) is float:
                    row_data[keys[index_cell]] = (
                        xlrd.xldate_as_datetime(cell.value, 0)
                        .date()
                        .strftime("%Y-%m-%d")
                    )
                else:
                    row_data[keys[index_cell]] = cell.value
            extracted_data.append(row_data)

        return extracted_data
