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

def insert_task(new, u):
    sql = "insert into todo (task, urgent) value (%s, %s)"
    connection = pymysql.connect(user="root", password="", host="localhost", database="task")
    cursor = connection.cursor()
    cursor.execute(sql, (new,u))
    connection.commit()
    cursor.close()
    connection.close()
    return

def remove_task(id):
    sql = "delete from todo where id = (%s)"
    connection = pymysql.connect(user="root", password="", host="localhost", database="task")
    cursor = connection.cursor()
    cursor.execute(sql, (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return
