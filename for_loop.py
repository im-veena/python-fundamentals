# =========================================
# Python loop programs Practice
# Author: Veena
# Description: Basic for loop examples
# =========================================


# Program 1: Print numbers from 0 to 2
for i in range(3):
    print(i)

print("--------------------")


# Program 2: Print numbers from 2 to 4
for i in range(2, 5):
    print(i)

print("--------------------")


# Program 3: Print items from a list
foods = ["pizza", "burger", "fries"]
for food in foods:
    print(food)

print("--------------------")


# Program 4: Print each letter of a word
word = "snake"
for letter in word:
    print(letter)

print("--------------------")


# Program 5: Print each character using different variable name
word = "snake"
for char in word:
    print(char)

print("--------------------")


# Program 6: Sum of numbers from 4 to 7
total = 0
for i in range(4, 8):
    total = total + i
print("Total:", total)

print("--------------------")


# Program 7: Multiplication table of 2
num = 2
for l in range(1, 11):
    print(num, "*", l, "=", num * l)

print("--------------------")


# Program 8: Factorial of a number
num = 5
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print("Factorial:", fact)

print("--------------------")


# Program 9: Palindrome check
tex = input("Enter a word: ")
rev = ""

for i in range(len(tex) - 1, -1, -1):
    rev = rev + tex[i]

print("Reversed word:", rev)

if rev == tex:
    print("The given word is a palindrome")
else:
    print("The given word is not a palindrome")

print("--------------------")


# Program 10: Prime numbers between 10 and 20
for num in range(10, 21):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("It is a prime:", num)
    else:
        print("Not a prime:", num)

print("--------------------")

# Program 11: Print the square of numbers from 1 to 5.
for i in range(1,6):
   if(i>0):
       print(i*i)

       
print("--------------------")

# Program 12: Print the square of numbers from 1 to 5.
for i in range(0,21):
   if(i%2==0):
       print(i)

       
print("--------------------")

# program:13 Sum of even numbers between 1 and 50
n=int(input("enter a number:"))
total = 0
for i in range(2, 51, 2):
    total = total + i

    
print("--------------------")


