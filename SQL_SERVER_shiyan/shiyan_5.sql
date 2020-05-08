use xskc

CREATE VIEW C_Student AS SELECT Sno,Sname,Sage,Sdept FROM Student WHERE Sdept='MA' WITH CHECK OPTION;

CREATE VIEW Student_CR AS SELECT Student.Sno,Sname,Cname,Grade FROM Student,Course,SC WHERE Student.Sno=SC.Sno AND SC.Cno=Course.Cno

CREATE VIEW Student_birth(Sno,Sname,Sbirth) AS SELECT Sno,Sname,2018-Sage FROM Student
SELECT * FROM Student_birth


SELECT * FROM Student WHERE Sdept='MA'
SELECT * FROM C_Student
SELECT Sname,Sage FROM C_Student WHERE Sage <20
SELECT Sname,Sage FROM Student WHERE Sdept='MA' AND Sage<20

SELECT * FROM Student_CR
SELECT Sno,Sname,Cname FROM Student_CR WHERE Grade>85

UPDATE C_Student SET Sname='黄海' WHERE Sno='201215153'

INSERT INTO C_Student VALUES('200215124','王海',20,'MA')

SELECT * FROM C_Student
SELECT * FROM Student

DELETE FROM C_Student WHERE Sno='200215124'


--END实验五

