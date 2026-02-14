# =========================================
# NESTED FOR LOOP PRACTICE PROGRAMS
#Author: Veena
# =========================================


# 1. 3x3 Star Square

print("1. 3x3 Star Square")
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()
print("--------------------")


# 2. Right Triangle Star Pattern
print("\n2. Right Triangle Star Pattern")
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()

print("--------------------")


# 3. Inverted Right Triangle

print("\n3. Inverted Right Triangle")
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
print("--------------------")

# 4. Number Square (3x3)

print("\n4. Number Square (3x3)")
for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=" ")
    print()

print("--------------------")

# 5. Continuous Number Matrix (3x3)

print("\n5. Continuous Number Matrix (3x3)")
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()

print("--------------------")

# 6. Right Triangle Number Pattern

print("\n6. Right Triangle Number Pattern")
for i in range(1, 5):
    for j in range(i):
        print(j + 1, end=" ")
    print()

print("--------------------")

# 7. Repeated Number Triangle

print("\n7. Repeated Number Triangle")
for i in range(1, 5):
    for j in range(i):
        print(i, end="")
    print()

print("--------------------")

# 8. Multiplication Table (1 to 5)

print("\n8. Multiplication Table (1 to 5)")
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()

print("--------------------")

# 9. Coordinate Grid (i, j)

print("\n9. Coordinate Grid")
for i in range(1, 4):
    for j in range(1, 4):
        print("(", i, ",", j, ")", end=" ")
    print()

print("--------------------")

# 10. Pyramid Star Pattern

print("\n10. Pyramid Star Pattern")
rows = 4
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

print("--------------------")