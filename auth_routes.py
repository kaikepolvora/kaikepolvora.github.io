from flask import Blueprint, request, jsonify
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.models.user_models import db, User
# Para tokens JWT, precisaremos de Flask-JWT-Extended
# from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role", "journalist") # Default role

    if not username or not email or not password:
        return jsonify({"error": "Missing username, email, or password"}), 400

    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({"error": "Username or email already exists"}), 409

    new_user = User(username=username, email=email, role=role)
    new_user.set_password(password)
    
    try:
        db.session.add(new_user)
        db.session.commit()
        # access_token = create_access_token(identity=new_user.id) # Se usar JWT
        return jsonify({
            "message": f"User {username} registered successfully!",
            # "access_token": access_token # Se usar JWT
            "user": {"id": new_user.id, "username": new_user.username, "email": new_user.email, "role": new_user.role}
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@auth_bp.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        # access_token = create_access_token(identity=user.id) # Se usar JWT
        return jsonify({
            "message": f"User {username} logged in successfully!",
            # "access_token": access_token, # Se usar JWT
             "user": {"id": user.id, "username": user.username, "email": user.email, "role": user.role}
        }), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

# Adicionar rota de logout se estiver usando sessões ou JWT com blocklist
# @auth_bp.route("/logout", methods=["POST"])
# @jwt_required()
# def logout_user():
#     # Implementar lógica de logout, por exemplo, adicionar token à blocklist se usar JWT
#     return jsonify({"message": "Successfully logged out"}), 200

