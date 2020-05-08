-- ʵ���
USE xskc;

-- �������ݿ��ļ�
INSERT INTO Student VALUES('201215121','����','��',20,'CS')
INSERT INTO Student VALUES('201215122','����','Ů',19,'CS')
INSERT INTO Student VALUES('201215131','����2','Ů',19,'CS')
INSERT INTO Student VALUES('201215132','��','Ů',19,'CS')	--����༸��������Ƚ�
INSERT INTO Student VALUES('201215141','l','Ů',19,'CS')
INSERT INTO Student VALUES('201215142','ll','Ů',19,'CS')
INSERT INTO Student VALUES('201215143','lll','Ů',19,'CS')
INSERT INTO Student VALUES('201215123','����','Ů',18,'MA')
INSERT INTO Student VALUES('201215125','����','��',19,'IS')
INSERT INTO Student VALUES('201331001','ŷ��ԭҰ','��',17,'CS')
INSERT INTO Student VALUES('201439002','��С��','Ů',16,'CS')

INSERT INTO Course VALUES('1','���ݿ�','5',4)    --ע���ڴ˴��������޿�����ڵ�Լ��������ǰ������NULL
INSERT INTO Course VALUES('2','��ѧ',NULL,2)
INSERT INTO Course VALUES('3','��Ϣϵͳ','1',4)
INSERT INTO Course VALUES('4','����ϵͳ','6',3)
INSERT INTO Course VALUES('5','���ݽṹ','7',4)
INSERT INTO Course VALUES('6','���ݴ���',NULL,2)
INSERT INTO Course VALUES('7','C����',6,4)
INSERT INTO Course VALUES('8','DB_Design',1,2)

UPDATE Course SET Cpno='8' WHERE Cno='1'	--�������޿ε�����

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

-- END �������ݿ��ļ�

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

SELECT  Sname, Sno, Ssex FROM  Student WHERE  Sname  LIKE  '��%';

SELECT  Sname, Sdept  FROM  Student WHERE  Sname  LIKE  '��___';

SELECT  Sname, Sage FROM  Student WHERE  Sname NOT LIKE '��%';

SELECT  Cno, Ccredit FROM  Course WHERE  Cname LIKE 'DB\_DESIGN' ESCAPE '\';

SELECT  * FROM  Course WHERE  Cname LIKE 'DB\_%DESIG_'ESCAPE'\';	-- ��ѯ��"DB_"��ͷ,�ҵ����ַ�Ϊ��DESIG(N)���Ŀγ�

SELECT  Sno, Cno FROM  SC WHERE  Grade IS NULL;
SELECT  Sno, Cno FROM  SC WHERE  Grade IS NOT NULL;

SELECT  Sno, Grade FROM SC WHERE  Cno='3' ORDER BY Grade DESC;
SELECT  * FROM  Student ORDER BY Sdept ASC, Sage DESC;

SELECT  COUNT(*) FROM  Student;
SELECT  COUNT(*) count_name FROM  Student;
SELECT  COUNT(DISTINCT Sno) FROM SC;

SELECT  AVG(Grade) FROM  SC WHERE  Cno='2';  --Ӧ����88.3333..��������int����ʱ����

SELECT  MAX(Grade) FROM  SC WHERE  Cno='2';

SELECT  SUM(Ccredit) FROM  SC,Course WHERE  Sno='201215122' AND SC.Cno=Course.Cno;

SELECT  Cno , COUNT(Sno) CntSno FROM  SC GROUP  BY Cno;

SELECT  Sno FROM  SC GROUP BY Sno HAVING  COUNT(Cno)>2;


--ENDʵ���