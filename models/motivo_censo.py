from app import db
import uuid

class Motivo_Censo(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    external_id = db.Column(db.String(60),default = str(uuid.uuid4()),nullable=False) 
    #Relacion entre motivo_censo con censo_persona
    #censo_persona_id = db.Column(db.Integer,db.ForeignKey("censo__persona.id"),nullable = False)
    #motivo_censo = db.relationship('Censo_Persona', backref=db.backref('motivos_censos', lazy=True))
    #Relacion de motivo_censo con catalogo
    #catalogo = db.relationship("Catalogo",backref = "motivo_censo",lazy = True)