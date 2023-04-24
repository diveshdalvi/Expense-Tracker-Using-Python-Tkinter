import tkinter as tk
import mysql.connector
import datetime



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Divesh",
  database="transaction_manager"
)

# Variables
Label = tk.Label
Entry = tk.Entry
Radiobutton = tk.Radiobutton
Button = tk.Button
mycursor = mydb.cursor()
root = tk.Tk()
root.title("Expense Manager")
root.resizable(False,False)
cnv = tk.Canvas(root,width =900,height=700)
cnv.configure(bg='#CCF0F1')
cnv.pack()

def find_balance():
    global current_amount
    query_for_remaining_balance = ("SELECT SUM(amount) AS current_amount FROM transaction;")
    mycursor.execute(query_for_remaining_balance)
    balance_result = mycursor.fetchone()
    current_amount = balance_result[0]
    

#Functions
def save_transaction():
    name = t_name.get()
    amount = int(t_amount.get())
    transaction_type = t_type.get()
    now = datetime.datetime.now()
    time =  now.strftime('%Y-%m-%d')
    Query = "INSERT INTO transaction (name, amount, type, date) VALUES (%s, %s, %s, %s)"
    if (transaction_type == "Expense"):
        amount = amount * -1
    values = (name, amount, transaction_type, time)
    mycursor.execute(Query,values)
    mydb.commit()




def add_transaction():
    t_box_color = "white"
    global y
    name = t_name.get()
    amount = t_amount.get()
    transaction_type = t_type.get()
    now = datetime.datetime.now()
    time =  now.strftime('%Y-%m-%d')
  
    if(transaction_type == "Expense"):
        t_box_color = "#EBBDBD"
    elif(transaction_type == "Income"):
        t_box_color = "#D8EFBC"
    else:
        t_box_color ="grey"
    name_text = cnv.create_text(70, y+24, anchor="w", text=name, font=("Trebuchet", 23), fill="black")
    amount_text = cnv.create_text(470, y+20, anchor="w", text=f'₹{amount}', font=("Trebuchet", 22), fill="black")
    t_type_text_lbl = cnv.create_text(145, y+59, anchor="e", text=f"{transaction_type}", font=("Trebuchet", 17), fill="black")
    t_date_lbl = cnv.create_text(400, y+55, anchor="w", text=f"Date:{time}", font=("Trebuchet", 17), fill="black")


    transaction_rect = cnv.create_rectangle(50, y, 600, y+80, fill=t_box_color, outline="white")
    y+= 100

    cnv.lift(transaction_rect)
    cnv.lift(name_text)
    cnv.lift(amount_text)
    cnv.lift(t_type_text_lbl)
    cnv.lift(t_date_lbl)

    cnv.create_window(0, 0, anchor="nw",  width=270)

def transaction():
    save_transaction()
    add_transaction()
    find_balance()
find_balance()
# main widget of canvas
x1, y1 = 50, 40
x2, y2 = 850, 180
cnv.create_rectangle(x1,y1,x2,y2,fill="white",outline="")

#current balance text and amount text
#text
current_balance_txt_lbl = Label(text="Current Balance",bg='white',font=('futura',25))
current_balance_txt_lbl.place(x=80,y=55)
#balance

current_balance_lbl = Label(text=f"{current_amount}",bg='white',font=('Arial',21))
current_balance_lbl.place(x=175,y=110)

#expense text and expense balance text
#text
expense_text_lbl = Label(text="Expense",bg="white",font=("Arial",22,"bold"),fg="red")
expense_text_lbl.place(x=500,y=60)
#balance
expense_lbl = Label(text="₹20",bg='white',font=('Arial',21))
expense_lbl.place(x=536,y=105)


#income text and income balance text
#text
income_text_lbl = Label(text="Income",bg="white",font=("Arial",22,"bold"),fg="green")
income_text_lbl.place(x=680,y=60)
#balance
income_lbl = Label(text="₹50",bg='white',font=('Arial',21))
income_lbl.place(x=706,y=105)

# Data Entries 

#Transaction Name 
t_name_text = Label(text="Name",bg="#CCF0F1",font=("Verdana",19))
t_name_text.place(x=625,y=230)
t_name = Entry(root,bg="white",font=("arial",15),width=18)
t_name.place(x=625,y=265)

#Transaction Amount
t_amount_text = Label(text="Amount",bg="#CCF0F1",font=("Verdana",19))
t_amount_text.place(x=625,y=340)
t_amount = Entry(root,bg="white",font=("arial",15),width=18)
t_amount.place(x=625,y=375)

#Radio Button To change its An expense or an Income
t_type_text = Label(text="Select Transaction Type",bg="#CCF0F1",font=("Verdana",16))
t_type_text.place(x=620,y=450)
t_type = tk.StringVar()
income_btn = Radiobutton(root,text="Income",variable = t_type,value="Income",font=("Arial",18),bg="#CCF0F1")
expense_btn = Radiobutton(root,text="Expense",variable = t_type,value="Expense",font=("Arial",18),bg="#CCF0F1")
income_btn.place(x=625,y=500)
expense_btn.place(x= 740,y=500)

y = 230
#Add button
add_btn = Button(text="Add",bg="#38B6FF",fg="white",width=10,font=("Arial",30,"bold"),command=transaction)
add_btn.place(x=625,y=600)



root.mainloop()
