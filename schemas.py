from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str = "doctor"


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class DoctorCreate(BaseModel):
    name: str
    specialization: str
    email: EmailStr


class DoctorUpdate(BaseModel):
    name: Optional[str] = None
    specialization: Optional[str] = None
    email: Optional[EmailStr] = None


class DoctorResponse(BaseModel):
    id: int
    name: str
    specialization: str
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True


class PatientCreate(BaseModel):
    name: str
    age: int = Field(gt=0)
    phone: str = Field(
        pattern=r"^\d{10,15}$"
    )


class PatientResponse(BaseModel):
    id: int
    name: str
    age: int
    phone: str

    class Config:
        from_attributes = True