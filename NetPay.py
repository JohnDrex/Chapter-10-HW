import EmployeeClass as employee #accounts

def main():
    print('Enter the following customer data: ')
    name = "Jimmy Smith"
    IDNum = 58475
    department = "Information Systems"
    job = "Developer"
    MSalary = 6800
   
    employeeinfo = employee.Person(name, IDNum, department, job, MSalary)

    print()
    print('Table 1:')
    print('-------')
    print('| Name        | ID Number | Department          | Job Title     | Monthly Salary |')
    print('|', employeeinfo.get_name(), '|', employeeinfo.get_IDNum(), '    |', employeeinfo.get_department(), '|', employeeinfo.get_job(), '    |', employeeinfo.get_MSalary(), '          |')
    print()
    print()
    print()
    print("Table 2:")

    
    
    
    
    
    print()
    print()
    print()
    
    print("*** Employee Pay ***")
    print('Name:', employeeinfo.get_name())
    print('ID Number:', employeeinfo.get_IDNum())
    print('Department:', employeeinfo.get_department())
    print('Gross Pay: $', format(employeeinfo.get_MSalary(), ',.2f'), sep='')
    print('Net Pay: $', format(employeeinfo.get_MSalary(), ',.2f'), sep='')
    
   
main()