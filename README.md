# 📄 AI Resume Analyzer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask" />
  <img src="https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql" />
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Scikit--Learn-NLP-orange?style=for-the-badge&logo=scikitlearn" />
  <img src="https://img.shields.io/badge/HTML5-Frontend-E34F26?style=for-the-badge&logo=html5" />
  <img src="https://img.shields.io/badge/CSS3-Styling-1572B6?style=for-the-badge&logo=css3" />
  <img src="https://img.shields.io/badge/Bootstrap-UI-7952B3?style=for-the-badge&logo=bootstrap" />
</p>

<p align="center">
  A Flask-based Resume Analyzer that evaluates a resume against a Job Description,
  calculates an ATS-style match score, identifies matching and missing skills,
  and provides resume improvement recommendations.
</p>

---

## 🚀 Overview

The **AI Resume Analyzer** is a web application built using Python, Flask, PostgreSQL, and NLP techniques.

The application allows users to upload a resume in **PDF or DOCX format** and provide a Job Description (JD). It then analyzes the resume and generates an ATS-style score based on:

- Skill matching
- Resume–Job Description similarity
- Resume quality indicators

The application also identifies skills required by the Job Description that are missing from the resume and provides recommendations for improvement.

---

## ✨ Features

- 📄 Upload Resume in PDF or DOCX format
- 📝 Enter a Job Description
- 🔍 Automatic Resume Text Extraction
- 🧠 Database-driven Skill Extraction
- 🔗 Skill Alias / Skill Normalization
- 📊 ATS-style Resume Score
- 📈 Resume–Job Description Similarity Score
- ✅ Matched Skills Detection
- ❌ Missing Skills Detection
- 💡 Resume Improvement Recommendations
- 🗄️ PostgreSQL Database Integration
- 🌐 Flask Web Application
- 📱 Responsive UI using Bootstrap

---

## 🛠️ Tech Stack

### Frontend

- HTML5
- CSS3
- Bootstrap
- JavaScript

### Backend

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy

### Database

- PostgreSQL

### NLP / Machine Learning

- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- Regular Expressions for skill matching

### Resume Processing

- PyPDF2 / pdfplumber
- python-docx

### Development Tools

- Git
- GitHub
- VS Code

---

# 🏗️ Project Architecture

```text
                    ┌──────────────────────┐
                    │       User           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Flask Web Interface │
                    └──────────┬───────────┘
                               │
                    Resume + Job Description
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Resume Text Parser  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Skill Extraction   │
                    │ + Skill Aliases      │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴───────────┐
                    ▼                      ▼
             Resume Skills            JD Skills
                    │                      │
                    └──────────┬───────────┘
                               ▼
                    ┌──────────────────────┐
                    │   Skill Matching     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ TF-IDF + Cosine      │
                    │ Similarity            │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    ATS Scoring       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Recommendations      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Result Dashboard  │
                    └──────────────────────┘
# 👩‍💻 Developer

**Vanishka Kamboj**

- GitHub: [Vanishka-kamboj](https://github.com/Vanishka-kamboj)
- LinkedIn: [Vanishka Kamboj](https://www.linkedin.com/in/vanishka-kamboj/)

---

