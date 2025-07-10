# class Employee:
#     def __init__(self,first,last,salary):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@company.com'
#         self.salary = salary
#     def attri(self):
#         return('{} {} {} {}' .format(self.first , self.last,self.email,self.salary))
# emp_1 = Employee('Haris','Rafique',600)
# emp_2 = Employee('Hamza' , 'Rafique' , 400)
#
# #print('{} {}' .format(emp_1.first , emp_1.last))
# print(emp_1.attri())
# print(emp_2.attri())

print("Basic Employee Record System")
# Project Goal:
# Let the user:
# Create multiple employees
# View all employee details
# Give a raise to a specific employee

class Employee:
    def __init__(self,first,last,salary):
        self.first = first
        self.last = last
        self.email = f'{first.lower()}.{last.lower()}@devticks.com'
        self.salary = salary

    def get_info (self):
        return f'{self.first} | {self.last} | {self.email} | {self.salary}'

    def apply_raise(self,amount):
        self.salary += amount

# emp_1 = Employee("haris" , "Rafique" , 6000 )
# emp_2 = Employee("hamza" , "Rafique" , 5000)

# print(emp_1.get_info())
# print(emp_2.get_info())

#increasing salary
# print("\nIncreasing salary")
#
# emp_1.apply_raise(50)
#
# print(emp_1.get_info())
# print(emp_2.get_info())

print("\nBetter Approach\n")
employees = []
employees.append(Employee("Haris" , "Rafique" ,6000 ))
employees.append(Employee("Hamza" , "Rafique" , 5000))
for emp in employees:
    print(emp.get_info())
for emp in employees :
    if emp.first.lower() == "haris":
        emp.apply_raise(50)

#learning inheritance
print("started leaning inheritance")
class Personal(Employee):
    def __init__(self,first,last,salary,address):
        super().__init__(first,last,salary)
        self.address = address

employee_personal = []

employee_personal.append(Personal('Haris', 'Rafique' , '6000','house no 276 b block mustafa town' ))
employee_personal.append(Personal('Hamza', 'Rafique' , '5000', 'house no 275 b block mustafa town'))

for emp1 in employee_personal :
     print(emp1.address)