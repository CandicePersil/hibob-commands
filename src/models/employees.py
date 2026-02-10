from datetime import date, datetime
from pydantic import BaseModel, Field, field_validator, model_serializer, SerializerFunctionWrapHandler


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

    @model_serializer(mode="wrap")
    def serialize_model(self, handler: SerializerFunctionWrapHandler) -> dict[str, object]:
        return {
            "email": self.root.email,
            "first_name": self.root.first_name,
            "last_name": self.root.last_name,
            "start_date": self.work.start_date.strftime("%d/%m/%Y"),
            "end_date": None,
            "contract_type": self.payroll.employment.contract_type,
            "date_of_birth": None,
            "phone_number": None,
            "professional_category": None,
            "subsidy_level": None,
            "area": self.work.area,
        }

class CompanyEmployees(BaseModel):
    employees: list[Employee]
