from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/music_pro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



# Importar los controladores después de inicializar db para evitar la importación circular
from controllers.instrumento import instrumentos_blueprint
from controllers.pago import pagos_blueprint
from api.api import webpay_blueprint
from controllers.accesorio import accesorios_blueprint
from index import index_blueprint

app.register_blueprint(instrumentos_blueprint)
app.register_blueprint(pagos_blueprint)
app.register_blueprint(accesorios_blueprint)
app.register_blueprint(webpay_blueprint, url_prefix='/webpay')
app.register_blueprint(index_blueprint)
