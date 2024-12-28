#public,private,protected
class student:
    def __init__(self,name,age,roll_no):
        self.name=name  #public
        self._age=age   #protected
        self.__roll_no=roll_no   #private

    def display(self):
        print("Name:",s.name)
        print("Age:",s._age)
        # print("rollno:",s.__roll_no)

    def private(self):
        self.display()

s=student("Kiran",45,123)
s.display()
print(dir(s))
# print(s.__roll_no)
print(s._student__roll_no)



#.............Guess the word...........
string=input()

i=1
s=list(("_"*len(string)))
print(s)
while i<=5:
    n=input("Enter char: ")
    if n in string:
        index=string.index(n)
        s[index]=n
        print(s)
        count=string.count(n)
        string=string.replace(n," ",1)
        print(string)
    i=i+1
print(s)


#.....................stock buy and sell......................
prices=[7,1,5,3,6,4]
prices = [3, 8, 2, 6, 4, 10, 1, 5]
min=min(prices)
length=len(prices)
index=prices.index(min)
max=0
for i in range(index+1,length):
    diff=abs(prices[i]-prices[index])
    if diff>max:
        max=diff
print(max)

# prices = [3, 8, 2, 6, 4, 10, 1, 5]

# Initialize variables to track the minimum price and maximum profit
min_price = float('inf')
max_profit = 0

# Traverse the list
for price in prices:
    if price < min_price:
        min_price = price  # Update the minimum price
    elif price - min_price > max_profit:
        max_profit = price - min_price  # Update the maximum profit

print(max_profit)


#........print the first duplicate character in a string.........
s="ABCDEXYZBAAWQPOOLJ"
a=0
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            c=s[j]
            print(c)
            a=1
            break
    if a==1:
        break

#..........captialize string......
s=input().split()
for i in s:
    print(i[0].upper()+i[1:],end=" ")


#........valid brackets or not..............
def is_valid_brackets(s):
    dict_n = {')': '(',
                  ']': '[',
                  '}': '{'}
    stack = []
    for char in s:
        if char in dict_n.values():
            stack.append(char)
        elif char in dict_n.keys():
            if stack == [] or dict_n[char] != stack.pop():
                return False
    return stack == []


s = "(){}"
print(is_valid_brackets(s))


original_string = input("Enter the string: ").strip()
hidden_string = ["_" for _ in original_string]
print(hidden_string)
attempts = 5

while attempts > 0:
        print(f"Current state: {''.join(hidden_string)}")
        guess = input("Enter a character: ").strip()

        if guess in original_string:
            found = False
            for index, char in enumerate(original_string):
                if char == guess and hidden_string[index] == "_":
                    hidden_string[index] = guess
                    found = True
                    break  # Update only the first occurrence
            if found:
                print("Correct guess!")
            else:
                print("You already guessed that letter!")
        else:
            print("Incorrect guess!")

        if "_" not in hidden_string:
            print(f"You've guessed the word: {''.join(hidden_string)}!")
            break

        attempts -= 1

if "_" in hidden_string:
    print(f"Game over! The word was: {original_string}")

s="ABCDEXYZBAAWQPOOLJ"
a=0
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            c=s[j]
            print(c)
            a=1
            break
    if a==1:
        break



#...Arithmetic progression.....

n=list(map(int,input().split(" ")))
N=int(input())
diff=n[1]-n[0]
first=n[0]

for i in range(1,N):
    first+=diff
print(first)

#print the number of primes between N1 and N2

N1=int(input())
N2=int(input())
c=0
for i in range(N1,N2+1):
    count=0
    for j in range(2,i):
        if i%j==0:
            count+=1
    if count==2:
        c+=1
print(c)


#Rotate the string by L times
S=input()
L=int(input())
print(S[-L:]+S[:-L])

#.........print alphabets in descending order...........

s=input()
seen=set()
for char in s:
    if char not in seen:
        seen.add(char)
    else:
        continue
s="".join(sorted(seen,reverse=True))
print(s)


#.......print number of occurences where A followed by B
#input:  malayalam
# 'a' 'l' => al  => no of occurences=2
input_string = input("Enter the string: ").lower()
A = input("Enter character A: ").lower()
B = input("Enter character B: ").lower()

count = 0
for i in range(len(input_string) - 1):
    if input_string[i] == A and input_string[i + 1] == B:
        count += 1

print(f"Number of occurrences where '{A}' is followed by '{B}': {count}")


#given a number N. print the next immediate prime number
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(n):
    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate

# Input N
N = int(input("Enter a number: "))
print(f"The next immediate prime number after {N} is {next_prime(N)}")
