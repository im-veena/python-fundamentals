# =========================================
# Python Dictionary Functions Practice
# Author: Veena
# =========================================

# Create dictionary
d = {"id":101, "name":"Veena", "salary":25000}
print(d)
print(type(d))

# length
print(len(d))


# get particular value
print(d["name"])

# using get()
print(d.get("salary"))


# add value
d["city"] = "Chennai"
print(d)

# update value
d["salary"] = 30000
print(d)


# update multiple values
d.update({"dept":"IT", "age":22})
print(d)


# remove value using pop
d.pop("age")
print(d)

# remove last inserted value
d.popitem()
print(d)


# copy
cp = d.copy()
print(cp)

# compare
print(d == cp)


# check key present or not
print("name" in d)
print("phone" in d)

print("name" not in d)
print("phone" not in d)


# get only keys
print(d.keys())

# get only values
print(d.values())

# get both key and value
print(d.items())


# clear dictionary
# d.clear()
# print(d)


# =========================================
# LOOPING DICTIONARY
# =========================================

d = {"id":101, "name":"Veena", "salary":25000, "city":"Chennai"}

print("------Keys------")
for k in d:
    print(k)


print("------Values------")
for v in d.values():
    print(v)


print("------Key & Value------")
for k,v in d.items():
    print(k,"-",v)


print("------Enumerate------")
for i in enumerate(d):
    print(i)


print("------Enumerate with index------")
for i,k in enumerate(d):
    print(i,"-",k)


print("------Enumerate key and value------")
for i,(k,v) in enumerate(d.items()):
    print(i,"-",k,"-",v)