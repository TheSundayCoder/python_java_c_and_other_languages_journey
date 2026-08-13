#Write a program that prints: Hello, World! Welcome to Python
print("Hello world, welcome to python")


'''Write a program that prints the following poem using a single print() statement:

Twinkle, twinkle, little star,
How I wonder what you are!

'''

print("Twinkle , twinkle , little star , \nHow I wonder what you are!")

'''Q3: Variables & Data Types

Create variables to store:

Your name (string)
Your age (integer)
Your height in meters (float)
A boolean value representing whether you are a student
Print all of them in one line.

'''

name =  "Aditya"
age = 19
height = 1.7
is_student = True
print(name , age , height , is_student)

'''
Q4: Typecasting Practice
num = "45"

Convert it into an integer
Add 10 to it
Print the result
'''

num = "45"
num = int(num)
num += 10
print(num , type(num))


'''
Q5: Taking User Input

Write a program that:

Asks the user for their favorite food.
Prints:
Wow! I also like <food>.


'''

c = input("whats your fav food")  #ek bari me pura string line input ho jayega...
print("wow! i also like ",c , sep = "") 

'''
Q6: Simple Calculator

Write a program that:

Takes two numbers as input from the user.

Prints their:

Sum
Difference
Product
Quotient

'''
a = int(input("enter a number"))
b = int(input("Enter second number"))
print(a+b , a-b , a*b , a//b)


'''
Q7: Escape Sequences

Print the following output using escape sequences:

Hello "Python" World!
This is on a new line.
This is a tab →	    after tab.
'''

print("Hello \"Python\" World!\nThis is on a new line.\nThis is a tab ->\t after tab")

'''
Q8: Operator Challenge

Write a program that:

Takes an integer as input from the user.
Prints the square and cube of that number.
'''

f = int(input("enter a number"))
g = f*f
h = g*f
print("square is",g,"cube is",h)


'''


Q9: Quick Quiz (True/False)
Mark each as True or False:

Python code must always end with a semicolon ;    -> false
The # symbol is used for comments in Python  -> true
"123" and 123 are the same in Python  -> false
The * operator is used for multiplication -> true
\n creates a new line -> true
Variables in Python can start with numbers ->false
int("10") + 5 gives 15 ->true


'''