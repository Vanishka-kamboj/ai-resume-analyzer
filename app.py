from flask import Flask , render_template, request
import os
from parser import extract_resume_text
from skills import extract_skills
from similarity import calculate_similarity
from ATS import calculate_ats
from recommendation import generate_recommendations

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

ALLOWED_EXTENSIONS = {"pdf", "docx"}

def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


@app.route("/analyze", methods=["POST"])
def analyze():
    

    resume_file = request.files["resume"]
    if not allowed_file(resume_file.filename):

        return "Please upload PDF or DOCX only."
    jd_text = request.form["jd"]

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        resume_file.filename
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
    ats_score = calculate_ats(
        jd_skills,
        resume_skills,
        similarity_score
    )
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
        color=color
    )

if __name__=="__main__":
    app.run(debug = True)