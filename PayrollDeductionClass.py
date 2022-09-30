# Write a class that represents a payroll deduction transaction. 
# Each instance should have the description, date, charge amount
# and employee ID as attributes. The class’s __init__ method should accept 
# an argument for each attribute. The class should have accessor methods for each attribute.
# All attribute should be hidden.

class Deduction:
    
    def __init__(self, description, date, charge_amt, EmpID):
        self.__description  = description
        self.__date = date
        self.__charge_amt = charge_amt
        self.__EmpID = EmpID

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_charge_amt(self):
        return self.__charge_amt

    def get_EmpID(self):
        return self.__EmpID
