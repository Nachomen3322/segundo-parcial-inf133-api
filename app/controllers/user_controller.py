from flask import Blueprint, request, jsonify
from models.user_model import User
from flask_jwt_extended import create_access_token
from utils.decorators import jwt_required, roles_required
from werkzeug.security import check_password_hash

user_bp = Blueprint("user", __name__)

user_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    if not name or not email or not password or not role:
        return jsonify({"error": "Se requieren datos"}), 400

    existing_user = User.find_by_name(name)
    if existing_user:
        return jsonify({"error": "El nombre de usuario ya está en uso"}), 400

    new_user = User(name, email, password, role)
    new_user.save()

    return jsonify({"message": "Usuario creado exitosamente"}), 201


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    user = User.find_by_name(name)
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(
            identity={"name": name, "roles": user.role}
        )
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401