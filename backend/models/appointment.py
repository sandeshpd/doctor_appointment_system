from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from extension import db
# from models.patient import Patient
# from models.doctor import Doctor

class Appointment(db.Model):
  __tablename__ = "appointment"
  
  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  patient_id: Mapped[int] = mapped_column(ForeignKey("patient.id"), nullable=False)
  doctor_id: Mapped[int] = mapped_column(ForeignKey("doctor.id"), nullable=False)
  date: Mapped[str] = mapped_column(nullable=False)
  time: Mapped[str] = mapped_column(nullable=False)
  status: Mapped[str] = mapped_column(nullable=False)

  patient: Mapped["Patient"] = relationship("Patient", back_populates="appointments")
  doctor: Mapped["Doctor"] = relationship("Doctor", back_populates="appointments")