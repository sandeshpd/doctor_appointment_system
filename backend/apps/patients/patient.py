from flask import Blueprint, request, jsonify
from models.patient import Patient
from extension import db

patientRouter = Blueprint("app", __name__)

# Fetch a list of all patients in the database
@patientRouter.route("/api/patients/", methods=["GET"])
def fetchAllPatients():
  patients = Patient.query.all()
  patients_list = [
        {
            "id": p.id,
            "name": p.name,
            "contact": p.contact,
            "sex": p.sex,
            "age": p.age,
            "email": p.email
        }
        for p in patients
    ]
  
  return jsonify(patients_list)

# Fetch a single patient in the database associated with id
@patientRouter.route("/api/patients/<int:id>", methods=["GET"])
def fetchSinglePatient(id):
  try:
    patient = Patient.query.get(id)
    if patient:
      patient_data = {
        "id": patient.id,
        "name": patient.name,
        "contact": patient.contact,
        "sex": patient.sex,
        "age": patient.age,
        "email": patient.email
      }
      return jsonify(patient_data)
    else:
      return jsonify({"error": "Patient record not found"}), 404
  except Exception as e:
    return jsonify({"error": f"Something went wrong: {e}"}), 500    

# Stores patient record in the database
@patientRouter.route("/api/patients/", methods=["POST"])
def storePatient():
  try:
    new_patient = Patient(
      name = request.json.get("name"),
      contact = request.json.get("contact"),
      sex = request.json.get("sex"),
      age = request.json.get("age"),
      email = request.json.get("email"),
      password = request.json.get("password"),
    )

    db.session.add(new_patient)
    db.session.commit()

    return {"message": "Patient record successfully created."}
  except Exception as e:
    return {"error": f"Something went wrong: {e}"}

# TODO: Remaining operations like Update, Delete