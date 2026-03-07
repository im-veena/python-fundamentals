# =========================================
# Python Jump Statements Practice
# Author: Veena
# =========================================


# =========================================
# 1. Break Statement Example
# =========================================

for i in range(1,11):
    if i == 6:
        break
    print(i)



# =========================================
# 2. Break Practice Program
# Stop loop when number becomes 5
# =========================================

for i in range(1,10):
    if i == 5:
        break
    print("Number:",i)



# =========================================
# 3. Continue Statement Example
# Skip number 5
# =========================================

for i in range(1,11):
    if i == 5:
        continue
    print(i)



# =========================================
# 4. Continue Practice Program
# Print only odd numbers
# =========================================

for i in range(1,11):
    if i % 2 == 0:
        continue
    print("Odd Number:",i)



# =========================================
# 5. Pass Statement Example
# =========================================

for i in range(1,6):
    if i == 3:
        pass
    print(i)



# =========================================
# 6. Pass in Function
# =========================================

def future_function():
    pass



# =========================================
# 7. Break with While Loop
# =========================================

i = 1
while True:
    print(i)
    if i == 5:
        break
    i = i + 1



# =========================================
# 8. Continue with While Loop
# Skip multiples of 3
# =========================================

i = 0
while i < 10:
    i = i + 1
    if i % 3 == 0:
        continue
    print(i)



# =========================================
# 9. Practice Program
# Stop when number is divisible by 7
# =========================================

for i in range(1,20):
    if i % 7 == 0:
        print("Divisible by 7 found:",i)
        break
    print(i)



# =========================================
# 10. Practice Program
# Skip numbers divisible by 4
# =========================================

for i in range(1,21):
    if i % 4 == 0:
        continue
    print(i)
