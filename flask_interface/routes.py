"""
Rutas y endpoints del servicio de usuarios
Define los endpoints REST para el manejo de usuarios en Agroweb
"""

from flask import Blueprint, request, jsonify
from flasgger import Swagger
from application.useCases.RegisterUserService import RegisterUserService
from application.useCases.GetUserIdService import GetUserIdService
from application.useCases.GetAllUsersService import GetAllUsersService
from application.useCases.GetUserEmailService import GetUserEmailService
from application.useCases.AuthenticationService import AuthenticationService
from Infrastructure.adapterUserRepo import AdapterUserRepo
from observability.MetricsDecorator import monitor_endpoint
import requests

# Crear blueprint para las rutas de usuarios
bp = Blueprint('usuarios', __name__)

# Inicialización de servicios y repositorio
adapterRepo = AdapterUserRepo()
register_service = RegisterUserService(adapterRepo)
getUsers = GetAllUsersService(adapterRepo)
getUserDoc = GetUserIdService(adapterRepo)
getUserEmail = GetUserEmailService(adapterRepo)
autenticateUser = AuthenticationService(adapterRepo)

@bp.route("/users/register", methods=["POST"])
@monitor_endpoint("register_user")
def register():
    """
    Endpoint para registrar un nuevo usuario
    Recibe datos JSON del usuario y los valida antes de registrar
    """
    data = request.get_json()
    try:
        print(f"Registrando usuario: {data}")
        new_user = register_service.execute(data)
        return jsonify({
            "mensaje": "Usuario registrado exitosamente",
            "usuario": new_user
        }), 201
    except ValueError as e:
        print(f"Error al registrar usuario: {str(e)}")
        return jsonify({"error": str(e)}), 400

@bp.route("/users/", methods=["GET"])
@monitor_endpoint("get_all_users")
def getAllUsers():
    """
    Endpoint para obtener un usuario por número de documento
    """
    try:
        users = getUsers.execute()
        return jsonify(users), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@bp.route("/users/getById/<document>", methods=["GET"])
@monitor_endpoint("get_user_by_id")
def getUserById(document):
    """
    Endpoint para obtener un usuario por número de documento
    """
    try:
        user = getUserDoc.execute(document)
        return jsonify({
            "message": "Usuario encontrado con éxito",
            "user": user
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@bp.route("/users/getByEmail/<email>", methods=["GET"])
@monitor_endpoint("get_user_by_email")
def getUserByEmail(email):
    """
    Endpoint para obtener un usuario por email
    """
    try:
        user = getUserEmail.execute(email)
        return jsonify({
            "message": "Usuario encontrado con éxito",
            "user": user
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@bp.route("/users/autenticate/", methods=["POST"])
@monitor_endpoint("authenticate_user")
def authUser():
    """
    Endpoint para autenticar un usuario
    Recibe email y contraseña encriptada, valida las credenciales
    """
    data = request.get_json() 
    email = data.get("email")
    password = data.get("hashPassword")
    
    try:
        validate = autenticateUser.execute(email, password)
        return jsonify({"message": "Ingreso exitoso"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 404
