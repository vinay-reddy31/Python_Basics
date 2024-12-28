
#add prime numbers to the series
n=int(input())
prime=[]
for i in range(3,n+1):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if(count==2):
        prime.append(i)
print("prime:",prime)

temp = prime[0]
for i in range(1):
    for j in range(1,len(prime)):
        print(temp, end=" ")
        temp = temp + prime[j]


#2. pattern
#         1
#       1 2 3
#     1 2 3 4 5
#   1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8 9

n = int(input())
for i in range(1, n + 1):
    temp = 1
    print("  " * (n - i), end="")
    for j in range(i + i - 1):
        print(temp, end=" ")
        temp = temp + 1

    print()

import python_6_functions as t

n=[1,3,2,5,4]
t.length(n)
t.sum(n)
t.maximum(n)
t.minimum(n)



#find the no of occurences of the character
S=input("Enter String: ")
N=len(S)
C=input("Enter Character: ")

count=0
for i in S:
    if i==C:
        count+=1
print(count)


#even odd
array=[12,2,23,25,5]
n=len(array)
new_lst=""
for i in array:
    if i%2==0:
        new_lst+="even"
    else:
        new_lst+="Odd"
print(new_lst)


a = [5,5,6,7,7,7]
b = set(a)
def test(lst):
    if lst in b:
        return 1
    else:
        return 0
for i in  filter(test, a):
    print(i,end=" ")


#sum of all indices - xor of all even indices
n=6
arr=[1,2,3,4,5,6]

sum=0
xor=0
for i in range(n):
    if(i%2==0):
        xor=xor^arr[i]
    else:
        sum+=arr[i]
print(sum-xor)


# opposite number of a given number in dice
dict_a={1:6,2:5,3:4,4:3,5:2,6:1}
n=int(input())

print(dict_a[n])
