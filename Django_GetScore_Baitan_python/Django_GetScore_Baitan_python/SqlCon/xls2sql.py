import xlrd

data = xlrd.open_workbook('qa_(15).xls')  # 请在这里修改需要导入的xls文件，注意不要表头，此处所有关目一起用
table = data.sheets()[0]

sql_file = '''
set names utf8;
set names utf8;
SET FOREIGN_KEY_CHECKS = 0;

drop table IF exists bt_problems_sy;
create table bt_problems_sy (
  id int AUTO_INCREMENT,
  title varchar(100),
  options varchar(200),
  flag varchar(10),
  primary key (id)
);

drop table IF exists bt_record;
create table bt_record (
  id int AUTO_INCREMENT,
  award int not null,
  win_date datetime default '2018-09-28 00:00:00',
  primary key (id)
);
'''

# all_data = []
for i in range(table.nrows):  # 从0行开始
    # all_data.append(table.row_values(i))    # index, flag, title, options
    if i == 0:
        sql_file += 'insert into bt_problems_sy(title, options, flag)\n'
        sql_file += 'select \'{0}\',\'{1}\',\'{2}\''.format(table.row_values(i)[2],
                                                     table.row_values(i)[3],
                                                     table.row_values(i)[1])
    else:
        sql_file += '\nunion all select '
        sql_file += '\'{0}\',\'{1}\',\'{2}\'' \
            .format(table.row_values(i)[2],
                    table.row_values(i)[3].replace('B.', '<br>B.').replace('C.', '<br>C.').replace('D.', '<br>D.'),
                    table.row_values(i)[1])
sql_file += '\n;'

# print(sql_file)
with open('sql_python.sql', 'w', encoding='utf-8') as f:
    f.write(sql_file)