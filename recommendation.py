def generate_recommendations(
    ats_score,
    missing_skills,
    resume_text
):

    recommendations = []

    for skill in missing_skills:

        recommendations.append(
            f"Add projects or experience related to {skill}."
        )
    if ats_score < 60:
        recommendations.append(
            "Increase keyword coverage from the job description."
        )
    if ats_score > 75:
      recommendations.append("Your resume is moderately aligned. Add more relevant skills and keywords.")
    

    return recommendations