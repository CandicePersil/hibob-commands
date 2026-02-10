from datetime import date, datetime
from pydantic import BaseModel, Field, field_validator


class Work(BaseModel):
    start_date: date = Field(alias="startDate")
    area: str = Field(alias="site")

    @field_validator("start_date", mode="before")
    def parse_start_date(cls, value: str):
        return datetime.strptime(value, "%Y-%m-%d").date()

class Employment(BaseModel):
    contract_type: str = Field(alias="type")

class Payroll(BaseModel):
    employment: Employment = Field()

class Root(BaseModel):
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="surname")
    email: str = Field()

class Employee(BaseModel):
    payroll: Payroll = Field()
    work: Work = Field()
    root: Root = Field()


class CompanyEmployees(BaseModel):
    employees: list[Employee]
