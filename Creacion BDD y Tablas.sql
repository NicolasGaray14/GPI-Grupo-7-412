create database PARALELA;
use PARALELA;

create table salas(
	codigo varchar(25) primary key,
	nombre varchar(25),
	capacidad int not null
);

create table reservas(
  token VARCHAR(25) NOT NULL PRIMARY KEY,
    emailUsuario VARCHAR(50) NOT NULL,
    sala varchar(25) not null,
    fechaInicio DATETIME,
    fechaTermino DATETIME,
    FOREIGN KEY (emailUsuario) REFERENCES personas(correo),
    FOREIGN KEY (sala) REFERENCES salas(codigo)
    );

create table personas(
	nombre varchar(25) not null,
	correo varchar(50) primary key
);