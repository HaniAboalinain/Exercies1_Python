"""

    Done by : 
            HANI ABU-ALINAIN
            MOHAMMAD ALAA-ALDEEN
            RAHMA SANDOQA

"""

from tkinter import *
from tkinter import scrolledtext as st
from functools import reduce
import json
from tkinter import messagebox


class Person:

    def __init__(self, name, address):
        self._name = name
        self._address = address
 
    def getName(self):
        return self._name

    def setName(self, newName):
        self._name = newName

    def getAddress(self):
        return self._address

    def setAddress(self, newAdress):
        self._address = newAdress

    def __del__(self):
        print("I have been deleted")


class Employee(Person):

    def __init__(self, name, address, employeeNumber, salary, jobTitle, loans):
        super().__init__(name, address)
        self.employeeNumber = int(employeeNumber)
        self.__salary = float(salary)
        self.__jobTitle = jobTitle
        self.__loans = list(loans)

    def getSalary(self):
        return self.__salary

    def setSalary(self, newSalary):
        self.__salary = newSalary

    def getJobTitle(self):
        return self.__jobTitle

    def setJobTitle(self, newJobTitle):
        self.__jobTitle = newJobTitle

    def getLoans(self):
        return self.__loans

    def setLoans(self, newLoans):
        self.__loans = newLoans

    def getMaxLoan(self):
        if self.__loans:
            max = float(reduce(lambda x, y: x if x > y else y, self.__loans))
            return max

    def getMinLoan(self):
        if self.__loans:
            min = float(reduce(lambda x, y: x if x < y else y, self.__loans))
            return min

    def getEmployeeInfo(self):
        return (
            "\n Employee Information",
            "\n\t 1- Employee Name : " + self.getName(),
            "\n\t 2- Employee Address : " + self.getAddress(),
            "\n\t 3- Employee Number : " + str(self.employeeNumber),
            "\n\t 4- Salary : " + str(self.getSalary()),
            "\n\t 5- Job Title " + self.getJobTitle(),
            "\n\t 6- Loans : ", self.getLoans()
        )

    def low_high(self):
        low = 0
        high = 0

        if self.__loans:
            low = reduce(lambda a, b: a if a < b else b, self.__loans)
            high = reduce(lambda a, b: a if a > b else b, self.__loans)

        return (low, high)

    def __del__(self):
        print("I have been deleted")


class Student(Person):
    def __init__(self, name, address, studentNumber, subject, marks):
        super().__init__(name, address)

        self.studentNumber = int(studentNumber)
        self.__subject = subject
        self.__marks = marks

    def getSubject(self):
        return self.__subject

    def setSubject(self, newSubject):
        self.__subject = newSubject

    def getMarks(self):
        return self.__marks

    def setMarks(self, newMarks):
        self.__marks = newMarks

    def getAverage(self):
        sum = 0
        for x, y in self.__marks.items():
            sum += y

        average = sum / len(self.__marks)
        return average

    def getAMarks(self):
        n = 0
        for x, y in self.__marks.items():
            if y >= 90:
                n += 1
        return n

    def getStudentInfo(self):
        return (
            "\n Student Information",
            "\n\t 1- Studen Name : " + self.getName(),
            "\n\t 2- Student Address : " + self.getAddress(),
            "\n\t 3- Student Number : " + str(self.studentNumber),
            "\n\t 4- Subject : " + self.getSubject(),
            "\n\t 5- Student Marks : ", self.getMarks(),
            "\n\t 6- Average : ", self.getAverage()
        )

    def __del__(self):
        print("I have been deleted")


Employee1 = Employee("Ahmad Yazan", "Amman,Jordan", 1000,
                     500.0, "HR Consultan", [434, 200, 1020])
Employee2 = Employee("Hala Rana", "Aqaba,Jordan", 2000,
                     750.0, "Department Manager", [150, 3000, 250])
Employee3 = Employee("Maram Ali", "Mafraq,Jordan", 3000,
                     600.0, "HR S Consultan", [304, 1000, 250, 300, 500, 235])
Employee4 = Employee("Yasmeen Mohammad", "Karak,Jordan",
                     4000.0, 865, "Director", [])


Student1 = Student("Khalid Ali", "Irbid, Jordan", 20191000, "History", {
                   'English': 80, 'Arabic': 90, 'Art': 95, 'Managment': 75})
Student2 = Student("Reem Hani", "Zarqa, Jordan", 20182000, "Software Eng", {
                   'English': 80, 'Arabic': 90, 'Managment': 75, 'Calculas': 85, 'OS': 73, 'Programming': 90})
Student3 = Student("Nawras Abdullah", "Amman, Jordan", 20161001, "Arts", {
                   'English': 83, 'Arabic': 92, 'Art': 90, 'Managment': 70})
Student4 = Student("Amal Raed", "Tafelah, Jordan", 20172030, "Computer Eng", {
                   'English': 83, 'Arabic': 82, 'Managment': 70, 'Calculas': 80, 'OS': 79, 'Programming': 81})

EmployeesList = [Employee1, Employee2, Employee3, Employee4]
StudentsList = [Student1, Student2, Student3, Student4]


# ======================================================
#                     Report function
# ======================================================


def reportWindow():
    reportWin = Toplevel(root)
    reportWin.title("Report")

    scroll = st.ScrolledText(reportWin, width=50, height=10)
    scroll.grid(column=0, row=0)
#name, address, employeeNumber, salary, jobTitle, loans
    for i in range(len(EmployeesList)):
        scroll.insert(INSERT,  EmployeesList[i].getEmployeeInfo())

    scroll.insert(INSERT, "\n\n\n\n\n" , "========================================================")

    for i in range(len(StudentsList)):
        scroll.insert(INSERT, StudentsList[i].getStudentInfo(), "\n")

    reportWin.geometry("300x300+558+250")
    Label(reportWin).grid()

#==========================================================================#
#                            Employees Functions
#==========================================================================#


def addEmp():
    def tempEmp():
        print(len(EmployeesList))
        loans = [int(i) for i in loansValue.get().split(",") ]

        temp = Employee(nameValue.get() , addressValue.get() , int(empNumValue.get()) , float(salaryValue.get()) , jobTitleValue.get() , loans )
        EmployeesList.append(temp)
        
        print(len(EmployeesList))
#name, address, employeeNumber, salary, jobTitle, loans

    addEmployee = Toplevel(root)
    addEmployee.title("Add Employee")

    Label(addEmployee, text="Name : ").place(x=10, y=10)
    Label(addEmployee, text="Address : ").place(x=10, y=40)
    Label(addEmployee, text="Employee Number : ").place(x=10, y=70)
    Label(addEmployee, text="Salary : ").place(x=10, y=100)
    Label(addEmployee, text="Job Title : ").place(x=10, y=130)
    Label(addEmployee, text="Loans : ").place(x=10, y=160)


#def add():
#     return Employee(nameValue, addressValue, empNumValue, 
#     salaryValue, jobTitleValue, loansValue)

    nameValue = StringVar()
    addressValue = StringVar()
    empNumValue = StringVar()
    salaryValue = DoubleVar()
    jobTitleValue = StringVar()
    loansValue = StringVar()

    name = Entry(addEmployee , textvariable = nameValue).place(x=150, y=10)
    address = Entry(addEmployee , textvariable = addressValue).place(x=150, y=40)
    empNum = Entry(addEmployee , textvariable = empNumValue).place(x=150, y=70)
    salary = Entry(addEmployee , textvariable = salaryValue).place(x=150, y=100)
    jobTitle = Entry(addEmployee , textvariable = jobTitleValue).place(x=150, y=130)
    loans = Entry(addEmployee , textvariable = loansValue).place(x=150, y=160)

    # newEmp = {
    #     "name": nameValue.get(),
    #     "address": addressValue.get(),
    #     "empNum": empNumValue.get(),
    #     "salary": salaryValue.get(),
    #     "jobTitle": jobTitleValue.get(),
    #     "loans": loansValue.get().split(",")
    # }


    save = Button(addEmployee, text="Save", command= tempEmp ).place(x=100, y=200)
    cancel = Button(addEmployee, text="Cancel").place(x=200, y=200)

    addEmployee.geometry("300x300+558+250")
    Label(addEmployee).grid()


def viewEmp():
    viewEmployee = Toplevel(root)
    viewEmployee.title("view Employee")

    scroll = st.ScrolledText(viewEmployee, width=50, height=10)
    scroll.grid(column=0, row=2)

    for i in range(len(EmployeesList)):
        scroll.insert(INSERT, EmployeesList[i].getEmployeeInfo(), "\n")


    viewEmployee.geometry("300x300+558+250")
    Label(viewEmployee).grid()


def delEmp():


    def deleteEmp():
        msg=True
        for i,j in enumerate(EmployeesList):
            if(j.employeeNumber == int(empNumber.get())):
                EmployeesList.pop(i)
                msg=False
         
        if msg:
            messagebox.showerror("ERROR","This Employee is not exist")
        
        print("ffffffffff" , len(StudentsList))
    
    delEmployee = Toplevel(root)
    delEmployee.title("Delete Employee")

    Label(delEmployee, text="Employee ID : ").place(x=10, y=10)
    
    empNumber = StringVar()
    id = Entry(delEmployee , textvariable = empNumber).place(x=150, y=10)
    delete = Button(delEmployee, text="Delete" , command = deleteEmp ).place(x=50, y=100)
    cancel = Button(delEmployee, text="Cancel" , command = "").place(x=100, y=100)

    delEmployee.geometry("300x300+558+250")
    Label(delEmployee).grid()


#==========================================================================#
#                            Student Functions
#==========================================================================#


def addStu():
    def tempStu():
        print(len(StudentsList))
        # marks = [int(i) for i in loansValue.get().split(",") ]

        temp = Student(nameValue.get(), addressValue.get(), stuNumValue.get(), subjectValue.get(), marksValue.get())
        # temp = Student(nameValue.get() , addressValue.get() , int(stuNumValue.get()), subjectValue.get(), marksValue.get())
        StudentsList.append(temp)
        
        print(len(StudentsList))
        #name, address, employeeNumber, salary, jobTitle, loans

    addStudent = Toplevel(root)
    addStudent.title("Add Student")

    Label(addStudent, text="Name : ").place(x=10, y=10)
    Label(addStudent, text="Address : ").place(x=10, y=40)
    Label(addStudent, text="Student Number : ").place(x=10, y=70)
    Label(addStudent, text="Subject : ").place(x=10, y=100)
    Label(addStudent, text="Marks : ").place(x=10, y=130)



#     return Employee(nameValue, addressValue, empNumValue, 
#     salaryValue, jobTitleValue, loansValue)

    nameValue    =  StringVar()
    addressValue =  StringVar()
    stuNumValue  =  IntVar()
    subjectValue =  StringVar()
    marksValue   =  StringVar()

    name = Entry(addStudent , textvariable = nameValue).place(x=150, y=10)
    address = Entry(addStudent , textvariable = addressValue).place(x=150, y=40)
    stuNum = Entry(addStudent , textvariable = stuNumValue).place(x=150, y=70)
    subject = Entry(addStudent , textvariable = subjectValue).place(x=150, y=100)
    marks = Entry(addStudent , textvariable = marksValue).place(x=150, y=130)


    save = Button(addStudent, text="Save", command= tempStu ).place(x=100, y=200)
    cancel = Button(addStudent, text="Cancel").place(x=200, y=200)

    addStudent.geometry("300x300+558+250")
    Label(addStudent).grid()






# def addStd():
#     addStudent = Toplevel(root)
#     addStudent.title("Add Student")

#     Label(addStudent, text="Name : ").place(x=10, y=10)
#     Label(addStudent, text="Address : ").place(x=10, y=40)
#     Label(addStudent, text="Student Number : ").place(x=10, y=70)
#     Label(addStudent, text="Subject : ").place(x=10, y=100)
#     Label(addStudent, text="Marks : ").place(x=10, y=130)

#     name = Entry(addStudent).place(x=150, y=10)
#     address = Entry(addStudent).place(x=150, y=40)
#     stdNum = Entry(addStudent).place(x=150, y=70)
#     subject = Entry(addStudent).place(x=150, y=100)
#     marks = Entry(addStudent).place(x=150, y=130)

#     save = Button(addStudent, text="Save").place(x=100, y=200)
#     cancel = Button(addStudent, text="Cancel").place(x=200, y=200)

#     addStudent.geometry("300x300+558+250")
#     Label(addStudent).grid()


def viewStd():
    viewStudent = Toplevel(root)
    viewStudent.title("view Student")

    scroll = st.ScrolledText(viewStudent, width=50, height=10)
    scroll.grid(column=0, row=0)

    for i in range(len(StudentsList)):
        scroll.insert(INSERT, StudentsList[i].getStudentInfo(), "\n")

    viewStudent.geometry("300x300+558+250")
    Label(viewStudent).grid()


def delStd():

    def deleteStd():
        msg=True
        for i,j in enumerate(StudentsList):
            if(j.studentNumber == int(stdNumber.get())):
                StudentsList.pop(i)
                msg=False
         
        if msg:
            messagebox.showerror("ERROR","This Student is not exist")
        
        print("ffffffffff" , len(StudentsList))

    

    delStudent = Toplevel(root)
    delStudent.title("view Employee")


    Label(delStudent, text = "Student Number : " ).place(x=10, y=10)
    
    stdNumber = StringVar()
    id = Entry(delStudent , textvariable = stdNumber).place(x=150, y=10)

    delete = Button(delStudent, text="Delete" , command = deleteStd).place(x=50, y=100)
    cancel = Button(delStudent, text="Cancel").place(x=100, y=100)

    delStudent.geometry("300x300+558+250")
    Label(delStudent).grid()


root = Tk()
root.title("project 2")


top = Menu(root)
root.config(menu=top)

file = Menu(top, tearoff=0)
file.add_command(label="Report", command=reportWindow)
file.add_separator()
file.add_command(label="Exit", command=root.destroy)
top.add_cascade(label='File', menu=file)


employee = Menu(top, tearoff=0)
employee.add_command(label="Add", command=addEmp)
employee.add_command(label="View", command=viewEmp)
employee.add_command(label="Delete", command=delEmp)
top.add_cascade(label='Employee', menu=employee)


student = Menu(top, tearoff=0)
student.add_command(label="Add", command=addStu)
student.add_command(label="View", command=viewStd)
student.add_command(label="Delete", command=delStd)
top.add_cascade(label='Student', menu=student)


Help = Menu(top, tearoff=0)
Help.add_command(label="About", command="")
top.add_cascade(label='Help', menu=Help)


root.geometry("500x400+518+200")
root.mainloop()
