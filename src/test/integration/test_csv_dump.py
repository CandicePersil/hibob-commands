import os

from extractor import csv_dump


def test_csv_dump(tmp_path) -> None:
    # GIVEN
    input_lines = [
        {
            "email": "clara.doxal@test.fr",
            "first_name": "Clara",
            "last_name": "Doxal",
            "start_date": "01/12/2025",
            "end_date": None,
            "contract_type": "Permanent",
            "date_of_birth": None,
            "phone_number": None,
            "professional_category": None,
            "area": "Paris",
        },
        {
            "email": "mateo.portu@test.fr",
            "first_name": "Mateo",
            "last_name": "Portu",
            "start_date": "13/09/2024",
            "end_date": "01/31/2025",
            "contract_type": "CDI",
            "date_of_birth": None,
            "phone_number": None,
            "professional_category": None,
            "area": "Lyon",
        },
    ]

    # WHEN
    csv_writer = csv_dump.CsvWriter(tmp_path / "test.csv")
    csv_writer.write_to_file(lines=input_lines)

    # THEN
    assert os.path.exists(tmp_path / "test.csv")
    with open(tmp_path / "test.csv", "r") as csv_file:
        csv_content = csv_file.readlines()
        assert csv_content == [
            "email,first_name,last_name,start_date,end_date,contract_type,date_of_birth,phone_number,professional_category,area\n",
            "clara.doxal@test.fr,Clara,Doxal,01/12/2025,,Permanent,,,,Paris\n",
            "mateo.portu@test.fr,Mateo,Portu,13/09/2024,01/31/2025,CDI,,,,Lyon\n",
        ]

    # CLEANUP
    os.remove(tmp_path / "test.csv")
    assert not os.path.exists(tmp_path / "test.csv")
