# =========================================
# Python Functions Practice
# Author: Veena
# =========================================


# =========================================
# 1. Without Argument & Without Return
# =========================================

def printrange():
    print("------Print Range------")
    for i in range(1,11):
        print(i)

printrange()



# =========================================
# 2. Without Argument & Without Return
# Odd or Even
# =========================================

def oddoreven():
    n=int(input("Enter a number:"))

    if n%2==0:
        print("Even Number")
    else:
        print("Odd Number")

oddoreven()



# =========================================
# 3. Without Argument & With Return
# Square of number
# =========================================

def square():
    n=int(input("Enter number:"))
    return n*n

print("Square:",square())



# =========================================
# 4. Without Argument & With Return
# Add two numbers
# =========================================

def add():
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    return a+b

print("Sum:",add())



# =========================================
# 5. With Argument & Without Return
# Multiplication table
# =========================================

def table(n):

    print("------Multiplication Table------")

    for i in range(1,11):
        print(n,"x",i,"=",n*i)

table(5)



# =========================================
# 6. With Argument & Without Return
# Pass or Fail
# =========================================

def passorfail(mark):

    if mark>=35:
        print("Pass")
    else:
        print("Fail")

passorfail(45)



# =========================================
# 7. With Argument & With Return
# Largest number
# =========================================

def largest(a,b):

    if a>b:
        return a
    else:
        return b

print("Largest:",largest(10,20))



# =========================================
# 8. Default Argument Function
# Simple Interest
# =========================================

def interest(p,t,r=5):

    si=(p*t*r)/100
    return si

print("Simple Interest:",interest(1000,2))



# =========================================
# 9. Variable Length Argument (*args)
# Add multiple numbers
# =========================================

def add_numbers(*a):

    s=0
    for i in a:
        s+=i

    print("Sum:",s)

add_numbers(10,20,30)
add_numbers(5,10,15,20)



# =========================================
# 10. Keyword Arguments
# =========================================

def employee(id,name,salary):

    print("Employee Id:",id)
    print("Employee Name:",name)
    print("Employee Salary:",salary)

employee(name="Veena",salary=25000,id=101)



# =========================================
# 11. **kwargs (Keyword Variable Argument)
# =========================================

def student_details(**details):

    print("------Student Details------")

    for k,v in details.items():
        print(k,"-",v)

student_details(id=101,name="Veena",dept="IT",city="Chennai")



# =========================================
# 12. Combine Normal + *args + **kwargs
# =========================================

def demo(a,*b,**c):

    print("Normal Argument:",a)
    print("Variable Argument (*args):",b)
    print("Keyword Argument (**kwargs):",c)

demo(10,20,30,40,x=1,y=2)



# =========================================
# 13. Local Variable Example
# =========================================

def local_example():

    x = 10   # local variable
    print("Local variable inside function:",x)

local_example()

# print(x)  # This will give error because x is local



# =========================================
# 14. Global Variable Example
# =========================================

x = 20   # global variable

def global_example():
    print("Global variable inside function:",x)

global_example()

print("Global variable outside function:",x)



# =========================================
# 15. Using global keyword
# =========================================

y = 5

def change_global():

    global y
    y = 50
    print("Changed inside function:",y)

change_global()

print("Changed outside function:",y)