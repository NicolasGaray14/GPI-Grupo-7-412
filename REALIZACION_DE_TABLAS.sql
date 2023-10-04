create table tipo_producto(
	sku varchar(50) primary key not null,
	nombre varchar(50)
);

--inventario
create table inventario(
	cod_inventario varchar(50) not null,
	cantidad int not null default 0,
	cod_ubicacion int not null default 0,
	foreign key (cod_inventario) references tipo_producto(sku),
	foreign key (cod_ubicacion) references ubicaciones(cod_ubi)
);
--tabla ubicaciones de la tienda
create table ubicaciones(
	cod_ubi int not null primary key default 0,
	descripcion varchar(50)
);
--Tabla de entradas, donde se actualiza el inventario
--create table entradas(
--	sku varchar(50) not null,
--	fecha datetime default getdate(),
--	cantidad int not null default 0
--	foreign key (sku) references tipo_producto(sku)
--);
--alter table entradas
--add razon varchar(50) not null default ' ';

-- Tablas de ventas, donde se actualiza en inventario
--create table salidas(
--	sku varchar(50) not null,
--	fecha datetime default getdate(),
--	cantidad int not null default 0
--	foreign key (sku) references tipo_producto(sku)
--);

create table movimiento(
	sku varchar(50) not null,
	fecha datetime default getdate(),
	cantidad int not null default 0,
	razon varchar(50) not null default ' ',
	foreign key (sku) references tipo_producto(sku)
);
