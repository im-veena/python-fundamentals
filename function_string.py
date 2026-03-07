# =========================================
# Python String Functions Practice
# Author: Veena
# =========================================

# 1. upper()
s = "hello world"
print(s.upper())


# 2. lower()
s = "HELLO WORLD"
print(s.lower())


# 3. capitalize()
s = "python programming"
print(s.capitalize())


# 4. title()
s = "welcome to python"
print(s.title())


# 5. swapcase()
s = "PyThOn"
print(s.swapcase())


# 6. len()
s = "data analyst"
print(len(s))


# 7. isalpha()
s = "Python"
print(s.isalpha())


# 8. isdigit()
s = "12345"
print(s.isdigit())


# 9. isalnum()
s = "Python123"
print(s.isalnum())


# 10. islower()
s = "hello"
print(s.islower())


# 11. isupper()
s = "HELLO"
print(s.isupper())


# 12. startswith()
s = "Welcome to Python"
print(s.startswith("Welcome"))


# 13. endswith()
s = "data.csv"
print(s.endswith(".csv"))


# 14. find()
s = "Python is easy"
print(s.find("is"))


# 15. index()
s = "Welcome to Python"
print(s.index("to"))


# 16. count()
s = "banana"
print(s.count("a"))


# 17. replace()
s = "I like Java"
print(s.replace("Java", "Python"))


# 18. split()
s = "apple,banana,grape"
print(s.split(","))


# 19. join()
words = ["Python", "is", "fun"]
print(" ".join(words))


# 20. strip()
s = "   hello   "
print(s.strip())


# 21. lstrip()
s = "   hello"
print(s.lstrip())


# 22. rstrip()
s = "hello   "
print(s.rstrip())


# 23. substring check using in
s = "Welcome to Python"
print("Python" in s)


# 24. basic slicing
s = "Python"
print(s[0:4])


# 25. slicing with step
s = "DataScience"
print(s[0:10:2])


# 26. reverse string using slicing
s = "Python"
print(s[::-1])


# 27. compare strings
a = "apple"
b = "banana"
print(a == b)
print(a < b)

#practice programs

#To get a index value 

s="welcome to python"
print(s.index("m"))
print(s.index("to"))
print(s.index(" "))
print(s.index("e"))
print(s.index(""))
print(s.index("n"))
print(s.index(""))

print("------------------------------")

#String Find Function Examples
s="welcome to python"
print(s.find("m"))
print(s.find("q"))
print(s.find("to"))
print(s.find(" "))
print(s.rfind("e"))
print(s.find("e"))
print(s.find(""))

print("------------------------------")

#String startswith Function Examples

s="Welcome to python"
print(s.startswith("Welcome"))
print(s.startswith("welcome"))
print(s.startswith("Wel"))
print(s.startswith("W"))
print(s.startswith("to"))
print(s.startswith("python"))
print(s.startswith(" "))

print("------------------------------")

#String endswith Function Examples

s="Welcome to python"

print(s.endswith("Welcome"))
print(s.endswith("python"))
print(s.endswith("on"))
print(s.endswith("n"))


print("------------------------------")

#String Contains Function Example

s = "All of us are dead"
print(s.__contains__("s"))
print(s.__contains__('dead'))
print(s.__contains__("ll"))
print(s.__contains__("are"))
print(s.__contains__("th"))
print(s.__contains__(" "))


print("------------------------------")

#String in Function Example

s = "All of us are dead"
print("All" in s)
print("of" in s)
print(" " in s)
print("java" in s)
print("me" in s)

print("------------------------------")