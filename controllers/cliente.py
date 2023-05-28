from flask import Flask, Blueprint, request, jsonify
from app import db
from model import Cliente



app = Flask(__name__)


cliente_bp = Blueprint('clientes', __name__)


@cliente_bp.route('/cliente', methods=['POST'])
def create_cliente():
    data = request.get_json()
    
    rut = data['rut']
    dv = data['dv']
    nombre = data['nombre']
    apaterno = data['apaterno']
    amaterno = data['amaterno']
    direccion = data['direccion']
    email = data['email']
    contrasenia = data['contrasenia']
    
    cliente = Cliente(
        RUT_CLI=rut,
        DV_CLI=dv,
        NOM_CLI=nombre,
        APAT_CLI=apaterno,
        AMAT_CLI=amaterno,
        DIRECCION_CLI=direccion,
        EMAIL_CLI=email,
        CONTRASENIA=contrasenia
        
    )
    
    db.session.add(cliente)
    db.session.commit()

    return jsonify({'message': 'Cliente creado exitosamente'}), 201


@cliente_bp.route('/clientes', methods=['GET'])
def obtener_clientes():
    # Obtener todos los clientes de la base de datos
    clientes = Cliente.query.all()

    # Crear una lista para almacenar los datos de los clientes
    lista_clientes = []

    # Iterar sobre los clientes y agregar sus datos a la lista
    for cliente in clientes:
        
        

        cliente_data = {
            'rut': cliente.RUT_CLI,
            'dv': cliente.DV_CLI,
            'nombre': cliente.NOM_CLI,
            'apaterno': cliente.APAT_CLI,
            'amaterno': cliente.AMAT_CLI,
            'direccion': cliente.DIRECCION_CLI,
            'email': cliente.EMAIL_CLI,
            'contrasenia': cliente.CONTRASENIA
            
        }
        lista_clientes.append(cliente_data)

    return jsonify(lista_clientes)


