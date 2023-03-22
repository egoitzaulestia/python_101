   create table usuarios (
    ID number not null constraint usuarios_pk primary key,
    Nombre varchar2(50) not null,
    Email varchar2(255)
);
/

-- NO EJECUTAR LA SIGUIENTE SENTENCIA 
alter table usuarios add constraint usuarios_id_uq unique (ID); -- Restricciones

INSERT INTO Usuarios (ID, Nombre, Email)
VALUES (1, 'Jon', 'jon@gmail.com') 

	SELECT * FROM usuarios

INSERT INTO Usuarios (ID, Nombre, Email)
VALUES (2, 'Ego', 'ego@gmail.com') 





SELECT * FROM ALL_TABLES
    
DESCRIBE scott.emp -- Para describir LA INFORMACIÓN DE LAS TABLAS
    
SELECT * FROM USER_TABLES
SELECT * FROM USER_VIEWS
SELECT * FROM USER_SEQUENCES -- Para hacer incremento

DESCRIBE user

create sequence Usuario_Seq1
start with 1
increment by 1

SELECT * FROM USER_SEQUENCES

SELECT * FROM Usuarios
    
-- Para insertar ejecutar las dos siguientes lineas
INSERT INTO Usuarios (ID, Nombre)
VALUES (USUARIO_SEQ1.nextVal, 'jon')

CREATE TABLE tasks (
    id
)
INSERT INTO Usuarios (ID, Nombre)
VALUES (USUARIO_SEQ1.nextVal, 'maria')
INSERT INTO Usuarios (ID, Nombre)
VALUES (USUARIO_SEQ1.nextVal, 'jaun')

SELECT USUARIO_SEQ1.nextVal FROM DUAL

SELECT CURRENT_DATE FROM DUAL -- Para mostrar la información

select * from Usuarios

INSERT INTO Usuarios (ID, Nombre)
VALUES (USUARIO_SEQ1.nextVal, 'Ego')
    
UPDATE USUARIOS 
SET Nombre = 'Ego MAN'
WHERE ID = 1

DELETE FROM Usuarios
WHERE ID = 1

UPDATE USUARIOS 
SET Nombre = 'Ego MAN'
WHERE ID = 0

ROLLBACK --UNDO
COMMIT --

-- CRUD: Create, Read, Update, Delete

-- EJERCICIO DE CLASE -- 
-- creamos tabla Material y creamos una Sequencia de autoincremento

SELECT * FROM MATERIAL

SELECT * FROM USER_TABLES

SELECT * FROM MATERIAL
    
INSERT INTO Material (ID, Nombre, Precio)
VALUES (MATERIALS_SEQ1.nextVal, 'BCI', 300)

INSERT INTO Material (ID, Nombre, Precio)
VALUES (MATERIALS_SEQ1.nextVal, 'VR GLASESS', 450)

UPDATE MATERIAL
SET Nombre = '3D Printer'
WHERE ID = 3

UPDATE MATERIAL
SET pRECIO = 600
WHERE ID = 3

INSERT INTO Material (ID, Nombre, Precio)
VALUES (MATERIALS_SEQ1.nextVal, 'PC + Graphic Card', 1550)

INSERT INTO Material (ID, Nombre, Precio)
VALUES (MATERIALS_SEQ1.nextVal, 'Muse2 BCI', 280)

SELECT * FROM MATERIAL

DELETE FROM Material
WHERE Nombre = 'BCI'