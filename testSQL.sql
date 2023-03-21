-- SELECT * FROM SCOTT.EMP;

SELECT *
FROM scott.emp
-- WHERE SAL > 2000 AND JOB LIKE 'M%'
-- WHERE Ename = 'BLAKE'
WHERE DEPTNO = 30

SELECT *
FROM scott.EMP
INNER JOIN scott.dept ON emp.deptno = dept.deptno
