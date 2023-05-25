from app import db
from datetime import datetime
from sqlalchemy import DateTime, Numeric

class REGION(db.Model):
    __tablename__ = 'REGION'
    ID_REGION = db.Column(db.Integer, primary_key=True)
    NOMBRE_REG = db.Column(db.String(80), nullable=False)
    

class CIUDAD(db.Model):
    __tablename__ = 'CIUDAD'
    ID_CIUDAD = db.Column(db.Integer, primary_key=True)
    NOM_CIUD = db.Column(db.String(80), nullable=False)
    ID_REGION = db.Column(db.Integer, db.ForeignKey('REGION.ID_REGION'))
    

class COMUNA(db.Model):
    __tablename__ = 'COMUNA'
    ID_COM = db.Column(db.Integer, primary_key=True)
    NOM_COM = db.Column(db.String(100), nullable=False)
    ID_CIUDAD = db.Column(db.Integer, db.ForeignKey('CIUDAD.ID_CIUDAD'))
    ID_REGION = db.Column(db.Integer, db.ForeignKey('REGION.ID_REGION'))
    

class ROL(db.Model):
    __tablename__ = 'ROL'
    ID_ROL = db.Column(db.Integer, primary_key=True)
    NOMBRE_ROL = db.Column(db.String(50))
    



class CLIENTE(db.Model):
    __tablename__ = 'CLIENTE'
    RUT_CLI = db.Column(db.String(8), primary_key=True)
    DV_CLI = db.Column(db.String(1), nullable=False)
    NOM_CLI = db.Column(db.String(80), nullable=False)
    APAT_CLI = db.Column(db.String(50), nullable=False)
    AMAT_CLI = db.Column(db.String(50), nullable=False)
    FECHA_NAC_CLI = db.Column(db.Date, nullable=False)
    DIRECCION_CLI = db.Column(db.String(100), nullable=False)
    EMAIL_CLI = db.Column(db.String(100), nullable=False)
    CONTRASEÑA = db.Column(db.String(6), nullable=False)
    ID_ROL = db.Column(db.Integer, db.ForeignKey('ROL.ID_ROL'), default=2)
    ID_COM = db.Column(db.Integer, db.ForeignKey('COMUNA.ID_COMUNA'))
    ID_CIUDAD = db.Column(db.Integer, db.ForeignKey('CIUDAD.ID_CIUDAD'))
    ID_REGION = db.Column(db.Integer, db.ForeignKey('REGION.ID_REGION'))

class Instrumento(db.Model):
    __tablename__ = 'INSTRUMENTO'
    ID_INSTR = db.Column(db.Integer, primary_key=True)
    NOMBRE_INSTR = db.Column(db.String(100), nullable=False)
    DESCRIPCION_INSTR = db.Column(db.String(100))
    PRECIO_INSTR = db.Column(db.Integer, nullable=False)
    STOCK_INSTR = db.Column(db.Integer, nullable=False)
    ID_SUBTIPO = db.Column(db.Integer, db.ForeignKey('SUBTIPO.ID_SUBTIPO'))

    subtipo = db.relationship('Subtipo', backref='instrumentos')

class Subtipo(db.Model):
    __tablename__ = 'SUBTIPO'
    ID_SUBTIPO = db.Column(db.Integer, primary_key=True)
    NOMBRE_SUBTIPO = db.Column(db.String(60), nullable=False)
    ID_MARCA = db.Column(db.Integer, db.ForeignKey('MARCA.ID_MARCA'))

    marca = db.relationship('Marca', backref='subtipos')

class Marca(db.Model):
    __tablename__ = 'MARCA'
    ID_MARCA = db.Column(db.Integer, primary_key=True)
    NOMBRE_MARCA = db.Column(db.String(60), nullable=False)

class Carrito(db.Model):
    __tablename__ = 'CARRITO'
    ID_CARRITO = db.Column(db.Integer, primary_key=True)
    RUT_CLI = db.Column(db.String(8), db.ForeignKey('CLIENTE.RUT_CLI'))
    FECHA_COMPRA_CARRITO = db.Column(DateTime, default=datetime.utcnow)
    PRECIO_TOTAL_CARRITO = db.Column(Numeric(10,2), nullable = False)
    CANTIDAD = db.Column(db.Integer, nullable= False)

class Estado_pago(db.Model):
    __tablename__ = 'ESTADO_PAGO'
    ID_ESTADO_PAGO = db.Column(db.Integer, primary_key=True)
    DESCRIPCION_ESTADO_PAGO = db.Column(db.String(20), nullable=False, default='Pendiente')
    
class Pago(db.Model):
    __tablename__ = 'Pago'
    ID_PAGO = db.Column(db.Integer, primary_key=True)
    ID_CARRITO = db.Column(db.Integer, db.ForeignKey('CARRITO.ID_CARRITO'))
    MONTO_TOTAL_PAGO = db.Column(db.Numeric(10, 2))
    FECHA_PAGO = db.Column(db.DateTime, default=datetime.utcnow)
    ID_ESTADO_PAGO = db.Column(db.Integer, db.ForeignKey('ESTADO_PAGO.ID_ESTADO_PAGO'), default=1)
    
