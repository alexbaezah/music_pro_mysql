-- insert tabla region

INSERT INTO REGION (ID_REGION, NOMBRE_REG) VALUES (1, 'Región Metropolitana');

-- insert tabla ciudad

INSERT INTO CIUDAD (ID_CIUDAD, NOM_CIUD, ID_REGION) VALUES (1, 'Santiago', 1);

-- insert tabla comuna

INSERT INTO COMUNA (ID_COM, NOM_COM, ID_CIUDAD, ID_REGION)
VALUES
    (1, 'Santiago', 1, 1),
    (2, 'Providencia', 1, 1),
    (3, 'Las Condes', 1, 1),
    (4, 'La Reina', 1, 1),
    (5, 'Ñuñoa', 1, 1),
    (6, 'Maipú', 1, 1),
    (7, 'La Florida', 1, 1),
    (8, 'Puente Alto', 1, 1),
    (9, 'Quilicura', 1, 1),
    (10, 'Renca', 1, 1);

-- insert tabla rol

INSERT INTO ROL (ID_ROL, NOMBRE_ROL)
VALUES (1, 'Admin'),
       (2, 'Usuario');


-- insert tabla administrador

INSERT INTO ADMINISTRADOR (RUT_ADM, DV_ADM, NOM_ADM, APAT_ADM, AMAT_ADM, FECHA_NAC_ADM, DIRECCION_ADM, EMAIL_ADM, CONTRASEÑA, ID_ROL, ID_COM, ID_CIUDAD, ID_REGION)
VALUES ('12345678', '9', 'admin', 'admin', 'admin', str_to_date('01/01/2000', '%d/%m/%Y'), 'avenida siempre viva', 'admin@example.com', '123456', 1, 1, 1, 1);

-- insert tabla cliente

INSERT INTO CLIENTE (RUT_CLI, DV_CLI, NOM_CLI, APAT_CLI, AMAT_CLI, FECHA_NAC_CLI, DIRECCION_CLI, EMAIL_CLI, CONTRASEÑA, ID_COM, ID_CIUDAD, ID_REGION)
VALUES ('12345678', '9', 'Manuel', 'Albornoz', 'Paramesio', str_to_date('19/08/1990', '%d/%m/%Y'), 'Dirección', 'manuel@example.com', '123456', 2, 1, 1);

INSERT INTO CLIENTE (RUT_CLI, DV_CLI, NOM_CLI, APAT_CLI, AMAT_CLI, FECHA_NAC_CLI, DIRECCION_CLI, EMAIL_CLI, CONTRASEÑA, ID_COM, ID_CIUDAD, ID_REGION)
VALUES ('87654321', '0', 'Manolo', 'Farías', 'Andrades', str_to_date('24/01/1995', '%d/%m/%Y'), 'Otra Dirección', 'manolo@example.com', '123456', 3, 1, 1);

INSERT INTO CLIENTE (RUT_CLI, DV_CLI, NOM_CLI, APAT_CLI, AMAT_CLI, FECHA_NAC_CLI, DIRECCION_CLI, EMAIL_CLI, CONTRASEÑA, ID_COM, ID_CIUDAD, ID_REGION)
VALUES ('11111111', '2', 'Manuela', 'Milonga', 'Mayoneso', str_to_date('25/05/1995', '%d/%m/%Y'), 'Tercera Dirección', 'manuela@example.com', '123456', 4, 1, 1);

-- insert para tipo_empleado

INSERT INTO TIPO_EMPLEADO (COD_TIPO_EMP, DESC_TIPO_EMP)
VALUES ('V', 'Vendedor');

INSERT INTO TIPO_EMPLEADO (COD_TIPO_EMP, DESC_TIPO_EMP)
VALUES ('B', 'Bodeguero');

INSERT INTO TIPO_EMPLEADO (COD_TIPO_EMP, DESC_TIPO_EMP)
VALUES ('C', 'Contador');


-- Insert para el empleado bodeguero
INSERT INTO EMPLEADO (RUT_EMP, DV_EMP, NOMBRE, APATERNO_EMP, AMATERNO_EMP, FECHA_NAC, DIRECCION, EMAIL_EMP, SALARIO, COD_TIPO_EMP, CONTRASEÑA, ID_COM, ID_CIUDAD, ID_REGION)
VALUES ('12345678', '9', 'Juan', 'Pérez', 'González', str_to_date('1990-05-15', '%d/%m/%Y'), 'Calle 123', 'juan@example.com', 400000, 'b', '123456', 1, 1, 1);

-- Insert para el empleado vendedor
INSERT INTO EMPLEADO (RUT_EMP, DV_EMP, NOMBRE, APATERNO_EMP, AMATERNO_EMP, FECHA_NAC, DIRECCION, EMAIL_EMP, SALARIO, COD_TIPO_EMP, CONTRASEÑA, ID_COM, ID_CIUDAD, ID_REGION)
VALUES ('23456789', '0', 'María', 'López', 'García', str_to_date('1988-10-20', '%d/%m/%Y'), 'Avenida 456', 'maria@example.com', 800000, 'v', '123456', 2, 1, 1);

-- Insert para el empleado contador
INSERT INTO EMPLEADO (RUT_EMP, DV_EMP, NOMBRE, APATERNO_EMP, AMATERNO_EMP, FECHA_NAC, DIRECCION, EMAIL_EMP, SALARIO, COD_TIPO_EMP, CONTRASEÑA, ID_COM, ID_CIUDAD, ID_REGION)
VALUES ('34567890', '1', 'Pedro', 'Rodríguez', 'Fernández', str_to_date('1995-03-10', , '%d/%m/%Y'), 'Plaza 789', 'pedro@example.com', 400000, 'c', '123456', 3, 1, 1);

-- insert para tienda

INSERT INTO TIENDA (ID_TIENDA, NOMBRE_TIENDA, DIR_TIENDA, ID_COM, ID_CIUDAD, ID_REGION)
VALUES (1, 'musicpro santiago', 'Calle Principal 123', 1, 1, 1);

-- insert para vendedor

INSERT INTO VENDEDOR (ID_VENDEDOR, RUT_EMP, ID_TIPO_EMP, VENTAS, ID_TIENDA)
VALUES (1, '23456789', 1, 10, 1);

-- insert para bodega

INSERT INTO BODEGA (ID_BOD, NOMBRE_BOD, DIR_BODEGA, ID_COM, ID_CIUDAD, ID_REGION)
VALUES (1, 'Bodega Santiago', 'Dirección de la bodega', 1, 1, 1);

-- insert para bodeguero

INSERT INTO BODEGUERO (ID_BODEGUERO, RUT_EMP, ID_TIPO_EMP, ID_BOD)
VALUES (1, '12345678', 2, 1);

-- insert para tipo_envio 

INSERT INTO TIPO_ENVIO (COD_TIPO_ENVIO, DESCRIPCION)
VALUES ('R', 'Retiro');

INSERT INTO TIPO_ENVIO (COD_TIPO_ENVIO, DESCRIPCION)
VALUES ('D', 'Despacho');

-- insert para despacho

INSERT INTO DESPACHO (ID_DESPACHO, DESCRIPCION, DIRECCION, COD_TIPO_ENVIO, ID_BOD)
VALUES (1, 'Despacho a domicilio', 'Calle Principal 123', 'D', 1);

-- insert para retiro

INSERT INTO RETIRO (ID_RETIRO, DESCRIPCION, ID_TIENDA, ID_TIPO_ENV)
VALUES (1, 'Retiro en tienda principal', 1, 'R');

-- insert into marca
INSERT INTO MARCA (ID_MARCA, NOMBRE_MARCA) VALUES
(1, 'Tama'),
(2, 'Pearl'),
(3, 'Sonor'),
(4, 'Mapex'),
(5, 'Roland'),
(6, 'Alesis'),
(7, 'ENGL'),
(8, 'Marshall'),
(9, 'Pavey'),
(10, 'EVH'),
(11, 'Gibson');

-- insert subtipo

INSERT INTO SUBTIPO (ID_SUBTIPO, NOMBRE_SUBTIPO, ID_MARCA) VALUES
(1, 'Cuerpo Solido', 11),
(2, 'Acústica', 11),
(3, 'Eléctricas', 11),
(4, 'Bajos Cuatro Cuerdas', 11),
(5, 'Bajos Cinco Cuerdas', 11),
(6, 'Bajos Activos', 11),
(7, 'Bajos Pasivos', 11),
(8, 'Piano de media cola', 11),
(9, 'Piano de cola entera', 11),
(10, 'Pianolas', 11),
(11, 'Batería Acústica', 1),
(12, 'Batería Electrónica', 1),
(13, 'cabezales', 5),
(14, 'cajas', 5);

-- insert instrumento

INSERT INTO INSTRUMENTO (ID_INSTR, NOMBRE_INSTR, DESCRIPCION_INSTR, PRECIO_INSTR, STOCK_INSTR, ID_SUBTIPO) VALUES
(1, 'Guitarra', 'Guitarra súper bacán', 500000, 10, 1),
(2, 'Bajo', 'Bajo bueno como en las canciones de Dua Lipa', 600000, 8, 2),
(3, 'Piano', 'Al pan pan al piano piano', 1500000, 5, 3),
(4, 'Percusión', 'Batería de las buenas', 300000, 15, 4),
(5, 'Amplificador', 'Amplificador de los buenos', 200000, 12, 5);

-- insert accesorio

INSERT INTO ACCESORIO (ID_ACCESORIO, NOMBRE, DESCRIPCION, PRECIO_ACCE, STOCK_ACCE, ID_MARCA) VALUES
(1, 'Audífono', 'Descripción de los audífonos', 50000, 20, 6),
(2, 'Monitor', 'Descripción de los monitores', 100000, 15, 6),
(3, 'Parlantes', 'Descripción de los parlantes', 150000, 10, 6),
(4, 'Cables', 'Descripción de los cables', 20000, 30, 6),
(5, 'Micrófono', 'Descripción de los micrófonos', 80000, 25, 6),
(6, 'Interface', 'Descripción de las interfaces', 120000, 12, 6),
(7, 'Mixer', 'Descripción de los mixers', 200000, 8, 6);
