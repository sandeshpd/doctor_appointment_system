from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from extension import db
# from models.appointment import Appointment

class Doctor(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  name: Mapped[str] = mapped_column(unique=True, nullable=False)
  contact: Mapped[str] = mapped_column(unique=True, nullable=False)
  speciality: Mapped[str] = mapped_column(nullable=False)
  email: Mapped[str] = mapped_column(unique=True, nullable=False)
  password: Mapped[str] = mapped_column(nullable=False)
  clinic_name: Mapped[str] = mapped_column(nullable=True)
  availability_hours: Mapped[str] = mapped_column(nullable=False)
  appointments: Mapped[List["Appointment"]] = relationship("Appointment", back_populates="doctor")

  def __repr__(self):
    return f"<Doctor {self.name}>"