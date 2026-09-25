from sqlalchemy import Column, Integer, String, Boolean, Table, ForeignKey
from sqlalchemy.orm import relationship

from  .database import Base


doctor_patient = Table(
    "doctor_patient",
    Base.metadata,
    Column(
        "doctor_id",
        Integer,
        ForeignKey("doctors.id"),
        primary_key=True
    ),
    Column(
        "patient_id",
        Integer,
        ForeignKey("patients.id"),
        primary_key=True
    )
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="doctor")


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)

    patients = relationship(
        "Patient",
        secondary=doctor_patient,
        back_populates="doctors"
    )


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    phone = Column(String, nullable=False)

    doctors = relationship(
        "Doctor",
        secondary=doctor_patient,
        back_populates="patients"
    )