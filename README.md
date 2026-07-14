# 📄 AI Resume Analyzer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask" />
  <img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikitlearn" />
  <img src="https://img.shields.io/badge/HTML5-Frontend-E34F26?style=for-the-badge&logo=html5" />
  <img src="https://img.shields.io/badge/CSS3-Styling-1572B6?style=for-the-badge&logo=css3" />
  <img src="https://img.shields.io/badge/JavaScript-Interactive-F7DF1E?style=for-the-badge&logo=javascript" />
</p>

<p align="center">
An AI-powered Resume Analyzer that evaluates resumes against a Job Description (JD), calculates an ATS Match Score, identifies missing skills, and provides actionable suggestions to improve job application success.
</p>

---

## 🚀 Overview

The **AI Resume Analyzer** is a Flask-based web application designed to help job seekers optimize their resumes for Applicant Tracking Systems (ATS).

Users can upload their resume in **PDF** or **DOCX** format, paste a job description, and instantly receive:

- 📊 ATS Match Score
- ✅ Matching Skills
- ❌ Missing Skills
- 💡 Resume Improvement Suggestions

The project leverages **Natural Language Processing (NLP)** techniques such as **TF-IDF Vectorization** and **Cosine Similarity** to measure how closely a resume aligns with a given job description.

---

# ✨ Features

- 📄 Upload Resume (PDF & DOCX)
- 📝 Paste Any Job Description
- 🔍 Automatic Resume Text Extraction
- 📊 ATS Compatibility Score
- 🤖 Skill Matching Analysis
- ❌ Missing Skills Detection
- 💡 Resume Improvement Suggestions
- ⚡ Fast and User-Friendly Interface

---

# 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Flask (Python)

### Machine Learning / NLP
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

### Libraries
- PyPDF2 / pdfplumber
- python-docx
- NumPy
- Scikit-learn

---

# 📂 Project Structure

```
AI-Resume-Analyzer/
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│
├── templates/
│   ├── index.html
│   ├── result.html
│
├── uploads/
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

# ⚙️ How It Works

### Step 1
Upload your resume in PDF or DOCX format.

⬇️

### Step 2
Paste the Job Description.

⬇️

### Step 3
The application extracts text from your resume.

⬇️

### Step 4
Resume and Job Description are converted into TF-IDF vectors.

⬇️

### Step 5
Cosine Similarity is calculated to determine the ATS Match Score.

⬇️

### Step 6
The application displays:

- ATS Match Score
- Matching Skills
- Missing Skills
- Resume Suggestions

---

# 🧠 Workflow

```
Resume
   │
   ▼
Text Extraction
   │
   ▼
Text Cleaning
   │
   ▼
TF-IDF Vectorization
   │
   ▼
Cosine Similarity
   │
   ▼
ATS Match Score
   │
   ▼
Missing Skills + Suggestions
```

---

# 📊 Example Output

```
ATS Match Score : 84%

✔ Matching Skills
Python
SQL
Machine Learning
Data Analysis

❌ Missing Skills
AWS
Docker
Git

💡 Suggestions
• Add missing technical keywords.
• Include measurable project outcomes.
• Improve formatting for ATS compatibility.
```

---



# 💻 Installation

Clone the repository

```bash
git clone https://github.com/Vanishka-kamboj/AI-Resume-Analyzer.git
```

Move into the project folder

```bash
cd AI-Resume-Analyzer
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000/
```

---

# 🎯 Skills Demonstrated

- Python Programming
- Flask Web Development
- Machine Learning
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Cosine Similarity
- Resume Parsing
- PDF & DOCX Processing
- Frontend Development
- Git & GitHub

---

# 🔮 Future Enhancements

- 🤖 LLM-powered Resume Feedback
- 📈 Resume Ranking System
- 📋 Cover Letter Generator
- 🌐 Multi-language Resume Support
- ☁️ Cloud Deployment
- 📊 Resume Analytics Dashboard
- 🎨 Multiple Resume Templates

---

# 🤝 Contributing

Contributions are welcome!

Feel free to fork this repository, create a new branch, and submit a Pull Request.

---

# 👩‍💻 Developer

**Vanishka**

GitHub: [https://github.com/Vanishka-kamboj](https://github.com/Vanishka-kamboj)

LinkedIn:[ https://linkedin.com/in/your-linkedin-url](https://www.linkedin.com/in/vanishka-kamboj/)

---

