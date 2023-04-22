from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = "Divesh",
    database = "tasks"
)
mycursor = mydb.cursor()
def add_task():
    task_name = task_name_tb.get()
    task_description = task_description_tb.get()
    query = "INSERT INTO task_list (task, description) VALUES (%s, %s)"
    value = (task_name, task_description)
    mycursor.execute(query,value)
    mydb.commit()
    task_list.insert(END,task_name)

def update_task():
    task_name = task_name_tb.get()
    task_description = task_description_tb.get()
    query = "UPDATE task_list SET description = %s where task = %s"
    value = (task_description,task_name)
    mycursor.execute(query,value)
    mydb.commit()
    task_list.delete(ACTIVE)
    task_list.insert(ACTIVE,task_name)

def delete_task():
    task_name = task_name_tb.get()
    query = "DELETE FROM task_list WHERE task = %s"
    value = (task_name,)
    mycursor.execute(query,value)
    mydb.commit()
    task_list.delete(ACTIVE)




root = Tk()
root.title("Task Manager")
root.geometry("800x700")
task_label = Label(root,text="Task: " ,font=("Helvetica", 14))
task_label.configure(fg="blue", bg="yellow")
task_label.place(x =10,y=10)

root.mainloop()