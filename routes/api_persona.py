from flask import Blueprint, jsonify, make_response, request
# Importacion de los modelos de tablas de la base de datos
from controllers.personaControl import PersonaControl
from controllers.utiles.error import Error
api_persona = Blueprint('api__persona', __name__)
from flask_expects_json import expects_json
#API para persona
personaC = PersonaControl()


schema = {
    'type': 'object',
    'properties':{
        'nombre':{'type': 'string'},
        'apellido':{'type': 'string'},
        'edad':{'type': 'integer'},
        'estado_civi;':{'type': 'boolean'}
    },
    'required': ['nombre', 'apellido','edad','estado_civil']
}

schema_censador = {
    'type': 'object',
    'properties':{
        'nombres':{'type': 'string'},
        'apellido':{'type': 'string'},
        'fecha':{'type': 'string'},
        'estado':{'type': 'string'}
    },
    'required': ['nombres', 'apellido','fecha','estado']
}
@api_persona.route("/persona",methods =["GET"])
def listar():
    personas = [i.serialize() for i in personaC.listar()]
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": personas}),
        200
    )

@api_persona.route(("/persona/guardar/censado"), methods=["POST"])
@expects_json(schema)
def guardar_censado():
    data = request.get_json()
    id = personaC.guardar_censado(data)
    print(str(id))
    if (id >=0):
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": {"tag":"Datos Guardados"}}),
            200
        )
    else:
        return make_response(
            jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Error.error[str(id)]}}), 
        )

@api_persona.route("/persona/guardar/censador",methods =["POST"])
@expects_json(schema_censador)
def guardar_censador ():
    data = request.json
    id =personaC.guardar_censador(data)
    if (id >=0):
        return make_response(
        jsonify({"msg": "OK", "code": 200,"datos":[]}),
        200
    )
    else:
        return make_response(
        jsonify({"msg": "OK", "code": 400,"datos":{"error":Error.error[str(id)]}}),
        400
        )
    
@api_persona.route("/persona/modificar/censado/<external_id>",methods =["POST"])
@expects_json(schema)
def modificar_censado(external_id):
    data = request.get_json()
    id = personaC.modificar_censado(data,external_id)
    if (id >=0):
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": {"tag":"Datos Modificados"}}),
            200
        )
    else:
        return make_response(
            jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Error.error[str(id)]}}), 
        )




