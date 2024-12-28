#Abstraction

from abc import ABC,abstractmethod
class S:
    @abstractmethod
    def demo(self):
        pass
    def greet(self):
        print("Good Mrng")

class A(S):
    def demo(self):
        print("hey")
b=A()
b.demo()
b.greet()



from python_9_2 import *
class Bike(vehicle):
    def __init__(self,n,color):
        self.n=n
        self.color=color
    def start(self):
        print("Bike starts with kick")
        print(f"Bike has {self.n} tyres")

class car(vehicle):
    def __init__(self,n):
        super().__init__(n)

    def start(self):
        print(f"car has {self.n} tyres")
        print("car starts with key")
class Auto(vehicle):
    def __init__(self,n):
        super().__init__(n)
        print(f"auto has {self.n} tyres")
    def start(self):
        print('start with chook')

#...................This can be accessed in python_9_1.py file...................


#Bank Application to withdraw and deposit
class Bank:
    def __init__(self,balance=0):
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"{amount} deposited successfully")
        print(f"Current Balance: {self.balance}")

    def withdraw(self,amount):
        if(amount>self.balance):
            print("Insuffienct Balance")
        else:
            self.balance = self.balance - amount
            print(f"{amount} Withdrawn successfully")
            print(f"Current Balance: {self.balance}")


b=Bank()
b.deposit(20000)
b.withdraw(5000)

s = "abbbcdddd"
res = ""
count = 1
for i in range(1, len(s)):
    if (s[i] == s[i - 1]):
        count += 1
    else:
        res += s[i - 1] + str(count)
        count = 1
res += s[-1] + str(count)

print(res)  #=> a1b3c1d4


# Maximum subarray sum

nums=[-4,-2,0,10,41,3,1,5]
current_sum= max_sum=nums[0]

for num in nums[1:]:
    current_sum=max(num,current_sum+num)
    max_sum=max(current_sum,max_sum)
print(max_sum)


# common portion of two strings
def find_common_portion(s1, s2):
    common = ""
    for i in range(1, min(len(s1), len(s2)) + 1):
        if s1[-i:] == s2[:i]:
            common = s1[-i:]
    return common

s1 = "friday"
s2 = "daybreak"

common_portion = find_common_portion(s1, s2)
print(common_portion)



def max_sub_array(nums):
    res = float('-inf')  # Equivalent to Integer.MIN_VALUE in Java
    sum = 0

    for num in nums:
        sum += num
        res = max(res, sum)
        if sum < 0:
            sum = 0

    return res
a=list(map(int,input().split()))
res=max_sub_array(a)
print(res)


s=input()
c=1
res=""
for i in range(0,len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        res+=s[i]+str(c)
        c=1
res+=s[i]+str(c)
print(res)