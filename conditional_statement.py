<<<<<<< HEAD
#if condition
# else condition 
 
#1.Student Pass or Fail Program
mark=int(input("enter your mark:"))
if mark>=35:
    print("pass")
else:
     print("fail")

#2.Even or Odd Checker
n=int(input("enter a number:"))
if(n%2==0):
    print("The given number is even")
else:
 print("the given number is odd")

#3.TO find wheather a number is positive or negative and odd or even.
n=int(input("Enter a number:"))
if(n>0):
    print("The given number is positive ")
    if(n%2==0):
        print("The given number is even")
    else:
        print("odd")
elif(n<0):
   print("The given number is negative")
   if(n%2==0):
    print("even")
   else:
        print("The given number is odd")
else:
        print("The given number is zero")

#4 vote eligibility checker 
Age=int(input("Enter your Age:"))
if(Age>18):
    print("eligible to vote")
else:
    print("not eligible to vote")

#5 finding largest among two numbers
a=int(input("enter a number:"))
b=int(input("enter a number:"))
if(a>b):
    print("a is greater")
else:
    print("b is greater")

#6 Grade calculator
mark=int(input("enter your mark:"))
if(mark>=80):
    print("Grade A")
elif(mark>=70):
    print("Grade B")
elif(mark>=60):
   # print("Grade C")
#elif(mark>=50):
    print("Grade D")
#else:
    print("improve yourself")

#7.Discount Eligibility Program
bill = int(input("Enter your bill amount: "))
memberid = int(input("Enter your member id: "))
if bill >= 1000:
    print("Discount applied")
    if memberid == 1234:
        print("Extra discount of 10% available")
    else:
        print("No extra discount applied")
else:
    print("No discount available")

#8.password checker
password = input("Enter your password: ")

if len(password) >= 8:
    if any(char.isdigit() for char in password):
        print("Strong password")
    else:
        print("Password is medium (add numbers)")
else:
    print("Weak password (too short)")
#leap year or not
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

#10.simple calculator
print("1.addition")
print("2.subraction")
print("3.multiplication")
print("4.division")

n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
choice= int(input("enter a option from (1-4):"))

if choice==1:
    print("result=",n1+n2)
elif choice==2:
    print("result=",n1-n2)
elif choice==3:
    print("result=",n1*n2)
elif choice==4:
    print("result=",n1/n2)
else:
    print("invalid choice")

#11.divisibility checker

n1 = int(input("Enter a number: "))

if n1 % 5 == 0 and n1 % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")


=======
#if condition
# else condition 
 
#1.Student Pass or Fail Program
#mark=int(input("enter your mark:"))
#if mark>=35:
    #print("pass")
#else:
   # print("fail")

#2.Even or Odd Checker
#n=int(input("enter a number:"))
#if(n%2==0):
   # print("The given number is even")
#else:
# print("the given number is odd")

#3.TO find wheather a number is positive or negative and odd or even.
n=int(input("Enter a number:"))
if(n>0):
    print("The given number is positive ")
    if(n%2==0):
        print("The given number is even")
    else:
        print("odd")
elif(n<0):
   print("The given number is negative")
   if(n%2==0):
    print("even")
   else:
        print("The given number is odd")
else:
        print("The given number is zero")

#4 vote eligibility checker 
Age=int(input("Enter your Age:"))
if(Age>18):
    print("eligible to vote")
else:
    print("not eligible to vote")

#5 finding largest among two numbers
a=int(input("enter a number:"))
b=int(input("enter a number:"))
if(a>b):
    print("a is greater")
else:
    print("b is greater")

#6 Grade calculator
mark=int(input("enter your mark:"))
if(mark>=80):
    print("Grade A")
elif(mark>=70):
    print("Grade B")
elif(mark>=60):
   # print("Grade C")
#elif(mark>=50):
    print("Grade D")
#else:
    print("improve yourself")

#7.Discount Eligibility Program
bill = int(input("Enter your bill amount: "))
memberid = int(input("Enter your member id: "))
if bill >= 1000:
    print("Discount applied")
    if memberid == 1234:
        print("Extra discount of 10% available")
    else:
        print("No extra discount applied")
else:
    print("No discount available")

#8.password checker
password = input("Enter your password: ")

if len(password) >= 8:
    if any(char.isdigit() for char in password):
        print("Strong password")
    else:
        print("Password is medium (add numbers)")
else:
    print("Weak password (too short)")
#9leap year or not
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

#10.simple calculator
print("1.addition")
print("2.subraction")
print("3.multiplication")
print("4.division")

n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
choice= int(input("enter a option from (1-4):"))

if choice==1:
    print("result=",n1+n2)
elif choice==2:
    print("result=",n1-n2)
elif choice==3:
    print("result=",n1*n2)
elif choice==4:
    print("result=",n1/n2)
else:
    print("invalid choice")

#11.divisibility checker

n1 = int(input("Enter a number: "))

if n1 % 5 == 0 and n1 % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")


>>>>>>> a36706ef10ba65c75d53a68ded4ba2eb59376a45
