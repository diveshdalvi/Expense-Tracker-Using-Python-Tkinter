import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import font
import tkinter.ttk as ttk

mydb = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = "Divesh",
    database = "tasks"
)
mycursor = mydb.cursor()
def add_task():
    task_name = task_name_tb.get()
    task_desc = task_desc_tb.get()
    query = "INSERT INTO task_list (task, description) VALUES (%s, %s)"
    value = (task_name, task_desc)
    mycursor.execute(query,value)
    mydb.commit()
    task_box.insert(parent="",index="end",text="",values=(value))
    task_name_tb.delete(0, END)
    task_desc_tb.delete(0, END)

def update_task():
    current_item = task_box.focus()
    new_task = task_name_tb.get()
    new_description = task_desc_tb.get()
    mycursor = mydb.cursor()
    sql = "UPDATE task_list SET task = %s, description = %s WHERE task = %s"
    val = (new_task, new_description, task_box.item(current_item)['text'])
    mycursor.execute(sql, val)
    mydb.commit()
    task_box.item(current_item, text=new_task, values=(new_description,))
    task_name_tb.delete(0, END)
    task_desc_tb.delete(0, END)

def delete_task():
    current_item = task_box.focus()
    task_to_delete = task_box.item(current_item)['text']
    mycursor = mydb.cursor()
    sql = "DELETE FROM task_list WHERE task = %s"
    val = (task_to_delete,)
    mycursor.execute(sql, val)
    mydb.commit()
    task_box.delete(current_item)
    task_name_tb.delete(0, END)
    task_desc_tb.delete(0, END)




root = tk.Tk()
root.title("Task Manager")
root.geometry("900x600")
root.resizable(False, False)
root.configure(bg="#E1E3E8")

Label = tk.Label
Button = tk.Button
Listbox = tk.Listbox
Entry = tk.Entry
# font = tk.font

task_lbl = Label(root, text= "Task Manager",font=("Helvetica", 25, "italic"),bg="#E1E3E8")
task_lbl.place(x=365,y=10)


task_btn = Button(root, text="Add Task", bg="white", fg="black", font=("Trebuchet", 13), width=8, height=2 ,relief="flat" ,borderwidth=1 , command=add_task)
task_btn.place(x=200,y=200)


task_name_lbl = Label(root,text = "Task Name: ",font= ("Helvetica", 12, "italic"),bg="#E1E3E8")
task_name_lbl.place(x=20, y=95)
task_name_tb = Entry(root)
task_name_tb.place(x=170, y=100)


task_desc_lbl = Label(root,text = "Task Description: ",font= ("Helvetica", 12, "italic"),bg="#E1E3E8")
task_desc_lbl.place(x=20, y=140)
task_desc_tb = Entry(root)
task_desc_tb.place(x=170, y=145)


task_box = ttk.Treeview(root, columns=("Name" , "Description"), selectmode="browse")
task_box.column("#0",width=0,stretch=NO)
task_box.column("Name",anchor=CENTER,width=80)
task_box.column("Description",anchor=CENTER,width=80)
task_box.heading("#0",text="",anchor=CENTER)
task_box.heading("Name",text="Name",anchor=CENTER)
task_box.heading("Description",text="Description",anchor=CENTER)
task_box.place(x= 20,y=300)
mycursor.execute("SELECT * FROM task_list")
myresult = mycursor.fetchall()
for task in myresult:
    task_box.insert("", "end", values=(task[1],task[2]))

root.mainloop()