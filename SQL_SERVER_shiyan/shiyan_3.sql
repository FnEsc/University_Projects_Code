-- 实验三
USE xskc;

SELECT Student.*,SC.* FROM Student,SC WHERE Student.Sno=SC.Sno;

SELECT Student.Sno, Sname, Ssex, Sage, Sdept, Cno, Grade FROM Student,SC WHERE Student.Sno=SC.Sno;

SELECT A.Cno,A.Cname,B.Cpno FROM Course A, Course B  -- 这样是笛卡尔积的连接，是不对的
SELECT A.Cno,A.Cname,B.Cpno FROM Course A, Course B WHERE A.Cpno=B.Cno   -- 表别名

SELECT Student.Sno,Sname,Ssex,Sdept,Cno,Grade FROM Student,SC WHERE Student.Sno=SC.Sno;

SELECT Student.Sno,Sname,Ssex,Sdept,Cno,Grade FROM Student LEFT JOIN SC ON Student.Sno=SC.Sno;  --这里的话lll是没有成绩的，但左漂浮在查询中了
SELECT Student.Sno,Sname,Ssex,Sdept,Cno,Grade FROM SC RIGHT JOIN Student ON Student.Sno=SC.Sno;  --跟上条语句查询结果一样，是注重左右漂浮的对象

SELECT Student.Sno,Sname,Cname,Grade FROM Student,SC,Course WHERE Student.Sno=SC.Sno AND SC.Cno=Course.Cno; -- 多表查询


SELECT Sno,Sname,Sdept 
FROM Student 
WHERE Sdept IN 
	(SELECT Sdept FROM Student WHERE Sname='李勇')
SELECT  Sno , Sname, Sdept
FROM  Student
WHERE  Sdept =
     (SELECT  Sdept
      FROM  Student
      WHERE  Sname='李勇');
SELECT A.Sno,A.Sname,A.Sdept FROM Student A,Student B WHERE A.Sdept=B.Sdept AND B.Sname='李勇'


SELECT Sname,Sdept 
FROM Student 
WHERE Sno IN
	(SELECT Sno FROM SC WHERE Cno='2')
SELECT Sname,Sdept FROM Student,SC WHERE Student.Sno=SC.Sno AND SC.Cno='2'


SELECT  Sno, Sname
FROM  Student
WHERE  Sno  IN
   (SELECT  Sno
	FROM  SC
	WHERE  Cno  IN
      (SELECT  Cno
       FROM  Course
       WHERE  Cname = '数据库'))
SELECT Student.Sno,Student.Sname FROM Student,SC,Course WHERE SC.Cno=Course.Cno AND Course.Cname='数据库' AND SC.Sno=Student.Sno;

INSERT INTO Student VALUES('201215153','王敏','女',10,'MA')
SELECT Sname,Sage FROM Student WHERE Sdept!='CS' AND Sage<=ALL(SELECT Sage FROM Student WHERE Sdept='CS')  -- !=或者<>都是正确的

SELECT Sname,Sage FROM Student WHERE Sdept<>'CS' AND Sage <= (SELECT MIN(Sage) FROM Student WHERE Sdept='CS')

SELECT Sname,Sdept FROM Student WHERE EXISTS (SELECT * FROM SC WHERE SC.Sno=Student.Sno AND Cno='1')

SELECT  Sno, Sname, Sdept FROM  Student A WHERE  EXISTS (SELECT * FROM  Student B WHERE  B.Sdept=A.Sdept AND B.Sname='李勇');

SELECT Sname,Sdept FROM Student WHERE NOT EXISTS 
	(SELECT * FROM Course WHERE NOT EXISTS 
		(SELECT * FROM SC,Student,Course WHERE SC.Sno=Student.Sno AND SC.Cno=Course.Cno) )	
SELECT Sname,Sdept FROM Student WHERE NOT EXISTS (SELECT * FROM Course WHERE NOT EXISTS (SELECT * FROM SC,Student,Course WHERE SC.Sno=Student.Sno AND SC.Cno=Course.Cno))

SELECT * FROM Student WHERE Sdept='CS' UNION SELECT * FROM Student WHERE Sage <=20  --UNION是或、接下去输出查询

SELECT * FROM Student WHERE Sdept='CS' OR Sage<=20

SELECT * FROM Student WHERE Sdept='CS' AND Sage<20;


--END实验三









