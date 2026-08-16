def calculate_ats(jd_skills, resume_skills, similarity_score, resume_text):

    # -----------------------------
    # 1. Skill Match Score (50%)
    # -----------------------------

    jd_skill_set = set(jd_skills)
    resume_skill_set = set(resume_skills)

    matched_skills = jd_skill_set & resume_skill_set

    if not jd_skill_set:
        skill_match_percentage = 0
    else:
        skill_match_percentage = (
            len(matched_skills) / len(jd_skill_set)
        ) * 100

    skill_score = skill_match_percentage * 0.50


    # -----------------------------
    # 2. Similarity Score (30%)
    # -----------------------------

    similarity_score_component = similarity_score * 0.30


    # -----------------------------
    # 3. Resume Quality Score (20%)
    # -----------------------------

    quality_score = calculate_resume_quality(resume_text)


    # -----------------------------
    # Final ATS Score
    # -----------------------------

    ats_score = (
    skill_score
    + similarity_score_component
    + quality_score
)

    return {
        "total": round(ats_score, 2),
        "skill_score": round(skill_score, 2),
        "similarity_score": round(similarity_score_component, 2),
        "quality_score": round(quality_score, 2)
    }
def calculate_resume_quality(resume_text):

    score = 0

    resume_lower = resume_text.lower()

    # -----------------------------
    # 1. Important Resume Sections
    # -----------------------------

    sections = {
        "education": 3,
        "experience": 3,
        "skills": 3,
        "projects": 3
    }

    for section, points in sections.items():

        if section in resume_lower:
            score += points

    # -----------------------------
    # 2. Resume Length
    # -----------------------------

    word_count = len(resume_text.split())

    if word_count >= 300:
        score += 5

    elif word_count >= 150:
        score += 3

    # -----------------------------
    # 3. Contact Information
    # -----------------------------

    if "@" in resume_text:
        score += 3

    return min(score, 20)