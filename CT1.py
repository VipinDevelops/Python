## Section A 

## A program to find factors of a whole number using a while loop

number = int(input("Enter a whole number: "))
i = 1
while i <= number:
    if number % i == 0:
        print(i)
    i += 1

## B 

## C Write output of following code 

for i in range (1,11,1):
    print(i,"hello")
else:
    if(i>2):
        print("\n Done")

# output
# 1 hello
# 2 hello
# 3 hello
# 4 hello
# 5 hello
# 6 hello
# 7 hello
# 8 hello
# 9 hello
# 10 hello

x = 19; y =14
print(x ^ y)

#   10011  (19 in binary)
# ^ 01110  (14 in binary)
#   ------
#   11101  (29 in binary)

## D  1. answer B 
## D  2. L and R are often used as variable names to represent the left and right boundaries in different scenarios. 

## E loop will run infinit time

### Section B 

# A   a conditional expression is also known as a ternary operator. It provides a concise way to write conditional statements in a single line.
# syntax :  expression_if_true if condition else expression_if_false

# Code:
x = 10
y = 5

smaller = x if x < y else y

print(smaller)

 
# B 
# Conditional Controlled Loops:

# - These loops are executed based on a condition.
# - The loop continues to execute until the condition evaluates to false.
# - The number of iterations is not predetermined.

i = 0
while i < 5:
    print(i)
    i += 1


# Counter Controlled Loops:

# - These loops are executed a predetermined number of times.
# - The number of iterations is determined by a counter variable.
# - The counter is typically incremented or decremented with each iteration.

for i in range(5):
    print(i)

# C 
n = int(input("Enter the value of n: "))

sum = 0.0

for i in range(1, n+1):
    sum += i / (i + 1)

print("Sum of the series:", sum)


# D 
x = float(input("Enter the base (x): "))
n = int(input("Enter the exponent (n): "))

result = 1

for _ in range(n):
    result *= x

print("Result:", result)

# E 
prime_count = 0
composite_count = 0

while True:
    num = int(input("Enter a number (-1 to exit): "))

    if num == -1:
        break

    if num < 2:
        continue

    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        prime_count += 1
    else:
        composite_count += 1

print("Prime numbers entered:", prime_count)
print("Composite numbers entered:", composite_count)

#### Section C 

# A  
decimal = int(input("Enter a decimal number: "))
binary = bin(decimal)[2:]
print("Binary equivalent:", binary)

# B
 
# 1. 

# 2.
# Example of type casting:

# python
x = 5.7
integer_x = int(x)
print(integer_x)  # Output: 5
# Example of coercion:

# python

x = 5
y = 2.5
result = x + y
print(result)  # Output: 7.5

# C
1. 
for i in range(5, 0, -1):
    print(str(i) * i)

for i in range(2, 6):
    print(str(i) * i)

# Output of pattern:

# 55555
# 4444
# 333
# 22
# 1
# 22
# 333
# 4444
# 55555

# 2.
for i in range(5):
    print(" " * i + "ABCDE"[i:])

# Output of pattern:

# ABCDE
#  BCDE
#   CDE
#    DE
#     E