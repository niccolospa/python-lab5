import pymysql

def update_tasks():
    sql = "select id,task from todo"
    connection = pymysql.connect(user="root", password="", host="localhost", database="task")
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    cursor.close()
    connection.close()
    tasks = dict((x, y) for x, y in result)
    return tasks
