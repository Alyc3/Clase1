from flask import Blueprint, jsonify, make_response, request
# Importacion de los modelos de tablas de la base de datos
from controllers import personaControl
from models.rol import Rol
from models.censo import Censo
from models.catalogo import Catalogo
from models.censo_persona import Censo_Persona
from models.cuenta import Cuenta
from models.motivo_censo import Motivo_Censo

api = Blueprint('api', __name__)
#API para persona

@api.route("/")
def home ():
    return make_response(
        jsonify({"msg": "OK", "code": 200}),
        200
    )
