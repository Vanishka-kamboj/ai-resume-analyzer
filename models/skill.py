from extensions import db


class Skill(db.Model):

    __tablename__ = "skills"

    id = db.Column(db.Integer, primary_key=True)

    skill_name = db.Column(
        db.String(100),
        nullable=False
    )

    category = db.Column(
        db.String(50),
        nullable=False
    )