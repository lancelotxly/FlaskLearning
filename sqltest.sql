create table emp (ename varchar(20), hiredate date, sal decimal(10,2), deptno INT(3));
create table dept (deptno INT(3), deptname varchar(20));
insert into emp (ename, hiredate, sal, deptno) VALUES ('zzx','2000-01-01',2000,1),
  ('lisa','2003-02-01',4000,2),('bjguan','2004-04-02',5000,1),('bzshen','2005-04-01',4000,3);
insert into dept (deptno, deptname) VALUES (1,'tech'),(2,'sal'),(3,'hr');
insert Into dept (deptno, deptname) VALUES (5,'doc');
insert into emp (ename, hiredate, sal, deptno) VALUES ('dony','2005-02-05',2000,4);
select *from emp;
select *from dept;
select ename,deptname from emp,dept where emp.deptno=dept.deptno;
select ename,deptname from emp left join dept on emp.deptno=dept.deptno;
select ename,deptname from emp right join dept on emp.deptno=dept.deptno;
select * from emp;
select * from dept;
select * from emp where deptno in (select deptno from dept);
select ename from emp UNION select deptno from dept;