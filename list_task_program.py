# 1. Count the number of even and odd numbers in a list
l = [1,2,3,4,5,6,7,8,9,10]

e_count = 0
o_count = 0

for i in l:
    if i % 2 == 0:
        e_count = e_count + 1
    else:
        o_count = o_count + 1

print("Count of even numbers:", e_count)
print("Count of odd numbers:", o_count)


# 2. Find the largest and smallest number in a list
l = [1,2,3,4,50,66,7,8]

print("Largest number in the list:", max(l))
print("Smallest number in the list:", min(l))


# 3. Remove all negative numbers from the list
l = [1,0,-9,-85,6,7,-2,-4,7,9,6]

positive_list = []

for i in l:
    if i >= 0:
        positive_list.append(i)

print("List after removing negative numbers:", positive_list)
