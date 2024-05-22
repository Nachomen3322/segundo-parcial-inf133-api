from flask import Blueprint, request, jsonify
from models.task_model import Task
from views.task_view import render_task_list, render_task_detail
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
from utils.decorators import jwt_required, roles_required

task_bp = Blueprint("task", __name__)

@task_bp.route("/tasks", methods=["GET"])
@jwt_required
def get_tasks():
    tasks = Task.get_all()
    return jsonify(render_task_list(tasks))

@task_bp.route("/tasks/<int:id>", methods=["GET"])
@jwt_required
def get_task(id):
    task = Task.get_by_id(id)
    if task:
        return jsonify(render_task_detail(task))
    return jsonify({"error": "Task no encontrada"}), 404

@task_bp.route("/tasks", methods=["POST"])
@jwt_required
@roles_required(role=["admin"])
def create_task():
    data = request.json
    print(data)
    title = data.get("title")
    description = data.get("description")
    status = data.get("status")
    created_at = data.get("created_at")
    assigned_to = data.get("assigned_to")
    
    if not title or not description or not status or not create_task or assigned_to is None:
        return jsonify({"error": "Faltan datos "}), 400
    task = Task(title=title, description=description, status=status, created_at=created_at, assigned_to=assigned_to)
    task.save()
    
@task_bp.route("/tasks/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(role=["Admin"])
def update_task(id):
    task = Task.get_by_id(id)
    if not task:
        return jsonify({"error": "Task no encontrado"}), 404
    data =request.json
    title = data.get("title")
    description = data.get("description")
    status = data.get("status")
    created_at = data.get("created_at")
    assigned_to = data.get("assigned_to")
    
    task.update(title=title, description=description, status=status, created_at=created_at, assigned_to=assigned_to)
    return jsonify(render_task_detail(task))

@task_bp.route("/tasks/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(role=["admin"])
def delete_task(id):
    task = Task.get_by_id(id)
    
    if not task:
        return jsonify({"error": "Task no encontrado"}), 404
    task.delete()
    return "", 204