-- 实验二
USE xskc;

-- 导入数据库文件
INSERT INTO Student VALUES('201215121','李勇','男',20,'CS')
INSERT INTO Student VALUES('201215122','刘晨','女',19,'CS')
INSERT INTO Student VALUES('201215131','刘晨2','女',19,'CS')
INSERT INTO Student VALUES('201215132','刘','女',19,'CS')	--插入多几个做编码比较
INSERT INTO Student VALUES('201215141','l','女',19,'CS')
INSERT INTO Student VALUES('201215142','ll','女',19,'CS')
INSERT INTO Student VALUES('201215143','lll','女',19,'CS')
INSERT INTO Student VALUES('201215123','王敏','女',18,'MA')
INSERT INTO Student VALUES('201215125','张立','男',19,'IS')
INSERT INTO Student VALUES('201331001','欧阳原野','男',17,'CS')
INSERT INTO Student VALUES('201439002','刘小莉','女',16,'CS')

INSERT INTO Course VALUES('1','数据库','5',4)    --注意在此处由于先修课须存在的约束，插入前须先置NULL
INSERT INTO Course VALUES('2','数学',NULL,2)
INSERT INTO Course VALUES('3','信息系统','1',4)
INSERT INTO Course VALUES('4','操作系统','6',3)
INSERT INTO Course VALUES('5','数据结构','7',4)
INSERT INTO Course VALUES('6','数据处理',NULL,2)
INSERT INTO Course VALUES('7','C语言',6,4)
INSERT INTO Course VALUES('8','DB_Design',1,2)

UPDATE Course SET Cpno='8' WHERE Cno='1'	--修正先修课的数据

INSERT INTO SC VALUES('201215121','1',92)
INSERT INTO SC VALUES('201215121','2',85)
INSERT INTO SC VALUES('201215121','3',88)
INSERT INTO SC VALUES('201215122','2',90)
INSERT INTO SC VALUES('201215122','3',80)
INSERT INTO SC VALUES('201331001','1',55)
INSERT INTO SC VALUES('201331001','2',90)
INSERT INTO SC VALUES('201331001','3',80)
INSERT INTO SC VALUES('201439002','1',69)
INSERT INTO SC VALUES('201215125','1',NULL)

-- END 导入数据库文件

SELECT * FROM Student;
SELECT * FROM SC;
SELECT * FROM Course;

SELECT Sname,Sno,Sdept FROM Student;

SELECT Sno,Sname,2018-Sage as 'Birthday' FROM Student;

SELECT Sno,Sname,2018-Sage 'Birthday',LOWER(Sdept) Sdept FROM Student;

SELECT  Sno, Sname FROM  Student WHERE  Sdept='MA';

SELECT DISTINCT Sno FROM SC WHERE  Grade<60;

SELECT  Sname, Sage FROM  Student WHERE  Sage<20;

SELECT  Sname, Sage FROM  Student WHERE  Sage>=18 AND Sage<=22;
SELECT  Sname, Sage FROM  Student WHERE  Sage  BETWEEN 18 AND 22;
SELECT  Sname, Sage FROM  Student WHERE  Sage  NOT  BETWEEN  18 AND 20;

SELECT  Sno, Sname, Ssex  FROM  Student WHERE  Sdept  IN ('CS', 'MA', 'IS');
SELECT  Sno, Sname, Ssex FROM  Student WHERE  Sdept='CS' OR Sdept='MA' OR Sdept='IS';
SELECT  Sname, Ssex FROM  Student WHERE  Sdept  NOT  IN ('IS', 'MA', 'CS');

SELECT  Sname, Sno, Ssex FROM  Student WHERE  Sname  LIKE  '刘%';

SELECT  Sname, Sdept  FROM  Student WHERE  Sname  LIKE  '刘___';

SELECT  Sname, Sage FROM  Student WHERE  Sname NOT LIKE '刘%';

SELECT  Cno, Ccredit FROM  Course WHERE  Cname LIKE 'DB\_DESIGN' ESCAPE '\';

SELECT  * FROM  Course WHERE  Cname LIKE 'DB\_%DESIG_'ESCAPE'\';	-- 查询以"DB_"开头,且倒数字符为“DESIG(N)”的课程

SELECT  Sno, Cno FROM  SC WHERE  Grade IS NULL;
SELECT  Sno, Cno FROM  SC WHERE  Grade IS NOT NULL;

SELECT  Sno, Grade FROM SC WHERE  Cno='3' ORDER BY Grade DESC;
SELECT  * FROM  Student ORDER BY Sdept ASC, Sage DESC;

SELECT  COUNT(*) FROM  Student;
SELECT  COUNT(*) count_name FROM  Student;
SELECT  COUNT(DISTINCT Sno) FROM SC;

SELECT  AVG(Grade) FROM  SC WHERE  Cno='2';  --应该是88.3333..但由于是int，暂时忽略

SELECT  MAX(Grade) FROM  SC WHERE  Cno='2';

SELECT  SUM(Ccredit) FROM  SC,Course WHERE  Sno='201215122' AND SC.Cno=Course.Cno;

SELECT  Cno , COUNT(Sno) CntSno FROM  SC GROUP  BY Cno;

SELECT  Sno FROM  SC GROUP BY Sno HAVING  COUNT(Cno)>2;


--END实验二