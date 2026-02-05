from flask import Flask
from extension import db
from models import appointment, doctor, patient
from apps.doctors import doctor
from apps.patients import patient
from dotenv import load_dotenv
import os

load_dotenv()
DB_URL = os.getenv("DATABASE_URL")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SQLALCHEMY_ECHO"] = True

# Initialize the database 
db.init_app(app)

# Register blueprints
app.register_blueprint(patient.patientRouter)

# We create the table here
with app.app_context():
  print("Creating tables...")
  db.create_all()
  db.session.commit()
  print("Tables created!")

@app.route("/")
def index():
  return "Index Page..."

if __name__=="__main__":
  app.run(debug=True)