## 数据库配置方法

MySQL 建立一个数据库，例如 baitan_python

$ create database baitan_python;

选择数据库之后，导入sql文件，文件的路径用了xxx代替

$ use baitan_python;
$ source /xxx/xxx/sql.sql

在 connection.py 中，配置好 MySQL 的用户、密码、数据库名，就可以用了。