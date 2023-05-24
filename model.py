from app import db

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
