#Inheritance
class Animal:
    def __init__(self):
        print("Hi from animal")

    def sleep(self):
        print("Sleeping..")

    def eat(self):
        print("Animal is Eating")

class Dog(Animal):   #Dog inherits Animal
    def bark(self):
        print("barking")

a=Animal()
a.eat()
b=Dog()
b.eat()
b.sleep()
b.bark()


#MultiLevel Inheritance
class Instagram:
    def __init__(self):
        print("Company...")

    def ceo(self):
        print("Mark Zukerburg")

class Operations(Instagram):
    def posts(self):
        print("We can post Images/videos")

    def reels(self):
        print("We can watch reels")

    def likes(self):
        print("We can like Reels")

class all_about_the_company(Operations):
    def about(self):
        self.ceo()
        self.posts()
        self.reels()
        self.likes()

n=all_about_the_company()
n.about()



#Multiple Inheritance
class Dog:
    def bark(self):
        print("Dog is Barking")
class Cat:
    def meow(self):
        print("Cat is Meow")


class Pets(Dog,Cat):
    def __init__(self):
        print("Pets")

p=Pets()
p.bark()
p.meow()

#Hierarchical Inheritance

class Animal:
    def sleep(self):
        print("Sleeping...")
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Dog is Barking")
class Cat(Animal):
    def meow(self):
        print("Meow from cat")

d=Dog()
d.eat()
d.bark()
c=Cat()
c.sleep()
c.meow()

 #Super Keyword
class A:
    def __init__(self):
        print("This is A class")


class B(A):
    def __init__(self):
        super().__init__()
        print('This is B class')


class C(A, B):
    def __init__(self):
        super().__init__()
        print("This is C class")


c = C()

#Mro Error -> Method Resolution Error
class A:
    def __init__(self):
        print("This is A class")

class B(A):
    def __init__(self):
        super().__init__()
        print('This is B class')

class C(B,A):
    def __init__(self):
        super().__init__()
        print("This is C class")

c = C()

class A:
    def __init__(self):
        print("Iam from A class")

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b


class B:
    def __init__(self):
        super().__init__()
        print("Iam from B class")

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


class c(B, A):
    def __init__(self):
        super().__init__()
        print("Iam from C class")
        print(self.mul(10, 20))

c = c()

# output:
# Iam from A class
# Iam from B class
# Iam from C class
# 200

class c(A, B):
    def __init__(self):
        super().__init__()
        print("Iam from C class")
        print(self.mul(10, 20))

# output
# Iam from A class
# Iam from C class
# 200


#*****************.......................ploymorphism..............................*********



class pycharm():
    def features(self):
        print("Easy to write python code")
        print("code Suggestions")
class vscode():
    def features(self):
        print("Easy Indentation")
        print("Easy Extension Downloading")

class Thonny():
    def features(self):
        print("Easy to install")
        print("syntax Highlighting")

class python():
    def code(self,ide):
        ide.features()

p=python()
ide_name=input("Enter the Ide: ")
ide_instance = eval(ide_name)() #converts string to class name and add the ()
print(ide_instance)
# ide=Thonny()
p.code(ide_instance)

#prime,factorial,fibonacci
import math
class A:
    def __init__(self,n):
        self.n=n
        self.prime(n)
        self.fact(n)
        self.fibonacci(n)

    def prime(self,n):
        print("prime: ",end="")
        for i in range(2,n+1):
            count=0
            for j in range(1,i+1):
                if(i%j==0):
                    count+=1
            if count==2:
                print(i,end=" ")
        print()

    def fact(self,n):
        print("Factorial:",math.factorial(n))

    def fibonacci(self,n):
        prev=1
        prev_2=0
        print("Fibonacci:",end="")
        print(0,end=" ")
        for i in range(2,n+1):
            curr=prev+prev_2
            print(curr,end=" ")
            prev_2=prev
            prev=curr

a=A(5)


# Pangram checking
import string
s = "qwertyuiopasdfghjklzxcvbnm"

s = s.lower()

# Create a set of all alphabet characters
alphabet_set = set(string.ascii_lowercase)

# Create a set from the input string
input_set = set(s)

# Check if all alphabet characters are in the input string
print(alphabet_set <= input_set)


# method overriding
class maths():
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def __add__(self, other):
        s1 = self.m1 + other.m1
        s2 = self.m2 + other.m2
        s3 = self.m3 + other.m3
        s = maths(s1, s2, s3)
        return s

    def __gt__(self, other):
        a = self.m1 + self.m2
        b = other.m1 + other.m2

        if a > b:
            return True
        else:
            return False

    def __str__(self):
        return(self.m1,self.m2,self.m3)


a = maths(99, 90, 70)
b = maths(99, 45, 143)
m = a + b
print(m.m1)
print(m.m2)
print(m.m3)

if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")


#Method overriding
class A:
    def method(self):
        print("Method A")

class B(A):
    pass

a = B()
a.method()


#Method overloading
class student():
    def sum(self,a,b,c,d):
        return a+b+c+d

s=student()
print(s.sum(10,20,30,40))

#BINARY
s=input()
result=int(s[0])
i=1
while(i<len(s)):
    operator=s[i]
    first=int(s[i+1])
    if(operator=="A"):
        result=first&result
    elif operator=="B":
        result=first|result
    else:
        result=first^result
    i+=2
print(result)



s=input()
result=int(s[0])
i=1
while(i<len(s)):
    operator=s[i]
    first=int(s[i+1])
    if(operator=="A"):
        result=first&result
    elif operator=="B":
        result=first|result
    else:
        result=first^result
    i+=2
print(result)

s="LRUD"
x,y=0,0
for i in s:
    if x=="L":
        x-=1
    elif x=="R":
        x+=1
    elif x=="U":
        y+=1
    elif x=="D":
        y-=1
print(x==0 and y==0)


def is_at_same_point(directions):
    x, y = 0, 0  # Starting at (0, 0)

    for move in directions:
        if move == 'L':
            x -= 1
        elif move == 'R':
            x += 1
        elif move == 'U':
            y += 1
        elif move == 'D':
            y -= 1

    # Check if we are back at the starting point
    return 1 if x == 0 and y == 0 else 0


# Input string
directions = "LRUD"
# Check if we return to the starting point
result = is_at_same_point(directions)
print(result)