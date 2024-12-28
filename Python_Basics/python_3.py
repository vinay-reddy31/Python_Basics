# 1. Sequence generation with increments
a=3
b=4
while(a<=100):
    print(a)
    a=a+b
    b=b+2


# 2. Distribute chocolates with stock limit
n = 10
give = int(input("Enter how many: "))
if (give <= n):
    for i in range(1, give + 1):
        print(str(i) + " chocolates")
else:
    for i in range(1, n + 1):
        print(str(i) + " chocolates")
    print(str(give - n) + " out of stock")


# 3. Optimized chocolate distribution with stock limit
n = 10
give = int(input("Enter how many: "))
for i in range(1, min(give, n) + 1):
    print(str(i) + " chocolates")

if (give > 10):
    print(f"{give - n} out of stock")


# 4. Optimized chocolate distribution with stock limit using while loop
n = 10
give = int(input("Enter how many: "))
i = 1
while (i <= give):
    if (i <= n):
        print(f"{i} chocolates")
        i = i + 1
    else:
        print(f"{give - n} chocolates")
        break


# 5. Optimized chocolate distribution with out of stock check
available = 10
n = int(input("Enter how many chocolates: "))
for i in range(1, n + 1):
    if (i > available):
        print(str(n - available) + " out of stock ")
        break

    print(str(i) + " chocolates")


# 6. Jar containing chocolates with stock depletion
n=200
while(n!=0):
    give=int(input("Enter input: "))
    n=n-give
    if(n<=0):
        print("Out of stock")
        break


# 7. Accenture - Filter and process list with conditions
list_n=[12,75,150,180,145,525,50]
new_list=[]
for i in list_n:
    if(i>200):
        break
    if(i>150):
        continue
    if(i%5==0):
        new_list.append(i)
print(new_list)


# 8. Sum of elements at even indices in a list
A = [10, 20, 30, 40, 50, 60]
n = 6
sum = 0
for i in range(n):
    if (i % 2 == 0):
        sum += A[i]

print(sum)

# 9. Print all pairs in a list
list_n=[1,2,3,4,5]
for i in range(len(list_n)):
    for j in range(i+1,len(list_n)):
        print(list_n[i],list_n[j])


# 10. Print pairs whose product is divisible by 3
list_n=[1,2,3,4,5]
for i in range(len(list_n)):
    for j in range(i+1,len(list_n)):
        product=list_n[i]*list_n[j]
        if(product%3==0):
            print(list_n[i],list_n[j])


# 11. Right-angle triangle pattern with stars
for i in range(5):
    # print("*"*(5-i),end="")
    print("* " * (i + 1))

# 12. Inverted right-angle triangle pattern with stars
for i in range(5):
    for j in range(5 - i):
        print("", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()

# 13. General template for patterns printing right-aligned stars
for i in range(5):
    for j in range(i+1):
        print("",end=" ")
    for j in range(5-i):
        print("*",end=" ")
    print()


# 14. Printing numbers from 1 to n in a triangular pattern
for i in range(5):
    a=1
    for j in range(i+1):
        print(a,end=" ")
        a=a+1
    print()

# 15. Printing alphabets in a triangular pattern
b=65
for i in range(5):
    for j in range(i+1):
        a=chr(b)
        print(a,end=" ")
        b=b+1
    print()


# 16. Complex pattern printing with stars and spaces
j = 5
print(" " * 6, end="")
print("*")
for i in range(5):
    print(" " * (5 - i), end="")
    print("* " * (i + 2))

for i in range(3):
    print("  " * 2, end="")
    print(" *" * 2)

for i in range(2):
    print("* " * 7)
