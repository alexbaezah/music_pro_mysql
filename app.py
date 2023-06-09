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
from controllers.region import regiones_blueprint
from controllers.comuna import comunas_blueprint
from controllers.ciudad import ciudades_blueprint
from controllers.cliente import cliente_bp





app.register_blueprint(instrumentos_blueprint)
app.register_blueprint(pagos_blueprint)
app.register_blueprint(accesorios_blueprint)
app.register_blueprint(webpay_blueprint, url_prefix='/webpay')
app.register_blueprint(index_blueprint)
app.register_blueprint(regiones_blueprint)
app.register_blueprint(comunas_blueprint)
app.register_blueprint(ciudades_blueprint)
app.register_blueprint(cliente_bp)






"""@app.route('/')
def index():
    return render_template('index.html')
"""