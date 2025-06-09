from flask import Blueprint, request, jsonify
from application.useCases.RegisterUserService import RegisterUserService
from Infrastructure.adapterUserRepo import AdapterUserRepo

bp = Blueprint('usuarios', __name__)
adapterRepo = AdapterUserRepo()
register_service = RegisterUserService(adapterRepo)

@bp.route("/register/user", methods=["POST"])
def register():
    data = request.get_json()
    try:
        new_user = register_service.execute(data)
        return jsonify({"mensaje": "Usuario registrado exitosamente",
                        "usuario ":new_user}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400