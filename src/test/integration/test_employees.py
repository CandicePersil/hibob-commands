from models.employees import CompanyEmployees, Employee, Work


def test_validate_employee_data() -> None:
    # GIVEN
    input = {
        "firstName": "Noemie",
        "surname": "Star",
        "work": {
            "startDate": "10/01/2026",
            "contractType": "permanent",
            "title": "Software engineer",
            "site": "Paris",
        },
    }

    # WHEN
    employee = Employee(**input)

    # THEN
    assert employee == Employee(
        firstName=input["firstName"],
        surname=input["surname"],
        work=Work(
            startDate=input["work"]["startDate"],
            contractType=input["work"]["contractType"],
            title=input["work"]["title"],
            site=input["work"]["site"],
        ),
    )


def test_validate_multiple_employees_date() -> None:
    # GIVEN
    input = {
        "firstName": "Noemie",
        "surname": "Star",
        "work": {
            "startDate": "10/01/2026",
            "contractType": "permanent",
            "title": "Software engineer",
            "site": "Paris",
        },
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
