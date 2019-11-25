# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:41:29 2019

@author: Hani
"""

class Employee:
    def __init__(self , emp_number , name , address , salary , job_title ):
        self.emp_number = emp_number
        self.__name = name 
        self.__address = address
        self.__salary = salary
        self.__job_title = job_title
        
        
    def getName(self):
        return self.__name
    
    def getAddress(self):
        return self.__address
    
    def setAddress(self , newaddress):
        self.__address = newaddress
        
    def getSalary(self):
        return self.__salary
    
    def getJobTitle(self):
        return self.__job_title
    
    def __del__(self):
        print(self.__name +" has been deleted")
        
        
    def getEmpInfoFormate1(self):
        print("Employee1 Information :" , "\n\tEmployee Number : " + str(self.emp_number) ,
         "\n\tName : " + str(self.getName()) , 
         "\n\tAddress : " + str(self.getAddress()) ,
         "\n\tSalary : " + str(self.getSalary()) ,
         "\n\tJob Title : " + str(self.getJobTitle()))
        
    def getEmpInfoFormate2(self):
         print("Employee2 Information :" , "Employee Number : " + str(self.emp_number) ,
         ", Name : " + str(self.getName()) , 
         ", Address : " + str(self.getAddress()) ,
         ", Salary : " + str(self.getSalary()) ,
         ", Job Title : " + str(self.getJobTitle()))
    
    
Emp1 = Employee( 1 , "Mohammad Khalid" , "Amman,Jordan" , 500.0 , "Consultant")

Emp2 = Employee( 2 , "Hala Rana" , "Aqaba,Jordan" , 750.0 , "Manager")

Emp1.getEmpInfoFormate1()
Emp2.getEmpInfoFormate2()

Emp1.setAddress("USA")

print(Emp1.getAddress())

del Emp1
del Emp2