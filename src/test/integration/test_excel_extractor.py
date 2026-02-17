from extractor import excel


def test_excel_extractor() -> None:
    # GIVEN
    file_path = "./test/files/test_users.xls"
    extractor = excel.ExcelExtractor(file_path)

    # WHEN
    extraction = extractor.extract()

    # THEN
    assert extraction == [
        {
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email",
            "start_date": "start_date",
            "end_date": "end_date",
            "contract_type": "contract_type",
            "phone_number": "phone_number",
            "date_of_birth": "date_of_birth",
            "address": "address",
            "gender": "gender",
            "professional_category": "professional_category",
            "subsidy_level": "subsidy_level",
            "area": "area",
        },
        {
            "first_name": "Maria",
            "last_name": "Carret",
            "email": "test.co@example.com",
            "start_date": "2023-01-30",
            "end_date": "",
            "contract_type": "Permanent",
            "phone_number": "",
            "date_of_birth": "",
            "address": "random address",
            "gender": "female",
            "professional_category": 0.0,
            "subsidy_level": 0.0,
            "area": "Paris (FR)",
        },
        {
            "first_name": "Jean",
            "last_name": "Mouet",
            "email": "tester@example.com",
            "start_date": "2023-01-25",
            "end_date": "2025-02-24",
            "contract_type": "Permanent",
            "phone_number": "",
            "date_of_birth": "",
            "address": "random address 2",
            "gender": "male",
            "professional_category": 0.0,
            "subsidy_level": 0.0,
            "area": "Paris (FR)",
        },
    ]
