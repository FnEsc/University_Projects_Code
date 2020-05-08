-- ʵ��һ��

-- �ȴ����ļ��д������
CREATE DATABASE xskc
	on (name=xsks_data,filename='F:\SQL_SERVER\sjksy\xskc_data.mdf')
	log on (name=xskc_log,filename='F:\SQL_SERVER\sjksy\xskc_log.ldf');

--�����ļ���Ϊ�½�һ�����ݿ�
EXEC  sp_attach_db  @dbname  =  'xskc',
@filename1  =  'F:\SQL_SERVER\sjksy\xskc_data.mdf',
@filename2  =  'F:\SQL_SERVER\sjksy\xskc_log.ldf'
--END����

USE xskc;

CREATE TABLE Student(
	Sno CHAR(9) PRIMARY KEY,
	Sname CHAR(8) NOT NULL,
	Ssex CHAR(2) DEFAULT '��' CHECK(Ssex in ('��','Ů')),
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

-- DROP  TABLE Student CASCADE; -- ע�ͣ�SQL Server ����ɾ��ʧ��
-- CREATE CLUSTERED INDEX Stu_Sname ON Student(Sage); -- ע�ͣ�CLUSTERED�۴��������޷���ͬ�����Ͻ�������۴�����
-- DROP INDEX PK__Student__CA1FE4647F60ED59 ON Student; -- ע�ͣ������������ 'Student.PK__Student__CA1FE4647F60ED59' ��ʽ��ʹ�� DROP INDEX�������������� PRIMARY KEY Լ����ǿ��ִ�С�
-- ALTER TABLE Student ALTER COLUMN Sno char(9) not null; -- ע�ͣ�ɾ������ʧ��

CREATE UNIQUE INDEX Stu_Sno ON Student(Sno);

CREATE UNIQUE INDEX Cou_Cno ON Course(Cno);

CREATE UNIQUE INDEX SCno ON SC(Sno ASC,Cno DESC);

-- DROP INDEX Stu_Sname ON Student; -- ע�ͣ�����û�����۴�����

-- END ʵ��һ
