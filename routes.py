from flask import Blueprint, jsonify, request
from .models import Application
from . import db

api = Blueprint("api", __name__)

@api.route("/applications", methods=["GET"])
def get_applications():
    applications = Application.query.all()

    result = []
    for application in applications:
        result.append({
            "id": application.id,
            "user_id": application.user_id,
            "job_id": application.job_id,
            "status": application.status
        })

    return jsonify(result)

@api.route("/applications", methods=["POST"])
def create_application():
    data = request.get_json()

    application = Application(
        user_id=data["user_id"],
        job_id=data["job_id"],
        status=data["status"]
    )

    db.session.add(application)
    db.session.commit()

    return jsonify({
        "id": application.id,
        "user_id": application.user_id,
        "job_id": application.job_id,
        "status": application.status
    }), 201

@api.route("/applications/<int:application_id>", methods=["PUT"])
def update_application(application_id):
    application = db.session.get(Application, application_id)

    if application is None:
        return jsonify({"error": "Application not found"}), 404

    data = request.get_json()

    application.status = data["status"]

    db.session.commit()

    return jsonify({
        "id": application.id,
        "user_id": application.user_id,
        "job_id": application.job_id,
        "status": application.status
    }), 200

@api.route("/applications/<int:application_id>", methods=["DELETE"])
def delete_application(application_id):
    application = db.session.get(Application, application_id)

    if application is None:
        return jsonify({"error": "Application not found"}), 404

    db.session.delete(application)
    db.session.commit()

    return jsonify({
        "message": "Application deleted successfully"
    }), 200