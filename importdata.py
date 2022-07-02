
from pymysql import connect
import csv
#  建立链接
conn = connect(host='localhost', port=3306, db='movierec', user='root', password='123456', charset='utf8')
# 获取游标
cur = conn.cursor()
# 打开文件，读取所有文件存成列表
with open('./data/刘澎的movie11.csv', 'r', encoding='gb18030') as f:
    rete = csv.reader(f)
    for x in rete:
        print(x)
        #sql语句
        sql = "insert into movie_TABLE values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        print(sql)
        # 参数化方式传参
        row_count = cur.execute(sql, [int(x[0]), x[2], x[12], x[4], x[7], x[8], x[9]
                                      ,x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17]])
        # 显示操作结果
        print("SQL语句影响的行数为%d" % row_count)
# 统一提交
conn.commit()
# 关闭游标　
cur.close()
# 关闭连接
conn.close()