#Write a class named Employee that holds the following data about an employee in attributes:
#name, ID number, department, job title and monthly salary.The Employee class’s __init__ method should
#accept an argument for each attribute. The Employee class should have accessor methods for each attribute.
#All attribute should be hidden.

class Employee: #Person
    
    def __init__(self, name, IDNum, department, job, MSalary):
        self.__name = name
        self.__IDNum = IDNum
        self.__department = department
        self.__job = job
        self.__MSalary = MSalary

   
    def set_name(self, name):
        self.__name = name

    def set_IDNum(self, IDNum):
        self.__IDNum = IDNum
    
    def set_department(self, department):
        self.__department = department

    def set_job(self, job):
        self.__job = job
    
    def set_MSalary(self, MSalary):
        self.__MSalary = MSalary

    # The following methods are accessors for the
    # data attributes.

    def get_name(self):
        return self.__name

    def get_IDNum(self):
        return self.__IDNum

    def get_department(self):
        return self.__department

    def get_job(self):
        return self.__job

    def get_MSalary(self):
        return self.__MSalary