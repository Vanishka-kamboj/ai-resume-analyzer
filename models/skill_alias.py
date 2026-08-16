from extensions import db


class SkillAlias(db.Model):

    __tablename__ = "skill_aliases"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    alias = db.Column(
        db.String(100),
        nullable=False
    )

    skill_id = db.Column(
        db.Integer,
        db.ForeignKey("skills.id"),
        nullable=False
    )

    skill = db.relationship(
        "Skill",
        backref="aliases"
    )