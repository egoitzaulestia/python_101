-- SELECT * FROM SCOTT.EMP;

SELECT *
FROM scott.DEPT
-- WHERE SAL > 2000 AND JOB LIKE 'M%'
-- WHERE Ename = 'BLAKE'
WHERE DEPTNO = 30

SELECT *
FROM scott.EMP
INNER JOIN scott.dept ON emp.deptno = dept.deptno

SELECT nombre, apellido, emp.nombre
FROM cott.EMP
INNER JOIN scott.dept ON emp.deptno = dept.deptno
WHERE -- para filtrar las filas
ORDER BY nombre desc -- para ordenar por...

-- Todos los datos de los empleados del departamento “RESEARCH”
SELECT *
FROM scott.EMP
    JOIN scott.dept ON emp.deptno = dept.deptno
    	WHERE dname = 'RESEARCH'

-- Todos los datos del empleado no 7844
SELECT *
FROM scott.emp
	JOIN scott.dept ON emp.deptno = dept.deptno
		WHERE EMPNO = 7844 

-- Todos los datos de los empleados que son MANAGERS y trabajan en CHICAGO
SELECT *
FROM scott.emp
	JOIN scott.dept ON emp.deptno = dept.deptno
		WHERE JOB = 'MANAGER' AND LOC = 'CHICAGO'

-- Mostrar sólo el nombre y salario del empleado quienes trabajan en Nueva York. 
SELECT ename, sal
FROM scott.emp
	JOIN scott.dept ON emp.deptno = dept.deptno
		WHERE LOC = 'NEW YORK'

-- Mostrar los resultados ordenados por salario (quien gana más a menos).
SELECT ename, sal
FROM scott.emp
	JOIN scott.dept ON emp.deptno = dept.deptno
		ORDER BY sal DESC
    
SELECT *
FROM scott.emp
	JOIN scott.dept ON emp.deptno = dept.deptno
		ORDER BY sal DESC
--
-- WHERE ENAME LIKE 'M%' -- Texto que empieza por M-
-- WHERE ENAME LIKE '%Z' -- Texto que termine en -Z
--

-- Después, mostrar solo los empleados que ganan más de 2,000.
SELECT ename, sal
FROM scott.emp
	JOIN scott.dept ON emp.deptno = dept.deptno
		WHERE LOC = 'NEW YORK' AND sal > 2000 
    		ORDER BY sal DESC 
				LIMIT 10



-- Para Crear una Tabla
create table usuarios (
    ID number not null constraint usuarios_pk primary key,
    Nombre varchar2(50) not null,
    Email varchar2(255)
);
/

alter table usuarios add constraint usuarios_id_uq unique (ID); -- Restricciones
