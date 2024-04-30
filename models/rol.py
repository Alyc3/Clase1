from app import db
import uuid

class Rol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(100))
    estado = db.Column(db.Boolean, default=True)
    external_id = db.Column(db.String(60),default = str(uuid.uuid4()),nullable=False)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), unique=True)
    persona = db.relationship("Persona", back_populates="rol")

    @property
    #si no se le pone property lo toma como una funcion
    #las propiedades funcionan sin la llamada de un metodo
    def serialize(self):
        return{
            'nombre': self.nombre,
            'descripcion':self.descripcion,
            'external_id': self.external_id,
            'estado': 1 if self.estado else 0
        }
