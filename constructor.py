#1.Create a class Employee with constructor to initialize id, name, salary.
#a.
class Employee():
     def __init__(self,id,name,salary):
         print("Employee Name-",name)
         print("Employee id-",id)
         print("Employee salary-",salary)
Employee(243,"veena",4567)
print("------------------------------")
#b.
class Employee():
     def __init__(self,id,name,salary):
       self.name = name
       self.id = id
       self.salary = salary
         
e1=Employee(243,"veena",4567)
print("Name-",e1.name)
print("id-",e1.id)
print("salary-",e1.salary)
print("------------------------------")

#2.Create a class Car using constructor to set brand and model.
class Car():
    def __init__(self,brand,model):
        print("Brand-",brand)
        print("Model-",model)
Car("TOYATA","COROLLA")
print("------------------------------")

#3.Create a class Rectangle with constructor to initialize length and width and calculate area
class Rectangle():
    def __init__(self,length,width):
        print("Area:",length*width)
Rectangle(3,4)
print("------------------------------")
#4.Create a class Laptop with constructor to initialize brand, ram, price
class Laptop():
    def __init__(self,Brand,RAM,Price):
        self.b=Brand
        self.R=RAM
        self.P=Price
l=Laptop("DELL","16GB",75000)
print("Brand:",l.b)
print("RAM:",l.R)
print("Price:",l.P)
print("------------------------------")


#5.Create a class Book with constructor to initialize title and author.
class Book():
    def __init__(self,title,author):
        print("Title",title)
        print("Author",author)
Book("wings of fire","A.P.J kalam")
print("------------------------------")

#6.Create a class Person with constructor to print name and age.
class Person():
     def __init__(self,name,age):
         print("Name:",name)
         print("Age:",age)
Person("veena",21)
print("------------------------------")

#7.Create a class Product with constructor to initialize product_name and price. Give the code only for the frist question
class Product():
    def __init__(self,product_name,price):
        print("product_name:",product_name)
        print("price:",price)
Product("abcd",234)
print("------------------------------")