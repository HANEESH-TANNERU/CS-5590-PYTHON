class Employee():

    employCount = 0
    Sum=0
    Avg =0

    def __init__(self, id, name, family, salary, department):
        self.id = id
        self.name = name
        self.family=family
        self.salary = salary
        self.department = department
        Employee.employCount += 1
        Employee.Sum += self.salary

    def displayEmployee(self):
        print("id : ", self.id, ", Name : ", self.name,"family :",self.family , " Salary: ", self.salary, ", department: ", self.department)


class FullTimeEmployee(Employee):
    def __init__(self, id, name,family,salary, department):
        Employee.__init__(self, id, name,family, salary, department)
    def displayEmployee(self):
        print("id : ", self.id, ", Name : ", self.name,"family :",self.family ,", Salary:,", self.salary, ", department: ", self.department)


employ1 = Employee(1, "haneesh","T", 100000, "Ece")
employ2 = Employee(2, "sai","y", 8000, "Cse")
employ3=FullTimeEmployee(3, "tanneru","S", 7000,"It")
print("Total Employees %d" % Employee.employCount)
print("Average salary of the employees is", (Employee.Sum/Employee.employCount))
print(employ1.displayEmployee())
print(employ2.displayEmployee())
print(employ3.displayEmployee())
