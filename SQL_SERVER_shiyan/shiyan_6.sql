-- 实验六

-- use xskc;

CREATE TRIGGER tri1 ON Student 
FOR INSERT 
AS
	IF(SELECT Sage FROM INSERTED)>25 OR (SELECT Sage FROM INSERTED)<16 
		BEGIN
			PRINT '年龄应在16~25之间'
			ROLLBACK
		END;


DELETE FROM Student WHERE Sno='200231001'
INSERT INTO Student VALUES('200231001','王涛','男',30,'IS');

CREATE TRIGGER tri2 ON SC
FOR UPDATE
AS 
	IF NOT EXISTS (SELECT * FROM INSERTED WHERE Grade BETWEEN 0 AND 100)
		BEGIN
			PRINT '成绩应该在0~100之间'
			ROLLBACK
		END

UPDATE SC SET Grade=120 WHERE Sno='200215122'

CREATE TRIGGER tri3 ON Student
FOR DELETE
AS
	DELETE FROM SC WHERE Sno IN (SELECT Sno FROM DELETED)
	DELETE FROM Student WHERE Sno in (SELECT Sno FROM DELETED)

DELETE Student WHERE Sno='201215122'
SELECT * FROM Student


CREATE PROCEDURE pro1  --创建一个进程
AS
	SELECT * FROM Student
EXEC pro1  --调用进程


CREATE PROCEDURE pro2
@xh char(9),@kch char(4)
AS
	SELECT * FROM SC
	WHERE Sno=@xh AND Cno=@kch
EXEC pro2 201215121,1  --调用进程
SELECT * FROM SC

CREATE PROCEDURE pro3
@xh char(9)
AS
	SELECT * FROM Student WHERE Sno=@xh
EXEC pro3 201215121		--调用进程


CREATE PROCEDURE pro4
@kch char(4),@xf int
AS
	UPDATE Course
	SET Ccredit=@xf
	WHERE Cno=@kch
EXEC pro4 1,10			 --调用进程


CREATE PROCEDURE pro
@xh char(9)
AS
	DECLARE @pjf int
	SELECT @pjf=AVG(Grade)
	FROM SC
	WHERE Sno=@xh
RETURN @pjf


SELECT * FROM SC

declare @pjcj int
exec @pjcj=pro 201215122
print 'pjcj='+cast(@pjcj as char(10))


CREATE PROCEDURE pro6
@xh char(9),@pjf int output
AS
	SELECT @pjf=AVG(Grade)
	FROM SC
	WHERE Sno=@xh

DECLARE @pjcj int
EXEC pro6 201215122,@pjcj output
SELECT @pjcj

-- END





