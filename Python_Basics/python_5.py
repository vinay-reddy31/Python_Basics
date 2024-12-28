# a p q r s
# a b p q r
# a b c p q
# a b c d p

for i in range(4):
    first = 97
    second = 112
    for j in range(i + 1):
        print(chr(first), end=" ")
        first += 1
    for j in range(4 - i):
        print(chr(second), end=" ")
        second += 1
    print()

#Array Implementation
from array import *
a=array('i',[1,2,3,4,5])
print(a)
print(len(a))

#BufferInfo to get address and length

print(a.buffer_info())

#append
a.append(9)
print(a)

# #extend
a.extend([10,11])
print(a)

# #insert
a.insert(8,12)
print(a)

# #pop -> pop(index)
a.pop()
print(a)

a.pop(6)
print(a)

a.pop(6)
print(a)

a.extend([10,11,13,12,13])
print(a)

# #removes first element from the array
a.remove(13)
print(a)

# #concatenation
a=array('i',[1,2,3,4,5,6])
b=array('i',[7,8,9])
c=a+b
d=array('i',a+b)
print(d)
print(c)


a=array('i',[0,1,2,3,4,5,6])
print("slicing: ",a[0])
print("slicing: ",a[0:])
print("slicing: ",a[2:])
print("slicing: ",a[0:])
print("slicing: ",a[0:12])
print("slicing: ",a[0:12:2])


# #looping
print("Looping: ")
for i in a:
    print(i,end=" ")
print()

arr=array('i',[10,20,30,40])
for i in arr:
    print(i,end=" ")
print()

for i in range(len(arr)):
    print(i,end=" ")
print()

for i in range(len(arr)):
    print(arr[i],end=" ")
print()


# #Dynamic Input to the array
a=array('i',[])
b=array('i',[])
c=array('i',[])

n=int(input("Enter the length of the array: "))

for i in range(n):
    x=int(input("Enter the values: "))
    a.append(x)
    b.extend([x])
    c.insert(i,x)
print(a)
print(b)
print(c)

#find given element is present in array or not
a=array('i',[1,2,3,4,5])
ele=int(input("Enter an element: "))
for i in range(len(a)):
    if a[i]==ele:
        print("index:", i)

import numpy as np
a=np.array([10,20,30,40])
print(a)


import python_5_1
def applications():
    print("Applications")

def lock():
    print("Lock unlocked")

def main():
    lock()
    applications()

if __name__=="__main__":
    main()


#flip binary and print in number format -> Bit Manipulation
n=int(input())
string=""
while(n>0):
    temp=n%2
    string=str(temp)+string
    n=n//2
new_string=""
for i in range(len(string)):
    if string[i]=="0":
        new_string+="1"
    else:
        new_string+="0"
print(int(new_string,2))

#optimised:
n=int(input())
binary=bin(n)[2:]

final="".join("1" if bit=="0" else "0" for bit in binary)
print(int(final,2))


#separate alphabets and numericals and print them in sorted order
a="a7b1r3"
new_str=""
digits=""
for i in a:
    if i.isalpha():
        new_str+=i
    else:
        digits+=i
new_str="".join(sorted(new_str))
digits="".join(sorted(digits))
print(new_str+digits)
