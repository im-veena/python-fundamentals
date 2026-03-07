# 1. Slice a tuple and print the first three elements

t = (1,2,3,4,5,6,7,8)
print("First three elements:", t[0:3])


# 2. Find the sum of all elements in a numeric tuple
t = (1,2,3,4,5,6,7,8,9,10)

total = 0

for i in t:
    if i > 0:
        total = total + i

print("Sum of tuple elements:", total)
