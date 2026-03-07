<<<<<<< HEAD
# =========================================
# Python list Functions Practice
# Author: Veena
# =========================================

#1.To find the length 
l=[1,2,3,4,5,6,7,8,9,10]
print(len(l))

#2.To find the particular value using slice operator
print(l[1:5:1])
print(l[:])
print(l[-1:-5])
print(l[-2:-5:-1])
print(l[1:])

#3.To get a particular index value
print(l.index(5))
print(l.index(4))
print(l.index(10,1))
print(l.index(8,3,8))  

#To add a values in list 
l=[10,20,30,340,40,50,60]
l.append([1,2,3])
print(l)
l.append(100)
print(l)
print(l[7][1])

#To insert a value in list
l=[10,20,30,40,50,60,70,80,90,55,66]
l.insert(3,[1,2,4])
print(l)
#print(l[3][2]) #type error

#To add multiple values
l.append("hello")
print(l)
l.extend("world")
print(l)
l.extend([9,8,2])
print(l)
l.extend(1,2,3)#type error

#To remove a value from the list
l = [10,80,90,40,60,20,70,30]
print(l)
# remove
l.remove(40)
print(l)
# l.remove(100) value error

#  To pop a particular value
l.pop()
print(l)

# syntax---pop(index)
l.pop(1)
print(l)

# To delete a value from certain range
del l[2:4]
print(l)

# To clear a list
l.clear()
print(l)

#  To Replace a value from the list
l = [10,80,90,60,20,70, 30]
print(l)
l[2] = 200
print(l)
# l[8] = 100  Index error

#  to Reverse a list
l = [10,80,90,60,20,70,30]
print(l)
l.reverse()
print(l)

# sorting a list
l = [10,80,90,60,20,70, 30]
print(l)
l.sort()
print(l)
#Reverse printing a sorted list
l.sort(reverse= True)
print(l)

# sorting a list
l = [10,80,90,60,20,70, 30]
print(l)
st = sorted(l)
print(st)

l = [10,80,90,60,20,70, 30]

#To find  Maximum in the list
print(max(l))
# To find minimum in the list
print(min(l))

#TO Copy a list
l = [10,80,90,60,20,70, 30]
cp = l.copy()
print(l)
print(cp)

# Compare
print(l==cp)



# To a value in the list count

l = [1,2,3,6,4,9,7,7,2,9,4,1,1,1]
print(l.count(1))
print(l.count(4))
print(l.count(7))
=======
# =========================================
# Python list Functions Practice
# Author: Veena
# =========================================

#1.To find the length 
l=[1,2,3,4,5,6,7,8,9,10]
print(len(l))

#2.To find the particular value using slice operator
print(l[1:5:1])
print(l[:])
print(l[-1:-5])
print(l[-2:-5:-1])
print(l[1:])

#3.To get a particular index value
print(l.index(5))
print(l.index(4))
print(l.index(10,1))
print(l.index(8,3,8))  

#To add a values in list 
l=[10,20,30,340,40,50,60]
l.append([1,2,3])
print(l)
l.append(100)
print(l)
print(l[7][1])

#To insert a value in list
l=[10,20,30,40,50,60,70,80,90,55,66]
l.insert(3,[1,2,4])
print(l)
#print(l[3][2]) #type error

#To add multiple values
l.append("hello")
print(l)
l.extend("world")
print(l)
l.extend([9,8,2])
print(l)
l.extend(1,2,3)#type error

#To remove a value from the list
l = [10,80,90,40,60,20,70,30]
print(l)
# remove
l.remove(40)
print(l)
# l.remove(100) value error

#  To pop a particular value
l.pop()
print(l)

# syntax---pop(index)
l.pop(1)
print(l)

# To delete a value from certain range
del l[2:4]
print(l)

# To clear a list
l.clear()
print(l)

#  To Replace a value from the list
l = [10,80,90,60,20,70, 30]
print(l)
l[2] = 200
print(l)
# l[8] = 100  Index error

#  to Reverse a list
l = [10,80,90,60,20,70,30]
print(l)
l.reverse()
print(l)

# sorting a list
l = [10,80,90,60,20,70, 30]
print(l)
l.sort()
print(l)
#Reverse printing a sorted list
l.sort(reverse= True)
print(l)

# sorting a list
l = [10,80,90,60,20,70, 30]
print(l)
st = sorted(l)
print(st)

l = [10,80,90,60,20,70, 30]

#To find  Maximum in the list
print(max(l))
# To find minimum in the list
print(min(l))

#TO Copy a list
l = [10,80,90,60,20,70, 30]
cp = l.copy()
print(l)
print(cp)

# Compare
print(l==cp)



# To a value in the list count

l = [1,2,3,6,4,9,7,7,2,9,4,1,1,1]
print(l.count(1))
print(l.count(4))
print(l.count(7))
>>>>>>> a36706ef10ba65c75d53a68ded4ba2eb59376a45
