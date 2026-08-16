def generate_recommendations(
    ats_score,
    missing_skills,
    resume_text
):

    recommendations = []

    resume_lower = resume_text.lower()

    # --------------------------------
    # 1. Missing Skills
    # --------------------------------

    if missing_skills:

        skills = ", ".join(missing_skills)

        recommendations.append(
            f"Consider highlighting relevant missing skills "
            f"such as: {skills}, if you genuinely have "
            f"experience with them."
        )

    else:

        recommendations.append(
            "Your resume contains all the skills "
            "identified in the job description."
        )

    # --------------------------------
    # 2. Resume Sections
    # --------------------------------

    sections = [
        "education",
        "experience",
        "skills",
        "projects"
    ]

    missing_sections = []

    for section in sections:

        if section not in resume_lower:
            missing_sections.append(section)

    if missing_sections:

        recommendations.append(
            "Consider adding these resume sections: "
            + ", ".join(missing_sections)
            + "."
        )

    # --------------------------------
    # 3. Resume Length
    # --------------------------------

    word_count = len(resume_text.split())

    if word_count < 150:

        recommendations.append(
            "Your resume appears quite short. "
            "Consider adding relevant projects, "
            "technical skills, achievements, or "
            "experience where appropriate."
        )

    # --------------------------------
    # 4. Contact Information
    # --------------------------------

    if "@" not in resume_text:

        recommendations.append(
            "Make sure your resume contains a "
            "professional email address."
        )

    # --------------------------------
    # 5. ATS Score
    # --------------------------------

    if ats_score >= 80:

        recommendations.append(
            "Your resume has a strong overall match "
            "with the job description."
        )

    elif ats_score >= 60:

        recommendations.append(
            "Your resume has a moderate match. "
            "Improving missing skills and tailoring "
            "your resume to the job description may "
            "increase the score."
        )

    else:

        recommendations.append(
            "Your resume has a low match with the job "
            "description. Focus on relevant skills, "
            "projects, experience, and keywords."
        )

    return recommendations