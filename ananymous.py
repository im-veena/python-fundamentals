n=[1,2,3,4]
lap=list(map(lambda a:a*3,n))
print(lap)

n=[1,2,3,4,5,6,7]
lap=list(filter(lambda a:a%2==0,n))
print(lap)

from functools import reduce
n=[1,2,3,4]
lap=reduce(lambda a,b:a+b,n)
print(lap)

from functools import reduce
n=[2,3,4]
lap=reduce(lambda a,b:a*b,n)
print(lap)

n=[1,2,3,4,5,6]
lab=list(filter(lambda a:a%2==0,n))
lap=list(map(lambda a:a*2,lab))
print(lap)

n=[1,2,3,4,5,6]
lab=list(filter(lambda a:a>3,n))
lap=list(map(lambda a:a**2,lab))
print(lap)

n=[1,2,3,4,5,6]
lab=list(filter(lambda a:a%2==0,n))
lap=reduce(lambda a,b:a+b,lab)
print(lap)

n=[1,2,3,4,]
lab=list(filter(lambda a:a>2,n))
lap=reduce(lambda a,b:a*b,lab)
print(lap)

n=[1,2,3,4,5]
lab=list(filter(lambda a:a%2==1,n))
lap=list(map(lambda a:a+5,lab))
print(lap)

i=['apple','banana','cherry']
l=list(map(lambda a:a.upper(),i))
print(l)

i=['HELLO', 'WORLD', 'PYTHON']
l=list(map(lambda a:a.lower(),i))
print(l)

i=['apple', 'dog', 'ant', 'cat', 'anchor']
l=list(filter(lambda a:a.startswith("a"),i))
print(l)


l=['apple', 'banana', 'mango']
c="fruit_"
l=list(map(lambda a:c+a,l))
print(l)

i=['apple', 'dog', 'ant', 'cat', 'anchor']
l=list(filter(lambda a:"o" in a,i))
print(l)

i=['cat', 'elephant', 'dog', 'tiger', 'bat']
l=list(filter(lambda a:len(a)>4,i))
print(l)

i=['hi', 'hello', 'cat']
l=list(filter(lambda a:len(a),i))
t=reduce(lambda a,b:len(a)+len(b),l)
print(t)