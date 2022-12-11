from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import gamedb
import datetime as dt

db = gamedb("players.db")

root = Tk()
root.title("Player Editor")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

username, password, nickname, gender, email, confirmationcode, confirmationdate, regdate, linkdate, date = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), dt.datetime.now()
format_date=f"{date:%a, %b %d %Y}"

entries_frame, title = Frame(root, bg="#535c68"), Label(entries_frame, text="Player Management System", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
entries_frame.pack(side=TOP, fill=X)
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

lblUserName, txtUserName = Label(entries_frame, text="Username", font=("Calibri", 16), bg="#535c68", fg="white"), Entry(entries_frame, textvariable=username, font=("Calibri", 16), width=30)
lblUserName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtUserName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblPassword, txtPassword = Label(entries_frame, text="Password", font=("Calibri", 16), bg="#535c68", fg="white"), Entry(entries_frame, textvariable=password, font=("Calibri", 16), width=30)
lblPassword.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtPassword.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lblNickname, txtNickname = Label(entries_frame, text="Nickname", font=("Calibri", 16), bg="#535c68", fg="white"), Entry(entries_frame, textvariable=nickname, font=("Calibri", 16), width=30)
lblNickname.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtNickname.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblEmail, txtEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white"), Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblGender, comboGender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white"), ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female")
lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
comboGender.grid(row=3, column=1, padx=10, sticky="w")

lblConfirmationCode, txtConfirmationCode = Label(entries_frame, text="Confirmation Code", font=("Calibri", 16), bg="#535c68", fg="white"), Entry(entries_frame, textvariable=confirmationcode, font=("Calibri", 16), width=30)
lblConfirmationCode.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtConfirmationCode.grid(row=3, column=3, padx=10, sticky="w")

lblConfirmationDate, txtConfirmationDate = Label(entries_frame, text="Confirmation Date", font=("Calibri", 16), bg="#535c68", fg="white"), Entry(entries_frame, textvariable=format_date, font=("Calibri", 16), width=30)
lblConfirmationDate.grid(row=4, column=0, padx=10, pady=10, sticky="w")
txtConfirmationDate.grid(row=4, column=1, padx=10, sticky="w")

lblRegDate, txtRegDate = Label(entries_frame, text="Reg Date", font=("Calibri", 16), bg="#535c68", fg="white"), Entry(entries_frame, textvariable=format_date, font=("Calibri", 16), width=30)
lblRegDate.grid(row=4, column=2, padx=10, pady=10, sticky="w")
txtRegDate.grid(row=4, column=3, padx=10, sticky="w")

lblLinkDate, txtLinkDate = Label(entries_frame, text="Link Date", font=("Calibri", 16), bg="#535c68", fg="white"), Entry(entries_frame, textvariable=format_date, font=("Calibri", 16), width=30)
lblLinkDate.grid(row=5, column=0, padx=10, pady=10, sticky="w")
txtLinkDate.grid(row=5, column=1, padx=10, sticky="w")


def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    username.set(row[1])
    password.set(row[2])
    nickname.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    confirmationcode.set(row[6])
    confirmationdate.set(row[7])
    regdate.set(row[8])
    linkdate.set(row[9])

def showAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)

def add_player():
    if txtUserName.get() == "" or txtPassword.get() == "" or txtNickname.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtConfirmationCode.get() == "" or txtConfirmationDate.get() == "" or txtRegDate.get() == "" or txtLinkDate.get() == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(txtUserName.get(),txtPassword.get(), txtNickname.get() , txtEmail.get() ,comboGender.get(), txtConfirmationCode.get(), txtConfirmationDate.get(), txtRegDate.get(), txtConfirmationDate.get())
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    showAll()

def update_player():
    if txtUserName.get() == "" or txtPassword.get() == "" or txtNickname.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtConfirmationCode.get() == "":
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return
    db.update(row[0],txtUserName.get(),txtPassword.get(), txtNickname.get() , txtEmail.get() ,comboGender.get(), txtConfirmationCode.get(), txtConfirmationDate.get(), txtRegDate.get(), txtConfirmationDate.get())
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    showAll()


def delete_player():
    db.remove(row[0])
    clearAll()
    showAll()

def clearAll():
    username.set("")
    password.set("")
    nickname.set("")
    email.set("")
    gender.set("")
    confirmationcode.set("")
    confirmationdate.set("")
    regdate.set("")

btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")

btnAdd = Button(btn_frame, command=add_player, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_player, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_player, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)

tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1980, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18), rowheight=50) 
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18)) 
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=5)
tv.heading("2", text="Username")
tv.column("2", width=5)
tv.heading("3", text="Password")
tv.column("3", width=5)
tv.heading("4", text="Nickname")
tv.column("4", width=5)
tv.heading("5", text="Email")
tv.column("5", width=5)
tv.heading("6", text="Gender")
tv.column("6", width=5)
tv.heading("7", text="Confirmation Code")
tv.column("7", width=5)
tv.heading("8", text="Confirmation Date")
tv.column("8", width=5)
tv.heading("9", text="Reg Date")
tv.column("9", width=5)
tv.heading("10", text="Link Date")
tv.column("10", width=5)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

showAll()
root.mainloop()
