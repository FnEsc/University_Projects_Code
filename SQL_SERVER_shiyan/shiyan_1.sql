-- 实验一：

-- 先创建文件夹存放数据
CREATE DATABASE xskc
	on (name=xsks_data,filename='F:\SQL_SERVER\sjksy\xskc_data.mdf')
	log on (name=xskc_log,filename='F:\SQL_SERVER\sjksy\xskc_log.ldf');

--导入文件成为新建一个数据库
EXEC  sp_attach_db  @dbname  =  'xskc',
@filename1  =  'F:\SQL_SERVER\sjksy\xskc_data.mdf',
@filename2  =  'F:\SQL_SERVER\sjksy\xskc_log.ldf'
--END导入

USE xskc;

CREATE TABLE Student(
	Sno CHAR(9) PRIMARY KEY,
	Sname CHAR(8) NOT NULL,
	Ssex CHAR(2) DEFAULT '男' CHECK(Ssex in ('男','女')),
	Sage INT,
	Sdept CHAR(20)
);
	
CREATE TABLE Course(
	Cno CHAR(4) PRIMARY KEY,
	Cname CHAR(40) NOT NULL,
	Cpno CHAR(4),
	Ccredit INT,
	FOREIGN KEY(Cpno) REFERENCES Course(Cno)
);

CREATE TABLE SC(
	Sno CHAR(9),
	Cno CHAR(4),
	Grade INT,
	PRIMARY KEY(Sno,Cno),
	FOREIGN KEY(Sno) REFERENCES Student(Sno),
	FOREIGN KEY(Cno) REFERENCES Course(Cno)
);

ALTER TABLE Student ADD S_entrance DATETIME;

ALTER TABLE Student ALTER COLUMN Sage SMALLINT;

ALTER TABLE Course ADD UNIQUE(Cname);

ALTER TABLE Student ALTER COLUMN Sdept CHAR(20) NOT NULL;

ALTER TABLE Student DROP COLUMN S_entrance;

-- DROP  TABLE Student CASCADE; -- 注释：SQL Server 级联删除失败
-- CREATE CLUSTERED INDEX Stu_Sname ON Student(Sage); -- 注释：CLUSTERED聚簇索引，无法在同个表上建立多个聚簇索引
-- DROP INDEX PK__Student__CA1FE4647F60ED59 ON Student; -- 注释：不允许对索引 'Student.PK__Student__CA1FE4647F60ED59' 显式地使用 DROP INDEX。该索引正用于 PRIMARY KEY 约束的强制执行。
-- ALTER TABLE Student ALTER COLUMN Sno char(9) not null; -- 注释：删除主键失败

CREATE UNIQUE INDEX Stu_Sno ON Student(Sno);

CREATE UNIQUE INDEX Cou_Cno ON Course(Cno);

CREATE UNIQUE INDEX SCno ON SC(Sno ASC,Cno DESC);

-- DROP INDEX Stu_Sname ON Student; -- 注释：上面没建立聚簇索引

-- END 实验一
