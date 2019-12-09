import sqlite3
from tkinter import *
from tkinter import scrolledtext
from time import strftime 
from tkinter import messagebox

root = Tk() 
root.title("Project 3")

conn = sqlite3.connect('OrgDB.db')

conn.execute('''CREATE TABLE IF NOT EXISTS Employees
             (EmployeeNumber INT PRIMARY KEY NOT NULL,
             EmployeeName TEXT NOT NULL,
             EmployeeGender TEXT NOT NULL,
             EmployeeNationality TEXT NOT NULL,
             EmployeeDateofBirth TEXT NOT NULL,
             EmployeeAddress TEXT NOT NULL,
             EmployeeDepartment TEXT NOT NULL,
             EmployeeSalary REAL)''')

def addEmp():
    newEmp = (
            eNumber.get(),
            eName.get(),
            eGender.get(),
            eNty.get(),
            eDob.get(),
            eAddress.get(),
            eDpt.get(),
            eSalary.get())
    c = conn.cursor()    
    c.execute("INSERT INTO Employees VALUES (?,?,?,?,?,?,?,?)",newEmp)
    conn.commit()    
    print ("EMPLOYEE ADDED :",newEmp)
    messagebox.showinfo("Add Employee", "Employee Added Seccussfully")

eNumber = IntVar()
eName = StringVar()
eGender = StringVar()
eNty = StringVar()
eDob = StringVar()
eAddress = StringVar()
eDpt = StringVar()
eSalary = IntVar()

def CreateEmp():
    c = Toplevel(root)
    c.title("Create Employee")
    c.geometry('400x300')
    
    EmployeeNumber=Label(c,text="EmployeeNumber").grid(row=0,column=0)
    Entry(c,textvariable=eNumber).grid(row=0,column=1)
    
    EmployeeName=Label(c,text="EmployeeName").grid(row=1,column=0)
    Entry(c,textvariable=eName).grid(row=1,column=1)
    
    EmployeeNationality=Label(c,text="EmployeeNationality").grid(row=2,column=0)
    Entry(c,textvariable=eNty).grid(row=2,column=1)
    
    EmployeeDateofBirth=Label(c,text="EmployeeDateofBirth").grid(row=3,column=0)
    Entry(c,textvariable=eDob).grid(row=3,column=1)
    
    EmployeeAddress=Label(c,text="EmployeeAddress").grid(row=4,column=0)
    Entry(c,textvariable=eAddress).grid(row=4,column=1)
    
    EmployeeDepartment=Label(c,text="EmployeeDepartment").grid(row=5,column=0)
    Entry(c,textvariable=eDpt).grid(row=5,column=1)
    
    EmployeeSalary=Label(c,text="EmployeeSalary").grid(row=6,column=0)
    Entry(c,textvariable=eSalary).grid(row=6,column=1)
    
    def male():
        eGender.set("Male")
    rad1 = Radiobutton(c,text='Male', value="male", command=male).grid(row=7,column=0)
    
    def female():
        eGender.set("Female")
    rad2 = Radiobutton(c,text='Female', value="female", command=female).grid(row=7,column=1)
    
    submit=Button(c,text="save",command = addEmp ).grid(row=8,column=0)
    delete=Button(c,text="cancel",command = c.destroy).grid(row=8,column=1)
    
def ShowData():
    c = Toplevel(root)
    c.title("Show Employees Data")
    c.geometry("400x250")
    txt = scrolledtext.ScrolledText(c,width=40,height=10)
    mylist = Listbox(c)
    c=conn.cursor()
    c.execute("SELECT * FROM Employees")
    for row in c:
        mylist.insert(END, row)
    mylist.pack( fill = BOTH )
    txt.grid(column=0,row=0)

    
def deleteEmp():
    empNumber = IntVar()
    cc = Toplevel(root)
    cc.title("delete Employee")
    cc.geometry("400x250")
    EmployeeNumber=Label(cc,text="Employee Number").grid(row=0,column=0)
    Entry(cc,textvariable=empNumber).grid(row=0,column=1)
    print(empNumber.get())
    def conDelete():
        c = conn.cursor()
        c.execute("DELETE FROM Employees WHERE EmployeeNumber = %s " %empNumber.get())
        print(empNumber.get())
        messagebox.showinfo("Delete Employee", "Employee Deleted Seccussfully")
        cc.destroy()
    delete = Button(cc,text= "Delete",command = conDelete ).grid(row=2,column=2)

def Info():
    messagebox.showinfo("PROJECT 3", " PROJECT 3\n CREATED BY HANI")

def Report():
    messagebox.showwarning("Report", "Report A Problem")
    
menubar = Menu(root)
    
file = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file) 
file.add_command(label ='Report', command = Report) 
file.add_separator() 
file.add_command(label ='Exit', command = root.destroy)   

employee = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Employees', menu = employee) 
employee.add_command(label ='Add', command = CreateEmp) 
employee.add_command(label ='View', command = ShowData) 


Delete = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Delete', menu = Delete) 
Delete.add_command(label ='Delete', command = deleteEmp) 

help_ = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Help', menu = help_) 
help_.add_command(label ='About', command = Info) 

root.config(menu = menubar) 
root.geometry("800x600")
mainloop() 