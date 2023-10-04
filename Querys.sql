use prueba;
-- AGREGAMOS PRODUCTOS, CON LOS QUE SE TRABAJARA EN EL INVENTARIO
INSERT INTO tipo_producto (nombre, sku)
VALUES
  ('Naranjo', 'NAJ'),
  ('Arbol', 'ARB'),
  ('arbusto', 'ARBT'),
  ('Tierra de hojas', 'TH'),
  ('Fertilizante', 'FT'),
  ('Insecticida', 'INC'),
  ('Durmiente', 'DUR'),
  ('Maceteros', 'MAC');
  select* from tipo_producto

-- AGREGAMOS LAS UBICACIONES DE LA JARDINERIA
insert into ubicaciones(descripcion, cod_ubi)
values
	('Frontis',1),
	('Patio A',2),
	('Bodega',3),
	('Patio B',4);
select* from ubicaciones

--GENERAMOS EL INVENTARIO Y AEXISTENTE AL MOMENTO DE PONER EN MARCHA LA BDD
insert into inventario(cod_inventario,cantidad, cod_ubicacion)
values
	('ARB',4,1),
	('TH',100,2),
	('DUR',80,3),
	('FT',200,3),
	('MAC',150,2);
select* from inventario

-- EN ESTA QUERY SE AGREGAN A LA TABLA DE ENTRADA TODOS LOS PRODUCTOS QUE LLEGUEN A LA JARDINERIA
insert into entradas(sku,cantidad)
values
	('ARB',1),
	('DUR',10),
	('MAC',30);

--ACTUALIZAMOS EL INVENTARIO CON LOS NUEVOS PRODUCTOS QUE NOS LLEGAN
UPDATE inventario
SET cantidad = inventario.cantidad + entradas.cantidad
FROM inventario
INNER JOIN entradas ON inventario.cod_inventario = entradas.sku;

select* from inventario


-- EN ESTA QUERY SE AGREGAN A LA TABLA DE SALIDA TODOS LOS PRODUCTOS QUE SALGAN DE LA JARDINERIA
insert into salidas(sku,cantidad)
values
	('DUR',2),
	('MAC',15);

select* from salidas

--ACTUALIZAMOS EL INVENTARIO CON PRODUCTOS QUE SALGAN
UPDATE inventario
SET cantidad = inventario.cantidad - salidas.cantidad
FROM inventario
INNER JOIN salidas ON inventario.cod_inventario = salidas.sku;

select* from inventario


-- Restar la cantidad en caso de 'venta'
UPDATE inventario
SET cantidad = inventario.cantidad - movimiento.cantidad
FROM inventario
INNER JOIN movimiento ON inventario.cod_inventario = movimiento.sku
WHERE movimiento.razon = 'venta';

-- Sumar la cantidad en caso de 'devolucion' o 'actualizacion de inventario'
UPDATE inventario
SET cantidad = inventario.cantidad + movimiento.cantidad
FROM inventario
INNER JOIN movimiento ON inventario.cod_inventario = movimiento.sku
WHERE movimiento.razon = 'devolucion' OR  movimiento.razon = 'actualizacion de inventario';



