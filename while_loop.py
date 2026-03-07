<<<<<<< HEAD
# =========================================
# Python While Loop Practice Programs
# Author: Veena
# Description: Beginner to basic logic problems using while loops
# =========================================


# -----------------------------------------
# 1. Print numbers from 1 to 5
# -----------------------------------------
i = 1
while i <= 5:
    print(i)
    i = i + 1


# -----------------------------------------
# 2. Print numbers from 10 to 1 (reverse)
# -----------------------------------------
i = 10
while i >= 1:
    print(i)
    i = i - 1


# -----------------------------------------
# 3. Print even numbers from 2 to 10
# -----------------------------------------
i = 2
while i <= 10:
    print(i)
    i = i + 2


# -----------------------------------------
# 4. Print odd numbers from 1 to 9
# -----------------------------------------
i = 1
while i <= 9:
    print(i)
    i = i + 2


# -----------------------------------------
# 5. Print numbers from 1 to 10 and their sum
# -----------------------------------------
i = 1
total = 0
while i <= 10:
    print(i)
    total = total + i
    i = i + 1
print("Sum =", total)


# -----------------------------------------
# 6. Table of a number (user input)
# -----------------------------------------
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num * i)
    i = i + 1


# -----------------------------------------
# 7. Count numbers from 1 to 20 divisible by 3
# -----------------------------------------
i = 1
count = 0
while i <= 20:
    if i % 3 == 0:
        count = count + 1
    i = i + 1
print("Count =", count)


# -----------------------------------------
# 8. Keep asking numbers until 0
# -----------------------------------------
num = int(input("Enter a number (0 to stop): "))
while num != 0:
    print("You entered:", num)
    num = int(input("Enter a number (0 to stop): "))
print("Loop ended")


# -----------------------------------------
# 9. Sum of numbers until -1
# -----------------------------------------
total = 0
num = int(input("Enter a number (-1 to stop): "))
while num != -1:
    total = total + num
    num = int(input("Enter a number (-1 to stop): "))
print("Total sum =", total)


# -----------------------------------------
# 10. Reverse a number
# -----------------------------------------
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Reversed number:", rev)


# -----------------------------------------
# 11. Sum of digits
# -----------------------------------------
num = int(input("Enter a number: "))
total = 0
while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10
print("Sum of digits =", total)


# -----------------------------------------
# 12. Count digits
# -----------------------------------------
num = int(input("Enter a number: "))
count = 0
if num == 0:
    count = 1
else:
    while num > 0:
        num = num // 10
        count = count + 1
print("Total digits =", count)


# -----------------------------------------
# 13. Find the largest number (stop at 0)
# -----------------------------------------
largest = 0
num = int(input("Enter number (0 to stop): "))
while num != 0:
    if num > largest:
        largest = num
    num = int(input("Enter number (0 to stop): "))
print("Largest number is:", largest)


# -----------------------------------------
# 14. Count numbers entered (stop at -1)
# -----------------------------------------
count = 0
num = int(input("Enter a number (-1 to stop): "))
while num != -1:
    count = count + 1
    num = int(input("Enter a number (-1 to stop): "))
print("Total numbers entered =", count)


# -----------------------------------------
# 15. To check whether a given word is palindrome or not
# -----------------------------------------
str=input("enter a word:")
res="" 
i=len(str)-1
while i>=0:
    res=res+str[i]
    i=i-1
    if res==str:
        print("The given word is palindrome")
    else:
         print("The given word is not a palindrome")
    
=======
# =========================================
# Python While Loop Practice Programs
# Author: Veena
# Description: Beginner to basic logic problems using while loops
# =========================================


# -----------------------------------------
# 1. Print numbers from 1 to 5
# -----------------------------------------
i = 1
while i <= 5:
    print(i)
    i = i + 1


# -----------------------------------------
# 2. Print numbers from 10 to 1 (reverse)
# -----------------------------------------
i = 10
while i >= 1:
    print(i)
    i = i - 1


# -----------------------------------------
# 3. Print even numbers from 2 to 10
# -----------------------------------------
i = 2
while i <= 10:
    print(i)
    i = i + 2


# -----------------------------------------
# 4. Print odd numbers from 1 to 9
# -----------------------------------------
i = 1
while i <= 9:
    print(i)
    i = i + 2


# -----------------------------------------
# 5. Print numbers from 1 to 10 and their sum
# -----------------------------------------
i = 1
total = 0
while i <= 10:
    print(i)
    total = total + i
    i = i + 1
print("Sum =", total)


# -----------------------------------------
# 6. Table of a number (user input)
# -----------------------------------------
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num * i)
    i = i + 1


# -----------------------------------------
# 7. Count numbers from 1 to 20 divisible by 3
# -----------------------------------------
i = 1
count = 0
while i <= 20:
    if i % 3 == 0:
        count = count + 1
    i = i + 1
print("Count =", count)


# -----------------------------------------
# 8. Keep asking numbers until 0
# -----------------------------------------
num = int(input("Enter a number (0 to stop): "))
while num != 0:
    print("You entered:", num)
    num = int(input("Enter a number (0 to stop): "))
print("Loop ended")


# -----------------------------------------
# 9. Sum of numbers until -1
# -----------------------------------------
total = 0
num = int(input("Enter a number (-1 to stop): "))
while num != -1:
    total = total + num
    num = int(input("Enter a number (-1 to stop): "))
print("Total sum =", total)


# -----------------------------------------
# 10. Reverse a number
# -----------------------------------------
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Reversed number:", rev)


# -----------------------------------------
# 11. Sum of digits
# -----------------------------------------
num = int(input("Enter a number: "))
total = 0
while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10
print("Sum of digits =", total)


# -----------------------------------------
# 12. Count digits
# -----------------------------------------
num = int(input("Enter a number: "))
count = 0
if num == 0:
    count = 1
else:
    while num > 0:
        num = num // 10
        count = count + 1
print("Total digits =", count)


# -----------------------------------------
# 13. Find the largest number (stop at 0)
# -----------------------------------------
largest = 0
num = int(input("Enter number (0 to stop): "))
while num != 0:
    if num > largest:
        largest = num
    num = int(input("Enter number (0 to stop): "))
print("Largest number is:", largest)


# -----------------------------------------
# 14. Count numbers entered (stop at -1)
# -----------------------------------------
count = 0
num = int(input("Enter a number (-1 to stop): "))
while num != -1:
    count = count + 1
    num = int(input("Enter a number (-1 to stop): "))
print("Total numbers entered =", count)
>>>>>>> a36706ef10ba65c75d53a68ded4ba2eb59376a45
