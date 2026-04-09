from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from models import ApplicationStatus


class ORMBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    login: str = Field(min_length=3, max_length=100)
    password_hash: str


class UserRead(ORMBase):
    id: int
    login: str


class ParticipationRequestCreate(BaseModel):
    contact_person_full_name: str
    child_full_name: str
    child_age: int = Field(ge=0, le=25)
    email: EmailStr
    phone_number: str
    child_hobbies: str
    comment: str | None = None


class ParticipationRequestRead(ORMBase):
    id: int
    contact_person_full_name: str
    child_full_name: str
    child_age: int
    email: EmailStr
    phone_number: str
    child_hobbies: str
    comment: str | None
    status: ApplicationStatus
    created_at: datetime
    updated_at: datetime


class QuestionCreate(BaseModel):
    full_name: str
    email: EmailStr


class QuestionRead(ORMBase):
    id: int
    full_name: str
    email: EmailStr
    created_at: datetime


class CampShiftCreate(BaseModel):
    start_date: date
    end_date: date
    location_name: str
    location_latitude: str
    location_longitude: str
    participants_limit: int = Field(gt=0)
    participation_price: Decimal = Field(gt=0)


class CampShiftRead(ORMBase):
    id: int
    start_date: date
    end_date: date
    location_name: str
    location_latitude: str
    location_longitude: str
    participants_limit: int
    participation_price: Decimal


class NewsCreate(BaseModel):
    title: str
    html_content: str


class NewsRead(ORMBase):
    id: int
    title: str
    html_content: str
    created_at: datetime


class CuratorCreate(BaseModel):
    full_name: str
    direction: str
    photo_url: str
    description: str


class CuratorRead(ORMBase):
    id: int
    full_name: str
    direction: str
    photo_url: str
    description: str