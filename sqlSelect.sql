create table Student(Sno varchar(20) primary key, Sname varchar(20) not null,
  Ssex varchar(20) not null, Sbirthday datetime, Class varchar(20));
create table Course(Cno varchar(20) primary key , Cname varchar(20) not null, Tno varchar(20) not null );
create table Score(Sno varchar(20) not null, Cno varchar(20) not null , Degree DECIMAL(4,1),
constraint Sno_fk foreign key (Sno) references Student(Sno),
constraint Cno_fk foreign key (Cno) references Course(Cno));
create table Teacher(Tno varchar(20) primary key ,Tname varchar(20) not null
  ,Tsex varchar(20) not null , Tbirthday datetime, Prof varchar(20), Depart varchar(20) not null );

insert into Student (Sno, Sname, Ssex, Sbirthday, Class) values ('108','曾华','男','1997-09-01','95033');
insert into Student (Sno, Sname, Ssex, Sbirthday, Class) VALUES ('105','匡明','男','1975-10-02','95031'),
  ('107','王丽','女','1976-01-23','95033'),('101','李军','男','1976-02-20','95033'),
  ('109','王芳','女','1975-02-10','95031'),('103','陆军','男','1974-06-03','95031');
select * from Student;

insert into Course (Cno, Cname, Tno) VALUES
  ('3-105','计算机导论','825'),('3-245','操作系统','804'),('6-166','数字电路','856'),('9-888','高等数学','831');
select * from Course;

insert into Score(Sno, Cno, Degree) VALUES
  ('103','3-245','86'),('105','3-245','75'),('109','3-245','68'),
  ('103','3-105','92'),('105','3-105','88'),('109','3-105','76'),
  ('101','3-105','64'),('107','3-105','91'),('108','3-105','78'),
  ('101','6-166','85'),('107','6-166','79'),('108','6-166','81');
select * from Score;

insert into Teacher(Tno, Tname, Tsex, Tbirthday, Prof, Depart) VALUES
  ('804','李成','男','1958-12-02','副教授','计算机系'),
  ('856','张旭','男','1969-03-12','讲师','电子工程系'),
  ('825','王平','女','1972-05-05','助教','计算机系'),
  ('831','刘冰','女','1977-08-14','助教','电子工程系');
select * from Teacher;

select * from Student;
select Sname, Ssex, Class from Student;
select * from Teacher;
select DISTINCT Depart from Teacher;
--# 查询一段数据 BETWEEN:  a BETWEEN min AND max, 当 min<=a<=max 返回1， 否则返回0
select * from Score where  Degree between 60 and 80;
--# 查询某些数据 IN: a in (1,2,3)
select * from Score where Degree in (85,86,88);
select * from Student where Class='97031' or Ssex='女';
--# 按顺序排序数据: ORDER BY col [ASC/DESC]
select * from Student order by Class desc;
select * from Score order by Cno asc , Degree desc ;
select count(Sno) from Student where Class='95031';
--# 查询Score表中的最高分的学生学号和课程号。（子查询或者排序
select Sno, Cno from Score where Degree = (select max(Degree) from Score);
select Sno, Cno from Score order by Degree desc limit 0,1;
--# 查询每门课的平均成绩。
select Cno, avg(Degree) from Score group by Cno;
--# 查询Score表中至少有5名学生选修的并以3开头的课程的平均分数。
select avg(Degree) from Score where Cno like '3%' and Cno in (select Cno from Score group by Cno having count(Cno)>=5);
select Sno from Score where Degree>70 and Degree<90;

-- #  查询所有学生的Sname、Cno和Degree列
select Sname, Cno, Degree from Student, Score where Student.Sno = Score.Sno;
--# 查询所有学生的Sno、Cname和Degree列
select Sno, Cname, Degree from Score, Course where Score.Cno = Course.Cno;
--# 查询所有学生的Sname、Cname和Degree列
select Sname, Cname, Degree from Student, Course, Score where Student.Sno = Score.Sno and Score.Cno = Course.Cno;
--# 查询“95033”班学生的平均分
select avg(Degree) from Score where Sno in (select Sno from Student where Class='95033');