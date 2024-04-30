from models.persona import Persona
from app import db
import uuid
from models.rol import Rol
from controllers.utiles.error import Error


class PersonaControl:
    
    def listar(self):
        return Persona.query.all()
    def guardar_censado(self,data):
        persona = Persona()
        rol = Rol.query.filter_by(nombre ="Censado").first()
        if rol :           
            persona.nombre = data.get("nombre")
            persona.apellido = data.get("apellido")
            persona.edad = data.get("edad")
            persona.external_id = uuid.uuid4()
            persona.estado_civil = data.get("estado_civil")
            db.session.add(persona)
            db.session.commit()
            return persona.id
        else:
            return -1
    def guardar_censador(self,data):
        persona = Persona()
        rol = Rol.query.filter_by(nombre="Censador").first()
        if rol:
            persona.nombre = data.get("nombre")
            persona.apellido = data.get("apellido")
            persona.external_id = uuid.uuid4()
            persona.estado_civil = data.get("estado")
            db.session.add(persona)
            db.session.commit()
            return persona.id
        else:
            return -2
        
    def modificar_censado(self,external_id,data):
        persona = Persona.query.filter_by(external_id = external_id).first()
        if persona:
            persona.nombre = data.get("nombre")
            persona.apellido = data.get("apellido")
            persona.edad = data.get("edad")
            persona.estado_civil = data.get("estado_civil")
            persona.external_id = uuid.uuid4()
            db.session.add(persona)
            db.session.commit()
            return persona
        else:
            return -1
        
        
        
