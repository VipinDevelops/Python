## Section A 

#A 
 
list = ['vipin',1,'hello',2,4,'world']
nums = [];
strings = [];
for i in  list:
    if(type(i)==int):
       nums.append(i)
    else:
        strings.append(i)

print(nums);
print(strings);
    
#B
# Using *args and **kwargs allows you to create more flexible functions that can handle different numbers of arguments and provide a way to access them within the function bod
def example_function(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)

    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


#  Example function calls
example_function(1, 2, 3, name="John", age=25)

# C 


#D
def swap_numbers(a, b):
    print("Before swapping: a =", a, "b =", b)
    a, b = b, a
    print("After swapping: a =", a, "b =", b)


# Example usage
num1 = 10
num2 = 20
swap_numbers(num1, num2)

#E
def capitalize_alternate_letters(word):
    result = ""
    for i in range(len(word)):
        if i % 2 == 0:
            result += word[i].upper()
        else:
            result += word[i]
    return result


# Example usage
input_word = input("Enter a word in lowercase: ")
capitalized_word = capitalize_alternate_letters(input_word)
print("Capitalized alternate letters:", capitalized_word)


## Section B

#A 


#B 
def replace_vowels_with_asterisk(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    for char in string:
        if char in vowels:
            result += "*"
        else:
            result += char
    return result
input_string = "Hello, World!"
output_string = replace_vowels_with_asterisk(input_string)
print(output_string)

#C 
def get_student_info():
    name = "John"
    age = 20
    grade = "A"
    return name, age, grade

# Call the function and store the returned values
student_name, student_age, student_grade = get_student_info()

# Print the returned values
print("Name:", student_name)
print("Age:", student_age)
print("Grade:", student_grade)

#D
def increment_list_elements(lst, increment_value):
    for i in range(len(lst)):
         lst[i] += increment_value

# Define the list
my_list = [1, 2, 3, 4, 5]

# Call the function to increment the elements by 2
increment_list_elements(my_list, 2)

# Print the updated list
print("Updated List:", my_list)

#E
def my_function():
    x = 10  # Local variable
    print("Inside the function:", x)

my_function()
print("Outside the function:", x)  # Uncommenting this line will cause an error

x = 10  # Global variable

def my_function():
    print("Inside the function:", x)

my_function()
print("Outside the function:", x)


## Section C 

# A ## 
# Create a dictoinary "ODD" of odd number's between 1 and 10, where the key is the decimal number and the value is corresponding number in words. 

ODD = {
    1.0: "one",
    3.0: "three",
    5.0: "five",
    7.0: "seven",
    9.0: "nine"
}

# Display  keys 
for key in ODD.keys():
    print(key)

# Display values 
for Value in ODD.values():
    print(Value)

# Display items 
for items in ODD.items():
    print(items)

# length of the dictionary
print(len(ODD))

#  Check if 7 is present Or not
if 7.0 in ODD:
    print("7 is present in dic")
else:
    print("7 is not present in dic")

# Retrieve the value corresponding to the key 9
value = ODD[9.0]

# Delete the item corresponding to the key 9
del ODD[9.0]


# B ##
# write a function to convert a number entered by the user into its corresponding number in words. For example if the input is 876 the the output should be 'Eight Seven Six'

def convert_number_to_words():
    num = input("Enter a number: ")

    NUMS = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    }

    words = []
    for digit in num:
        words.append(NUMS[digit])

    number_in_words = " ".join(words)
    print(number_in_words)


# Call the function
convert_number_to_words()


# C write a program using a defind function to check if a string is palindrome or not 

def is_palindrome(string):
    # Remove whitespace and convert to lowercase
    string = string.replace(" ", "").lower()

    # Check if the string is a palindrome
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            return False

    return True

# Test the function
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
