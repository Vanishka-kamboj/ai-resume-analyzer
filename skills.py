import re

from models.skill import Skill
from models.skill_alias import SkillAlias


def extract_skills(text):

    found_skills = []

    text = text.lower()

    # Get all canonical skills
    skills = Skill.query.all()

    # Get all aliases
    aliases = SkillAlias.query.all()

    # --------------------------------
    # 1. Check canonical skills
    # --------------------------------

    for skill in skills:

        skill_name = skill.skill_name.lower()

        if skill_name == "c":

            pattern = r"(?<![a-z0-9+#])c(?![a-z0-9+#])"

        else:

            pattern = (
                r"(?<!\w)"
                + re.escape(skill_name)
                + r"(?!\w)"
            )

        if re.search(pattern, text):

            found_skills.append(
                skill.skill_name
            )

    # --------------------------------
    # 2. Check aliases
    # --------------------------------

    for alias in aliases:

        alias_name = alias.alias.lower()

        pattern = (
            r"(?<!\w)"
            + re.escape(alias_name)
            + r"(?!\w)"
        )

        if re.search(pattern, text):

            if alias.skill:

                found_skills.append(
                    alias.skill.skill_name
                )

    # --------------------------------
    # 3. Remove duplicates
    # --------------------------------

    return list(set(found_skills))