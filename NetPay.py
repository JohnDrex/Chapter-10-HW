import EmployeeClass as employee
from PayrollDeductionClass import Deduction

def main():
    name = "Jimmy Smith"
    IDNum = 58475
    department = "Information Systems"
    job = "Developer"
    MSalary = 6800
   
    employeeinfo = employee.Employee(name, IDNum, department, job, MSalary)

    deduction_1 = Deduction("food court", "8/14/2022", 22.50, 39119)
    deduction_2 = Deduction("gift contribution", "8/12/2022", 25.00,58475)
    deduction_3 = Deduction("food court", "8/17/2022", 15.25,21547)
    deduction_4 = Deduction("vending machine", "8/22/2022", 3.00,58475)
    deduction_5 = Deduction("vending machine", "8/05/2022", 2.75,58475)
    
    print("*** Employee Pay ***")
    print('Name:', employeeinfo.get_name())
    print('ID Number:', employeeinfo.get_IDNum())
    print('Department:', employeeinfo.get_department())
    print('Gross Pay: $', format(employeeinfo.get_MSalary(), ',.2f'), sep='')
    print('Net Pay: $', employeeinfo.get_MSalary() - deduction_2.get_charge_amt() - deduction_4.get_charge_amt() - deduction_5.get_charge_amt())
    
   
main()