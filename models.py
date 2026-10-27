
from . import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


class Profile(db.Model):
    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"),
        unique=True, nullable=False
    )
    phone = db.Column(db.String(20))
    location = db.Column(db.String(100))
    years_experience = db.Column(db.Integer)


class Company(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(100))
    website = db.Column(db.String(255))


class Job(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(
        db.Integer, db.ForeignKey("companies.id"),
        nullable=False
    )
    title = db.Column(db.String(150), nullable=False)
    salary = db.Column(db.Integer)
    location = db.Column(db.String(100))


class Application(db.Model):
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"),
        nullable=False
    )
    job_id = db.Column(
        db.Integer, db.ForeignKey("jobs.id"),
        nullable=False
    )
    status = db.Column(db.String(50), nullable=False, index=True)
    applied_date = db.Column(db.Date)


class Skill(db.Model):
    __tablename__ = "skills"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)


class JobSkill(db.Model):
    __tablename__ = "job_skills"

    job_id = db.Column(
        db.Integer,
        db.ForeignKey("jobs.id"),
        primary_key=True
    )
    skill_id = db.Column(
        db.Integer,
        db.ForeignKey("skills.id"),
        primary_key=True
    )
