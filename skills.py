def extract_skills(text):

    skill_list = [
        "python",
        "java",
        "sql",
        "flask",
        "git",
        "machine learning",
        "html",
        "css",
        "javascript",
        "Rest api",
        "docker",
        "c++",
        "c",
        "node.js",
        "react.js",
        "data science",
        "data structure",
        "algorithm"
    ]

    found_skills = []

    text = text.lower()

    for skill in skill_list:

        if skill in text:
            found_skills.append(skill)

    return found_skills