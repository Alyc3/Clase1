from app import db
import uuid


class Censo_Persona(db.Model):
    
    id = db.Column(db.Integer,primary_key =True)
    fecha = db.Column(db.Date)
    lat = db.Column(db.Numeric)
    long = db.Column(db.Numeric)
    motivo= db.Column(db.String(100))
    external_id = db.Column(db.String(60),default = str(uuid.uuid4()),nullable=False)


    #Relacion de censo_persona con persona
    #persona_id =  db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)
    #persona = db.relationship('Persona', back_populates='censo_persona')
    #Relacion de censo_persona con censo
    #censo_id = db.Column(db.Integer, db.ForeignKey("censo.id"),nullable = False)
    #Relacion de censo_persona con motivo_censo
    #motivos_censos = db.relationship("Motivo_Censo",back_populates = "censo_persona",lazy = True)