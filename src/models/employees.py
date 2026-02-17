from datetime import date, datetime
from pydantic import (
    BaseModel,
    Field,
    field_validator,
    field_serializer,
    model_serializer,
    SerializerFunctionWrapHandler,
)


class Work(BaseModel):
    start_date: date = Field(alias="startDate")
    area: str = Field(alias="site")

    @field_validator("start_date", mode="before")
    @classmethod
    def parse_start_date(cls, value: str) -> date:
        return datetime.strptime(value, "%Y-%m-%d").date()

    @field_serializer("start_date", mode="plain")
    def serialize_start_date(self, value: date) -> str:
        return value.strftime("%d/%m/%Y")


class Employment(BaseModel):
    contract_type: str = Field(alias="type")


class Payroll(BaseModel):
    employment: Employment = Field()


class Custom(BaseModel):
    first_name: str = Field(alias="field_1725354995510")
    last_name: str = Field(alias="field_1725355007237")


class Employee(BaseModel):
    payroll: Payroll = Field()
    work: Work = Field()
    custom: Custom = Field()
    email: str = Field()

    @model_serializer(mode="wrap")
    def serialize_model(
        self, handler: SerializerFunctionWrapHandler
    ) -> dict[str, object]:
        serialized = handler(self)
        return {
            "email": self.email,
            "first_name": self.custom.first_name,
            "last_name": self.custom.last_name,
            "start_date": serialized["work"]["start_date"],
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
