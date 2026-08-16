from flask import Flask , render_template, request
import os
from dotenv import load_dotenv
from extensions import db
from werkzeug.utils import secure_filename
from uuid import uuid4
from config import (
    UPLOAD_FOLDER,
    ALLOWED_EXTENSIONS,
    MAX_CONTENT_LENGTH
)
from parser import extract_resume_text
from skills import extract_skills
from similarity import calculate_similarity
from ATS import calculate_ats
from recommendation import generate_recommendations
load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

@app.route("/")
def home():
    return render_template("index.html")


def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


@app.route("/analyze", methods=["POST"])
def analyze():
    resume_file = request.files.get("resume")
    jd_text = request.form.get("jd", "").strip()

        # Check if resume was uploaded
    if not resume_file or resume_file.filename == "":
         return "Please upload your resume."

        # Check file type
    if not allowed_file(resume_file.filename):
        return "Please upload PDF or DOCX only."

        # Check job description
    if not jd_text:
        return "Please enter a job description."
    


    filename = secure_filename(resume_file.filename)

    unique_filename = f"{uuid4()}_{filename}"

    filepath = os.path.join(

        app.config["UPLOAD_FOLDER"],
        unique_filename
)

    resume_file.save(filepath)

    #Extract resume text FIRST
    resume_text = extract_resume_text(filepath)
    

    #Extract skills
    jd_skills = extract_skills(jd_text)

    resume_skills = extract_skills(resume_text)

    

    #Calculate similarity
    similarity_score = calculate_similarity(
        resume_text,
        jd_text
    )

    #Find matched and missing skills
    matched_skills = list(
        set(jd_skills) & set(resume_skills)
    )

    missing_skills = list(
        set(jd_skills) - set(resume_skills)
    )

    #Calculate ATS score
    ats_result = calculate_ats(
    jd_skills,
    resume_skills,
    similarity_score,
    resume_text
)
    ats_score = ats_result["total"]
    if ats_score >= 80:

        color = "success"      # Green
    elif ats_score >= 60:
        color = "warning"      # Yellow
    else:
        color = "danger"       # Red    

    #Generate recommendations
    recommendations = generate_recommendations(
        ats_score,
        missing_skills,
        resume_text
    )

    return render_template(
        "result.html",
        ats=ats_score,
        similarity=similarity_score,
        matched=matched_skills,
        missing=missing_skills,
        recommendations=recommendations,
        color=color,
        skill_score=ats_result["skill_score"],
        similarity_score_component=ats_result["similarity_score"],
        quality_score=ats_result["quality_score"]
    )

if __name__=="__main__":
    app.run(debug = True)