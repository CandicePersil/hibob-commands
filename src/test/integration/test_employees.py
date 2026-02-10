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
            firstName=input["firstName"],
            surname=input["surname"],
            work=Work(
                startDate=input["work"]["startDate"],
                contractType=input["work"]["contractType"],
                title=input["work"]["title"],
                site=input["work"]["site"],
            ),
        )
        for i in range_of_employees
    ]

    # THEN
    assert employees == CompanyEmployees(employees=expected_employees)
