# =========================================
# Python Inheritance Practice
# Author: Veena
# =========================================


# =========================================
# 1. Single Inheritance Example
# =========================================

class Vehicle():
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

v = Car()
v.start()
v.drive()



# =========================================
# 2. Practice Program - Person & Student
# =========================================

class Person():
    def set_details(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

s = Student()
s.set_details("Veena",21)
s.display()



# =========================================
# 3. Constructor Inheritance Example
# =========================================

class Employee():
    def __init__(self,id,name):
        self.id = id
        self.name = name

class Manager(Employee):
    def display(self):
        print("Employee ID:",self.id)
        print("Employee Name:",self.name)

e = Manager(101,"Veena")
e.display()



# =========================================
# 4. Multilevel Inheritance Example
# =========================================

class Animal():
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def sleep(self):
        print("Puppy sleeps")

p = Puppy()
p.eat()
p.bark()
p.sleep()



# =========================================
# 5. Hierarchical Inheritance Example
# =========================================

class Shape():
    def set_values(self,length,breadth):
        self.length = length
        self.breadth = breadth

class Rectangle(Shape):
    def area(self):
        print("Rectangle Area:",self.length*self.breadth)

class Triangle(Shape):
    def area(self):
        print("Triangle Area:",0.5*self.length*self.breadth)

r = Rectangle()
r.set_values(6,4)
r.area()

t = Triangle()
t.set_values(6,4)
t.area()



# =========================================
# 6. Multiple Inheritance Example
# =========================================

class Father():
    def skills(self):
        print("Gardening")

class Mother():
    def talents(self):
        print("Cooking")

class Child(Father,Mother):
    def show(self):
        print("Child skills:")

c = Child()
c.show()
c.skills()
c.talents()



# =========================================
# 7. Practice Program - Bank Account
# =========================================

class BankAccount():
    def deposit(self,amount):
        self.balance = amount

    def withdraw(self,amount):
        self.balance = self.balance - amount

class SavingsAccount(BankAccount):
    def display_balance(self):
        print("Balance:",self.balance)

b = SavingsAccount()
b.deposit(10000)
b.withdraw(500)
b.display_balance()



# =========================================
# 8. Practice Program - School Example
# =========================================

class School():
    def school_name(self,name):
        self.name = name

class Student(School):
    def student_name(self,sname):
        self.sname = sname

    def display(self):
        print("School:",self.name)
        print("Student:",self.sname)

st = Student()
st.school_name("ABC School")
st.student_name("Veena")
st.display()



# =========================================
# 9. Practice Program - Shape Square
# =========================================

class Shape():
    def set_side(self,side):
        self.side = side

class Square(Shape):
    def area(self):
        print("Square Area:",self.side*self.side)

sq = Square()
sq.set_side(5)
sq.area()



# =========================================
# 10. Practice Program - Vehicle Types
# =========================================

class Vehicle():
    def start(self):
        print("Vehicle Started")

class Bike(Vehicle):
    def ride(self):
        print("Bike Riding")

class Bus(Vehicle):
    def move(self):
        print("Bus Moving")

b = Bike()
b.start()
b.ride()

u = Bus()
u.start()
u.move()
