from app import db
import uuid

class Cuenta(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    usuario = db.Column(db.String(100),unique= True)
    password = db.Column(db.String(100))
    external_id = db.Column(db.String(60),default = str(uuid.uuid4()),nullable=False)

    #relacion
    #=db.Column(db.Integer,db.unique = True)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id'),nullable = False,unique = True)
    persona = db.relationship('Persona', back_populates='cuenta')