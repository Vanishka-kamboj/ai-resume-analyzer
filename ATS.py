def calculate_ats(
    jd_skills,
    resume_skills,
    similarity_score
):

    matched = set(jd_skills) & set(resume_skills)

    skill_score = (
        len(matched) /
        len(jd_skills)
    ) * 100

    ats_score = (
        0.7 * skill_score +
        0.3 * similarity_score
    )

    return ats_score