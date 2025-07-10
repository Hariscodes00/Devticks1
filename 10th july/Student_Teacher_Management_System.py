#Student & Teacher Management System

# Person (Base class)
# name, age
# Student (Inherits from Person)
# roll_number, marks (list of subject marks)
# Method: get_total(), get_percentage()
# Teacher (Inherits from Person)
# subject, salary

print("Student And Teacher Management System:\n")

class Person:
    def __init__(self,name,age):
        self.age = age
        self.name = name

#making Student class

class Student(Person):
    def __init__(self,name,age,roll_number,marks):
        super().__init__(name,age)
        self.marks = marks
        self.roll_number = roll_number
#making methods
    def get_total(self):
        return sum(self.marks)

    def get_percentage(self):
        return self.get_total()/len(self.marks)

#Teacher class

class Teacher(Person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject = subject
        self.salary = salary

#giving values
s1 = Student("Haris" , 21 , 1021 , [60,30,50])
t1 = Teacher("Sir ajmal" , 40 , "Math" , 40000)

#printing result
print(f"{s1.name} Total numbers Are : {s1.get_total()} \nPercentage is : {s1.get_percentage():.2f}%")
print(f"Name Of Teacher is: {t1.name} \nSalary : {t1.salary}")
