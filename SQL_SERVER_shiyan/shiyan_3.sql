-- ʵ����
USE xskc;

SELECT Student.*,SC.* FROM Student,SC WHERE Student.Sno=SC.Sno;

SELECT Student.Sno, Sname, Ssex, Sage, Sdept, Cno, Grade FROM Student,SC WHERE Student.Sno=SC.Sno;

SELECT A.Cno,A.Cname,B.Cpno FROM Course A, Course B  -- �����ǵѿ����������ӣ��ǲ��Ե�
SELECT A.Cno,A.Cname,B.Cpno FROM Course A, Course B WHERE A.Cpno=B.Cno   -- �����

SELECT Student.Sno,Sname,Ssex,Sdept,Cno,Grade FROM Student,SC WHERE Student.Sno=SC.Sno;

SELECT Student.Sno,Sname,Ssex,Sdept,Cno,Grade FROM Student LEFT JOIN SC ON Student.Sno=SC.Sno;  --����Ļ�lll��û�гɼ��ģ�����Ư���ڲ�ѯ����
SELECT Student.Sno,Sname,Ssex,Sdept,Cno,Grade FROM SC RIGHT JOIN Student ON Student.Sno=SC.Sno;  --����������ѯ���һ������ע������Ư���Ķ���

SELECT Student.Sno,Sname,Cname,Grade FROM Student,SC,Course WHERE Student.Sno=SC.Sno AND SC.Cno=Course.Cno; -- ����ѯ


SELECT Sno,Sname,Sdept 
FROM Student 
WHERE Sdept IN 
	(SELECT Sdept FROM Student WHERE Sname='����')
SELECT  Sno , Sname, Sdept
FROM  Student
WHERE  Sdept =
     (SELECT  Sdept
      FROM  Student
      WHERE  Sname='����');
SELECT A.Sno,A.Sname,A.Sdept FROM Student A,Student B WHERE A.Sdept=B.Sdept AND B.Sname='����'


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
       WHERE  Cname = '���ݿ�'))
SELECT Student.Sno,Student.Sname FROM Student,SC,Course WHERE SC.Cno=Course.Cno AND Course.Cname='���ݿ�' AND SC.Sno=Student.Sno;

INSERT INTO Student VALUES('201215153','����','Ů',10,'MA')
SELECT Sname,Sage FROM Student WHERE Sdept!='CS' AND Sage<=ALL(SELECT Sage FROM Student WHERE Sdept='CS')  -- !=����<>������ȷ��

SELECT Sname,Sage FROM Student WHERE Sdept<>'CS' AND Sage <= (SELECT MIN(Sage) FROM Student WHERE Sdept='CS')

SELECT Sname,Sdept FROM Student WHERE EXISTS (SELECT * FROM SC WHERE SC.Sno=Student.Sno AND Cno='1')

SELECT  Sno, Sname, Sdept FROM  Student A WHERE  EXISTS (SELECT * FROM  Student B WHERE  B.Sdept=A.Sdept AND B.Sname='����');

SELECT Sname,Sdept FROM Student WHERE NOT EXISTS 
	(SELECT * FROM Course WHERE NOT EXISTS 
		(SELECT * FROM SC,Student,Course WHERE SC.Sno=Student.Sno AND SC.Cno=Course.Cno) )	
SELECT Sname,Sdept FROM Student WHERE NOT EXISTS (SELECT * FROM Course WHERE NOT EXISTS (SELECT * FROM SC,Student,Course WHERE SC.Sno=Student.Sno AND SC.Cno=Course.Cno))

SELECT * FROM Student WHERE Sdept='CS' UNION SELECT * FROM Student WHERE Sage <=20  --UNION�ǻ򡢽���ȥ�����ѯ

SELECT * FROM Student WHERE Sdept='CS' OR Sage<=20

SELECT * FROM Student WHERE Sdept='CS' AND Sage<20;


--ENDʵ����









