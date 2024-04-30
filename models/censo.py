from app import db
import uuid

class Censo(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    estado =db.Column(db.Boolean, default =True)
    fecha_inicio = db.Column(db.Date)
    fecha_final = db.Column(db.Date)
    motivo_censo = db.Column(db.String(100))
    external_id = db.Column(db.String(60),default = str(uuid.uuid4()),nullable=False)