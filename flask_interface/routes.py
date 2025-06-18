from flask import Blueprint, request, jsonify
from flasgger import Swagger
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
      
    """
    Register a new user
    ---
    tags:
      - Users
    description: Register a new user.
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            firstName:
              type: string
            middleName:
              type: string
            surName1:
              type: string
            surName2:
              type: string
            bornDate:
              type: string
            department:
              type: string
            municipality:
              type: string
            phoneNumber:
              type: string
            typeDocument:
              type: string
            numberDocument:
              type: string
            trail:
              type: string
            username:
              type: string
            email:
              type: string
            hashPassword:
              type: string
          required:
            - firstName
            - middleName
            - surName1
            - bornDate
            - department
            - municipality
            - phoneNumber
            - typeDocument
            - numberDocument
            - username  
            - email
            - hashPassword
    responses:
      201:
        description: Usuario registrado exitosamente
        schema:
          type: object
          properties:
            mensaje:
              type: string
            usuario:
              type: object
      400:
        description: Error en los datos enviados
    """

    data = request.get_json()
    try:
        print(data)
        new_user = register_service.execute(data)
        return jsonify({"mensaje": "Usuario registrado exitosamente",
                        "usuario ":new_user}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/users/getById/<document>",methods=["GET"])
def getUserById(document):



    """
    Get user by document ID
    ---
    tags:
      - Users
    description: Get user by document ID.
    parameters:
      - in: path
        name: document
        type: string
        required: true
        description: User document ID
    responses:
      200:
        description: Usuario encontrado con exito
        schema:
          type: object
          properties:
            message:
              type: string
            user:
              type: object
      404:
        description: Usuario no encontrado
    """

    try:
        user=getUserDoc.execute(document)
        return jsonify({"message":"Usuario encontrado con exito",
                        "user":user}),200
    except ValueError as e:
        return jsonify({"error":str(e)}),404
    


@bp.route("/users/getByEmail/<email>",methods=["GET"])
def getUserByEmail(email):

    """
    Get user by email
    ---
    tags:
      - Users
    description: Get user by email.
    parameters:
      - in: path
        name: email
        type: string
        required: true
        description: User email
    responses:
      200:
        description: Usuario encontrado con exito
        schema:
          type: object
          properties:
            message:
              type: string
            user:
              type: object
      404:
        description: Usuario no encontrado
    """

    try:
        user=getUserEmail.execute(email)
        return jsonify ({"message":"Usuario encontrado con exito",
                         "user":user})
    except ValueError as e:
        return jsonify({"error":str(e)}),404

@bp.route("/users/autenticate/",methods=["POST"])
def authUser():

    """
    Authenticate user
    ---
    tags:
      - Users
    description: Authenticate user by email and password.
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
            hashPassword:
              type: string
          required:
            - email
            - hashPassword
    responses:
      200:
        description: Ingreso Exitoso
        schema:
          type: object
          properties:
            message:
              type: string
      401:
        description: Credenciales inválidas
    """

    data = request.get_json() 
    email = data.get("email")
    password = data.get("hashPassword")
    try:
        validate=autenticateUser.execute(email,password)
        return jsonify({"message":"Ingreso Exitoso"}),200
    except ValueError as e:
        return jsonify({"error":str(e)}),401

    
    