from flask import Blueprint, request, jsonify
from application.useCases.RegisterUserService import RegisterUserService
from application.useCases.GetUserIdService import GetUserIdService
from application.useCases.GetUserEmailService import GetUserEmailService
from application.useCases.AuthenticationService import AuthenticationService
from Infrastructure.adapterUserRepo import AdapterUserRepo

bp = Blueprint('usuarios', __name__)
adapterRepo = AdapterUserRepo()
register_service = RegisterUserService(adapterRepo)
getUserDoc= GetUserIdService(adapterRepo)
getUserEmail= GetUserEmailService(adapterRepo)
autenticateUser= AuthenticationService(adapterRepo)

@bp.route("/users/register", methods=["POST"])
def register():
    data = request.get_json()
    try:
        print(data)
        new_user = register_service.execute(data)
        return jsonify({"mensaje": "Usuario registrado exitosamente",
                        "usuario ":new_user}), 201
    except ValueError as e:
        print(str(e))
        return jsonify({"error": str(e)}), 400

@bp.route("/users/getById/<document>",methods=["GET"])
def getUserById(document):
    try:
        user=getUserDoc.execute(document)
        return jsonify({"message":"Usuario encontrado con exito",
                        "user":user}),200
    except ValueError as e:
        return jsonify({"error":str(e)}),404
@bp.route("/users/getByEmail/<email>",methods=["GET"])
def getUserByEmail(email):
    try:
        user=getUserEmail.execute(email)
        return jsonify ({"message":"Usuario encontrado con exito",
                         "user":user})
    except ValueError as e:
        return jsonify({"error":str(e)}),404

@bp.route("/users/autenticate/",methods=["POST"])
def authUser():
    data = request.get_json() 
    email = data.get("email")
    password = data.get("hashPassword")
    try:
        validate=autenticateUser.execute(email,password)
        return jsonify({"message":"Ingreso Exitoso"}),200
    except ValueError as e:
        return jsonify({"error":str(e)}),401

    
    