import tkinter as tk
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




root = tk.Tk()
root.title("Task Manager")
root.geometry("900x600")
root.resizable(False, False)
root.configure(bg="#E1E3E8")

Label = tk.Label
Button = tk.Button
Listbox = tk.Listbox
Entry = tk.Entry


task_lbl = Label(root, text= "Task Manager",font=("Helvetica", 25, "italic"),bg="#E1E3E8")
task_lbl.place(x=365,y=10)


task_btn = Button(root, text="Add Task", bg="white", fg="black", font=("Trebuchet", 13), width=8, height=2 ,relief="flat" ,borderwidth=1)
task_btn.place(x=700,y=200)


task_name_lbl = Label(root,text = "Enter Task Name: ",font= ("Helvetica", 12, "italic"),bg="#E1E3E8")
task_name_lbl.place(x=590, y=95)
task_name_tb = Entry(root)
task_name_tb.place(x=750, y=100)


task_desc_lbl = Label(root,text = "Enter Task Description: ",font= ("Helvetica", 12, "italic"),bg="#E1E3E8")
task_desc_lbl.place(x=570, y=140)
task_desc_tb = Entry(root)
task_desc_tb.place(x=750, y=145)




root.mainloop()