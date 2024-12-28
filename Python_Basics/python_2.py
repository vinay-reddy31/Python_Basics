#1.Simple expression evaluation
a=eval(input("Enter Expression:")) # 2+3+3 =>8
print(a)

#2.Converting space-separated input into a list of integers
a=list(map(int,input().split(" ")))
print(a)


#Conditional check for a number
a=10
if(a>2):
    print(1)
else:
    print(2)


# Electricity Bill Calculation based on units consumed

# first 100 units -> No charge
# next 100 units  -> per unit/ 5 rs
# after 200 units -> per unit/ 10 rs

# 350 units curret bill=2000 rs


units=int(input())

if units>200:
    second_hundred=100*5
    remaining_hundred=(units-200)*10
    print(second_hundred+remaining_hundred)

elif units>100 and units<=200:
    units=units-100
    bill=(units*5)
    print(bill)
else:
    print("No Charge")


#Check if a circle fits inside a square
#  radius of a circle
#  length of a square

circle=int(input())
square=int(input())

if((2*circle)<=square):
    print("Circle fit into square")
else:
    print("Circle Doesn't fit into square")


#Checking if a number is Automorphic
n = int(input("Enter Number: "))
if (n < 0):
    print("Invalid Input")

square = n * n
last_digit = square % 10
if (last_digit == n):
    print("Automorphic number")
else:
    print("Not an Automorphic number")


#E-commerce shopping comparison between different platforms
list_n = []

for i in range(9):
    list_n[i] = int(input())

def total(start, end):
    amount = list_n[start]
    discount = list_n[start + 1]
    shipping_charges = list_n[start + 2]
    return (amount - (discount / 100) + shipping_charges)

print("In FlipKart:", total(0, 3))
print("In Snapdeal:", total(3, 6))
print("In Amazon:", total(6, 9))

# E-commerce shopping comparison with discount and shipping charges
list_n = [0] * 9
for i in range(9):
    list_n[i] = int(input())
def total(start, end):
    amount = list_n[start]
    discount = list_n[start + 1]
    shipping_charges = list_n[start + 2]
    return (amount - (amount * (discount / 100)) + shipping_charges)

flipkart = total(0, 3)
snapdeal = total(3, 6)
amazon = total(6, 9)

print("In FlipKart:", flipkart)
print("In Snapdeal:", snapdeal)
print("In Amazon:", amazon)

if (flipkart < snapdeal and flipkart < amazon):
    print("He will prefer Flipkart")
elif (snapdeal < flipkart and snapdeal < amazon):
    print("He will prefer SnapDeal")
else:
    print("He will prefer Amazon")



#BMI calculation and advice based on weight and height
weight=float(input("Enter Weight in kilograms : "))
height=float(input("Enter Height in centimetres: "))

height_to_metres=height/100

bmi=weight/(height_to_metres ** 2)

if (bmi<18.5):
    print("You are underweight. Have an apple daily.")
elif (bmi>=18.5 and bmi<=24.9):
    print("You are normal. Go for a walkevery day and maintain it.")
elif (bmi>25 and bmi<=29.9):
    print("You are overweight. Go to the gym daily.")
else:
    print("You are obese. You need to see a doctor.")


#Stationary shop item purchase and stock management
item_name=input("Enter Product Name: ")
available_items=int(input("Enter Number of Available Items: "))
amount=int(input("Amount: "))
customer_wants=int(input("Enter the No.of products needed: "))

if customer_wants>available_items:
    print("only "+str(available_items)+" items are available")
else:
    print("The Amount for "+str(customer_wants)+" "+item_name+ " is "+str(customer_wants*amount))
    print("Remaining Number of "+item_name+" present in the stock is "+str(available_items-customer_wants))


#Check if a number is Weird or Not based on conditions
n=int(input('Enter a Number: '))
if(n%2!=0):
    print("Weird")
elif (n%2==0 and n>20):
    print("Not Weird")
elif (n%2==0 and 2<=n<=5):
    print("Not Weird")
else:
    print('Weird')

#Check if a topic appears in the list of other topics (Chef problem)
topics = list(map(int, input().split(" ")))
print(topics)
if (topics[3] in topics[:3]):
    print("yes")
else:
    print("No")