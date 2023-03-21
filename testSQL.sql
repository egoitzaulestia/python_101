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
