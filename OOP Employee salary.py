class Employee:

    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role:",self.role)
        print("Department:",self.dept)
        print("Salary:",self.salary)

class Engineer(Employee):

    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT",100000)

e1 = Employee("Acountant","Finance",60000)
e2 = Engineer("Ali Zahid",19)
e2.showDetails()