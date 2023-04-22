from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = "Divesh",
    database = "tasks"
)
mycursor = mydb.cursor()

root = Tk()
#Enter Task In database
# sql = "INSERT INTO task_list (task, description) VALUES (%s, %s)"
# val = ("Task 1", "This is task 1")
# mycursor.execute(sql, val)
# mydb.commit()

# to retrieve data from database
# mycursor.execute("SELECT * FROM task_list")
# myresult = mycursor.fetchall()
# for task in myresult:
#     print(task)

