from datetime import date, datetime
from pydantic import BaseModel, Field, field_validator


class Work(BaseModel):
    start_date: date = Field(alias="startDate")
    contract_type: str = Field(alias="contractType")  # full time
    title: str = Field(alias="title")
    site: str = Field(alias="site")

    @field_validator("start_date", mode="before")
    def parse_start_date(cls, value: str):
        return datetime.strptime(value, "%d/%m/%Y").date()


class Employee(BaseModel):
    name: str = Field(alias="firstName")
    surname: str = Field(alias="surname")
    work: Work = Field(alias="work")


class CompanyEmployees(BaseModel):
    employees: list[Employee]
