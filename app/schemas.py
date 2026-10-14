
import re
from datetime import date

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    field_validator,
    model_validator,
)


class StudentBase(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(min_length=2, max_length=100)
    date_of_birth: date

    email: EmailStr | None = None
    phone: str | None = Field(default=None, max_length=20)

    course: str | None = Field(default=None, max_length=100)
    address: str | None = Field(default=None, max_length=250)
    enrollment_date: date | None = None

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if len(value.strip()) < 2:
            raise ValueError("Name must have at least 2 characters")
        return value

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value):
        if value is None:
            return None

        value = value.strip()

        if not value:
            return None

        if not re.fullmatch(r"[0-9+() -]{7,20}", value):
            raise ValueError("Invalid phone number format")

        return value

    @model_validator(mode="after")
    def validate_dates_and_contact(self):
        today = date.today()

        if self.date_of_birth > today:
            raise ValueError("Date of birth cannot be in the future")

        if self.enrollment_date and self.enrollment_date > today:
            raise ValueError("Enrollment date cannot be in the future")

        if not self.email and not self.phone:
            raise ValueError("Provide an email or phone number")

        return self


class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentBase):
    pass


class StudentResponse(StudentBase):
    student_id: int
    created_at: str
    updated_at: str
