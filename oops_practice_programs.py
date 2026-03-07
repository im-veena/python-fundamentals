# =========================================
# Python Class & Object Practice Programs
# Author: Veena
# =========================================


# =========================================
# 1. Without Argument
# =========================================
class College():
    def college_name(self):
        print("My college name is Arunachala")

c = College()
c.college_name()


# =========================================
# 2. With Argument
# =========================================
class Student():
    def display_name(self, name):
        print("Student name is", name)

s = Student()
s.display_name("Veena")


# =========================================
# 3. Class with Return (with argument)
# =========================================
class Calculator():
    def subtract(self, a, b):
        return a - b

c = Calculator()
print("Subtraction:", c.subtract(4, 6))


# =========================================
# 4. Class with Return (without argument)
# =========================================
class Company():
    def company_name(self):
        name = "Infosys"
        return name

c = Company()
print("Company name is", c.company_name())


# =========================================
# 5. Employee Details
# =========================================
class Employee():
    def details(self, name, dept):
        print("Employee Name:", name)
        print("Employee Department:", dept)

e = Employee()
e.details("Veena", "IT")


# =========================================
# 6. Person Information
# =========================================
class Person():
    def info(self, name, age):
        print("Name:", name)
        print("Age:", age)

p = Person()
p.info("Veena", 21)


# =========================================
# 7. Sum of Numbers using Loop
# =========================================
class Numbers():
    def total(self, num):
        total = 0
        for i in num:
            total = total + i
        print("Total is:", total)

n = Numbers()
n.total([10, 20, 30])


# =========================================
# 8. Display Dictionary Data
# =========================================
class Details():
    def show(self, data):
        print("** Data **")
        for k, v in data.items():
            print(k, ":", v)

d = Details()
data = {"name": "Veena", "age": 21, "city": "Vellore"}
d.show(data)


# =========================================
# 9. Book Price
# =========================================
class Book():
    def book_price(self, price):
        print("Book price is", price)

b = Book()
b.book_price(50)


# =========================================
# 10. Square of Number
# =========================================
class Math():
    def square(self, num):
        return num * num

m = Math()
print("Square is:", m.square(6))


# =========================================
# 11. Bank Initial Balance
# =========================================
class Bank():
    def __init__(self):
        self.balance = 1000

    def show_balance(self):
        print("Initial balance:", self.balance)

b = Bank()
b.show_balance()


# =========================================
# 12. Bank Deposit
# =========================================
class BankDeposit():
    def __init__(self):
        self.balance = 1000

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Total balance is", self.balance)

b = BankDeposit()
b.deposit(500)


# =========================================
# 13. Student Name using self
# =========================================
class SStudent():
    def set_name(self, name):
        self.name = name

    def show_name(self):
        print("Student name is", self.name)

s = SStudent()
s.set_name("Veena")
s.show_name()


# =========================================
# 14. Rectangle Area
# =========================================
class Rectangle():
    def set_values(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        a = self.length * self.breadth
        print("The area is", a)

r = Rectangle()
r.set_values(5, 4)
r.area()