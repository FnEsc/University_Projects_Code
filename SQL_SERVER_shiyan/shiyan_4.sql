use xskc

INSERT INTO Student(Sno,Sname,Ssex,Sdept,Sage) VALUES('200215128','�¶�','��','IS',18);
INSERT INTO Student VALUES('200215129','�¶�','��',18,'IS');

INSERT INTO SC(Sno,Cno) VALUES('200215128','1');

UPDATE Student SET  Sage=31 WHERE Sno='200215129'
SELECT * FROM Student

UPDATE Student SET Sage = Sage+1

UPDATE SC SET Grade=0 WHERE 'CS' = (SELECT Sdept FROM Student WHERE Student.Sno=SC.Sno)
DELETE FROM SC WHERE Sno='200215128'
DELETE FROM Student WHERE Sno='200215128'

SELECT * FROM Student
SELECT * FROM SC

DELETE FROM SC

DELETE FROM SC WHERE 'CS'=(SELECT Sdept FROM Student WHERE Student.Sno=SC.Sno)  --ɾ���������ѧϵ����ѧ����ѡ�μ�¼

CREATE TABLE History_Student(
	Sno CHAR(9) PRIMARY KEY,
	Sname CHAR(8) NOT NULL,
	Ssex CHAR(2) DEFAULT '��' CHECK(Ssex in ('��','Ů')),
	Sage INT,
	Sdept CHAR(20)
);
INSERT INTO  History_Student SELECT  * FROM  Student;
SELECT * FROM History_Student

--ENDʵ��