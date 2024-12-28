#print count of odd and even numbers
even=0
odd=0
list_n=[1,2,3,4,5]
for i in list_n:
    if(i%2==0):
        even+=1
    else:
        odd+=1
print(even)
print(odd)

#function default arguments
def addition(c, a, b=5, d=9):
    add = a + b + c + d
    print(add)

addition(1, 2)
addition('a', 'b', 'c', 'd')


#args
def sum_numbers(*args):
    total=0
    for num in args:
        total+=num
    print(f"Numbers provided {args}")
    print(f"sum: {total}")

sum_numbers(1,2,3,4,5)
sum_numbers(1,2,3)
sum_numbers()

#kwargs
def print_user_info(**kwargs):
    print('user Info:')
    for key,value in kwargs.items():
        print(f"{key.capitalize()} : {value}")

print_user_info(name="John", age=25, city="New York")
print_user_info(username="jdoe", email="jdoe@example.com")
print_user_info()


# birds->2 legs and animals->4 legs
# head and leg count of both birds and animals
# 27 -> total count of birds and animals
# 84 -> total legs count of birds and animals

head_count=int(input())
leg_count=int(input())

for birds in range(head_count+1):
    animals=head_count-birds   # y=27-x
    if 2* birds+4 *animals==leg_count:   #2x+2y=84  => substitute y => 2x + 2(27-x)=84
        print(f"Number of birds: {birds}")
        print(f"Number of animals: {animals}")
        break



# 4 Input
# print this
# 4 4 4 4
# 4 3 3 4
# 4 3 3 4
# 4 4 4 4

n=int(input())
print((str(n)+" ")*n)
for i in range(n-2):
    print(str(n)+" "+((str(n-1)+" ")*(n-2))+str(n))
print((str(n)+" ")*n)

#6 input
# 6 6 6 6 6 6
# 6 5 5 5 5 6
# 6 5 4 4 5 6
# 6 5 4 4 5 6
# 6 5 5 5 5 6
# 6 6 6 6 6 6

#lambda
print("Lambda function")
a=[1,2,3,4,5,6,7,8]
add=lambda a,b:a+b
print(add(3,4))

#filter
a=[1,2,3,4,5,6,7,8]
even=list(filter(lambda i:i%2==0,a))
print(even)


#map
b=[1,2,3,4,5,6,7,8]
cubes=list(map(lambda i:i**3,b))
print(cubes)

#reduce
from functools import *
sum=reduce(lambda a,b:a+b,b)
print(sum)


#change sign
a=int(input())
print(-a)

#4. count of common characters
s1=set(input())
s2=set(input())
s1=set(s1)
count=0
for i in s2:
    if i in s1:
        count+=1
print(count)

# 5.reverse a string S upto _
# Eg: abcd_pqrs ->dcba_pqrs

s=input()
count=0
for i in s:
    if i=='_':
        break
    else:
        count+=1

print((s[:count:][::-1]+s[count:]))

# optimised
s = input()
count = s.find('_')
print(s[:count][::-1] + s[count:])


#6. s="5A11" -> 16

s=input()
count=0
for i in s:
    if i.ischar():
        break
    else:
        count+=1

a=s[:count]
b=s[count+1:]
char=s[count]

if(char=='A'):
    print(int(a)+int(b))
elif char=="S":
    print(int(a)-int(b))
elif char=="M":
    print(int(a)*int(b))
elif char=="D":
    print(int(a)/int(b))


#coding Test
# Description:
# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
# Note: The second largest element should not be equal to the largest element.

# Constraints:
# 2 ≤ arr.size() ≤ 105
# 1 ≤ arr[i] ≤ 105

# Examples:
# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34

l = list(map(int, input().split()))
s = set(l)
r = list(s)
r.sort()
if len(r) < 2:
    print(-1)
else:
    print(r[-2])