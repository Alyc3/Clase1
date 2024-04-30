from app import db
from models.estadoCivil import EstadoCivil
import uuid

class Persona(db.Model):
    #relation
    id = db.Column(db.Integer,primary_key =True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    edad = db.Column(db.Integer)
    estado_civil= db.Column(db.Enum(EstadoCivil),nullable=False)
    external_id = db.Column(db.String(60),default = str(uuid.uuid4()),nullable=False)

    #Relacion de uno a muchos con censo_persona
    #censo_persona =  db.relationship('Censo_Persona', back_populates='persona', lazy=True)

    #Relacion de uno a muchos con rol
    rol = db.relationship('Rol',uselist=False, back_populates='persona')
    #Relacion de uno a muchos con censo
    #censo = db.relationship("Censo",backref = "persona",lazy = True)
    #Relacion con cuenta
    cuenta = db.relationship('Cuenta', back_populates='persona', uselist=False)
    #Getters and setters
    @property
    def serialize(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad
            
        }

    

        

