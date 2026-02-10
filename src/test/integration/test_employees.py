from models.employees import CompanyEmployees, Employee, Work, Payroll, Employment, Root


def test_validate_employee_data() -> None:
    # GIVEN
    input = {
        "payroll": {
                "employment": {
                        "type": "Permanent",
                }
        },
        "work": {
                "startDate": "2025-10-02",
                "site": "France"
        },
        "root" : {
            "surname": "Star",
            "firstName": "Noemie",
            "email": "noemie.start@random.ex"
        }
    }

    # WHEN
    employee = Employee(**input)

    # THEN
    assert employee == Employee(
        payroll=Payroll(
            employment=Employment(
                type=input["payroll"]["employment"]["type"],
            )
        ),
        work=Work(
            startDate=input["work"]["startDate"],
            site=input["work"]["site"],
        ),
        root=Root(
            firstName=input["root"]["firstName"],
            surname=input["root"]["surname"],
            email=input["root"]["email"],
        ),
    )


def test_validate_multiple_employees_data() -> None:
    # GIVEN
    input = {
        "payroll": {
                "employment": {
                        "type": "Permanent",
                }
        },
        "work": {
                "startDate": "2025-10-02",
                "site": "France"
        },
        "root" : {
            "surname": "Star",
            "firstName": "Noemie",
            "email": "noemie.star@example.ex",
        }
    }

    list_of_employees: list[Employee] = []
    range_of_employees = range(0, 10, 1)
    for i in range_of_employees:
        employee = Employee(**input)
        list_of_employees.append(employee)

    # WHEN
    employees = CompanyEmployees(employees=list_of_employees)

    expected_employees = [
        Employee(
        payroll=Payroll(
            employment=Employment(
                type=input["payroll"]["employment"]["type"],
            )
        ),
        work=Work(
            startDate=input["work"]["startDate"],
            site=input["work"]["site"],
        ),
        root=Root(
            firstName=input["root"]["firstName"],
            surname=input["root"]["surname"],
            email=input["root"]["email"],
        ),
    )
        for i in range_of_employees
    ]

    # THEN
    assert employees == CompanyEmployees(employees=expected_employees)

def test_extract_employees_data() -> None:
    # GIVEN
    employees = CompanyEmployees(
        employees=[
            Employee(
                payroll=Payroll(
                    employment=Employment(
                        type="Permanent",
                    )
                ),
                work=Work(
                    startDate="2025-10-02",
                    site="Paris",
                ),
                root=Root(
                    firstName="Noemie",
                    surname="Star",
                    email="noemie.star@example.ex",
                ),
            ),
            Employee(
                payroll=Payroll(
                    employment=Employment(
                        type="Permanent",
                    )
                ),
                work=Work(
                    startDate="2025-10-01",
                    site="London",
                ),
                root=Root(
                    firstName="Mimi",
                    surname="Renolds",
                    email="mimi.renolds@example.ex",
                ),
            ), 
        ]
    )

    # WHEN
    extracted_data = employees.model_dump()
    assert extracted_data == {
        "employees": [
            {
                "area": "Paris",
                "contract_type": "Permanent",
                "date_of_birth": None,
                "email": "noemie.star@example.ex",
                "end_date": None,
                "first_name": "Noemie",
                "last_name": "Star",
                "phone_number": None,
                "professional_category": None,
                "start_date": "02/10/2025",
                "subsidy_level": None,
            },
            {
                "area": "London",
                "contract_type": "Permanent",
                "date_of_birth": None,
                "email": "mimi.renolds@example.ex",
                "end_date": None,
                "first_name": "Mimi",
                "last_name": "Renolds",
                "phone_number": None,
                "professional_category": None,
                "start_date": "01/10/2025",
                "subsidy_level": None,
            },
        ]
    }
