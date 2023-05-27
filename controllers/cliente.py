from flask import request, jsonify
from app import app, db
from model import Cliente, Region, Comuna, Ciudad

@app.route('/registro', methods=['POST'])
def registro_usuario():
    # Obtener los datos del formulario de registro
    rut = request.form['rut']
    dv = request.form['dv']
    nombre = request.form['nombre']
    apaterno = request.form['apaterno']
    amaterno = request.form['amaterno']
    fecha_nacimiento = request.form['fecha_nacimiento']
    direccion = request.form['direccion']
    email = request.form['email']
    contraseña = request.form['contraseña']
    region_nombre = request.form['region']
    comuna_nombre = request.form['comuna']
    ciudad_nombre = request.form['ciudad']

    # Obtener los IDs correspondientes a las regiones, comunas y ciudades seleccionadas
    region = Region.query.filter_by(nombre=region_nombre).first()
    comuna = Comuna.query.filter_by(nombre=comuna_nombre).first()
    ciudad = Ciudad.query.filter_by(nombre=ciudad_nombre).first()

    # Crear una instancia del modelo Cliente con los datos recibidos
    cliente = Cliente(
        RUT_CLI=rut,
        DV_CLI=dv,
        NOM_CLI=nombre,
        APAT_CLI=apaterno,
        AMAT_CLI=amaterno,
        FECHA_NAC_CLI=fecha_nacimiento,
        DIRECCION_CLI=direccion,
        EMAIL_CLI=email,
        CONTRASEÑA=contraseña,
        ID_ROL=2,
        ID_COM=comuna.id if comuna else None,
        ID_CIUDAD=ciudad.id if ciudad else None,
        ID_REGION=region.id if region else None
    )

    # Guardar el nuevo cliente en la base de datos
    db.session.add(cliente)
    db.session.commit()

    return jsonify({'message': 'Usuario creado exitosamente'})
