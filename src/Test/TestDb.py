# 导入pymysql模块
import pymysql

# 连接database
conn = pymysql.connect(host="localhost", user="root",password="076523",database="cameraeffects")
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
lkk = "'lkk'"
sql = "select password from user where username = " + lkk
print(sql)
try:
    cursor.execute(sql)  # 执行sql语句

    results = cursor.fetchall()  # 获取查询的所有记录
    print( "name", "password","phone")
    password = 0
    # 遍历结果
    for row in results:
        password = row[0]

    print(password)
except Exception as e:
    raise e
finally:
    conn.close()  # 关闭连接