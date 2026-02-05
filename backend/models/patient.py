from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from extension import db
# from models.appointment import Appointment

class Patient(db.Model):
  __tablename__ = "patient"

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  name: Mapped[str] = mapped_column(unique=True, nullable=False)
  contact: Mapped[str] = mapped_column(unique=True, nullable=False)
  sex: Mapped[str] = mapped_column(nullable=False)
  age: Mapped[str] = mapped_column(nullable=False)
  email: Mapped[str] = mapped_column(unique=True, nullable=False)
  password: Mapped[str] = mapped_column(nullable=False)
  
  appointments: Mapped[List["Appointment"]] = relationship("Appointment", back_populates="patient")

  def __init__(self, name, contact, sex, age, email, password):
    self.name = name
    self.contact = contact
    self.sex = sex
    self.age = age
    self.email = email
    self.password = password

  def __repr__(self):
    return f"<Patient {self.name}>"