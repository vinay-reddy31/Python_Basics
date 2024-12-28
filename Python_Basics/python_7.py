#OOPs concepts

class Dog:
    species = "animal"
class Animal:
    species = "animal"

obj1 = Dog.species
obj2 = Animal.species
print(id(obj1)) #-> 138320621819232
print(id(obj2)) #-> 138320621819232


class Dog:
    species = "animal"
class Animal:
    species = "dog"

obj1 = Dog.species
obj2 = Animal.species
print(id(obj1)) #-> 137085495350432
print(id(obj2)) #-> 137085495350720


class Dog:
    species="Canine"

    def __init__(self,name,age):
        self.name=name
        self.age=age


dog1=Dog("Buddy",5)

print(dog1.species)
print(dog1.name)
print(dog1.age)

#class variables and Instance variables
class Dog:
    # Class variable
    species = "Canine"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# # Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)





class Movie:
    def year(self):
        print("Kalki")
        print("Devara")
        print("Lucky Baskar")


mobile = Movie()
theatre = Movie()
Movie.year(mobile)


class movie:
    def __init__(self):
        print("Devara")
        print("kalki")
        print("Pushpa 2")
mobile=movie()
mobile.__init__()


#class inside class
class python:
    def __init__(self):
        self.id=self.ide()
    class ide:
        def __init__(self):
            print("Devara")
            print("kalki")
            print("Pushpa 2")

        def pycharm(self):
            print("Pycharm")

p=python.ide().pycharm()


# Problem Statement:
# to find all possible permutations in which n people can occupy r seats
# n->people, r->seats

# n friends are planning to go to a movie one among them suggested few movies and all others started to discuss and finally they selected a movie. one among them quickly booked there tickets online, to their suprise they are unable to select their seats.
# All of them got confused then anyhow decided to go to the movie they rushed to reach the theatre again they are suprised there was no one in the theatre. They are the only people to about to watch the movie there is odd no of seats in which n number persons should sit
# In how many ways they shiould sit inside the theatre

# To find the different no of ways in which npeople can occupy r seats

# Input : n r
# 2<=n<=10000
# output: print the total no of ways

# sample: 5 3
# sample out:   60

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

N=list(map(int,input().split()))
n=N[0]
r=N[1]

print(int(fact(n)/fact(n-r)))




class car:
    wheels = '3 wheels'

    def __init__(self):
        self.color = "Blue"
        self.mil = '8 Km'
        self.company = 'BMW'
        self.model = 'x8'
        self.wheels = '5 wheels'

    def update_company(self):
        self.company = "Buggati"

    def update_color(self):
        self.color = 'Pink'


c = car()
print(c.color, c.mil, c.company, c.model, c.wheels)
c.update_company()
print(c.color, c.mil, c.company, c.model, c.wheels)
c.update_color()
print(c.color, c.mil, c.company, c.model, c.wheels)

#class in class
class sports:
    def __init__(self, game1, game2, game3):
        self.game1 = game1
        self.game2 = game2
        self.game3 = game3

    def show(self):
        print(self.game1, self.game2, self.game3)
        self.esports().show()

    class esports:
        def __init__(self):
            self.sport1 = "BGMI"
            self.sport2 = "freefire"
            self.sport3 = "Clash of Clans"
            self.sport4 = "doctor driving"

        def show(self):
            print(self.sport1, self.sport2, self.sport3)


s = sports("cricket", "football", "hocky")
# es=sports.esports()
s.show()

# es=sports.esports()
# es.show()


#Activators and mutators

class student:
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def get_m2(self):  # Activator
        return self.m2

    # mutator
    def set_m2(self, value):
        self.m2 = value


s = student(100, 99, 92)

print(s.get_m2())
s.set_m2(94)
print(s.m2)

#static, classmethod, default
class sru:
    code = 424

    @classmethod
    def info(cls):
        return cls.code

    @staticmethod
    def name_static():
        print("Static method")

    def name(self):
        print("This is SRU")


s = sru()
print(sru.info())
s.name()
s.name_static()


import math as m
n=int(input())
while True:
    x=m.sqrt(n)
    if m.ceil(x)==m.floor(x):
        print(n)
        break

N = int(input("Enter the target point: "))
def can_ravi_reach(N):
    position = 0
    leap = 1
    while position < N:  # Stop if we exceed the target
        position += leap
        if position == N:
            return "YES"
        leap = leap + 1 if leap < 3 else 1  # Cycle through 1, 2, 3
    return "NO"


print(can_ravi_reach(N))