'''
1. If-Else Conditional Statements
a.Write a program that asks the user for a number and prints whether it is positive, negative, or zero.

b.Create a program that checks if a person is eligible to vote (age >= 18).

c.Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".

'''
# a = int(input("enter a number : "))
# if(a > 0):
#     print("positive")
# elif(a==0):
#     print("zero")
# else:
#     print("negative")    


# b = int(input("enter age : "))
# if(b>=18): 
#     print("you can vote")   
# else:
#     print("you cant vote")

# c = int(input("enter a number : "))
# if(c%2==0):
#     print("even")
# else:
#     print("odd")

'''
2. Match Case Statements
a.Ask the user to enter a day number (1-7) and print the corresponding day of the week using match case.

b.Write a program using match case that simulates a simple calculator.
  ->Ask the user for two numbers and an operation (+, -, *, /).
  ->Perform the operation using match case.

'''
# a = int(input("enter day number(1-7) : " ))
# match a :
#   case 1:
#     print("monday")
#   case 2 :
#     print("tuesday")  
#   case 3 :
#     print("wednesday")  
#   case 4 :
#     print("thrusday")  
#   case 5 :
#     print("friday")  
#   case 6 :
#     print("saturday")  
#   case 7:
#     print("sunday")  
#   case _:
#     print("invalid day number")



# a= int(input("enter a number : \n"))
# b = int(input("enter another number : \n"))
# c = input("enter operation(+ - * /) : ")
# match c:
#     case "+":
#         print(a+b)
#     case "-":
#         print(a-b)
#     case "*":
#         print(a*b)
#     case "/":
#         print(a/b)
#     case _:
#         print("dont use spaces")


'''
3. For Loops


a.Print numbers from 1 to 10 using a for loop.
b.Print the multiplication table of a number (entered by user).
c.Calculate the sum of all numbers from 1 to 100 using a for loop.
d.Print the following pattern using a for loop:
*
**
***
****
'''

# for i in range(1,11):
#     print(i)

# a=int(input("enter a number for table : "))
# for i in range(1,11):
#     print(a,"*",i,"is :",a*i)

# a = 0
# for i in range (1,101):
#     a = a+i
# print(a)

# a = int(input("enter a number : "))
# for i in range (1,a+1):
#    print(""*i)
    
'''
4. While Loops
a.Print numbers from 1 to 10 using a while loop.
b.Write a program that keeps asking the user to enter a password until they enter the correct one.
c.Use a while loop to reverse a given number (e.g., 123 → 321).
'''    

# i = 1
# while(i<11):
#     print(i,end=" ")
#     i +=1

# a=int(input("enter password : "))
# while(True):
#     b = int(input("whats the password ? "))
#     if(a==b):
#         print("Correct password")
#         break
#     else:
#         print("wrong password ,  try again")

# a = int(input("enter a number"))
# print(int(str(a)[::-1]))  


'''
5. Break, Continue, and Pass Statements

a.Use a for loop to print numbers from 1 to 10, but stop the loop if the number is 7 (use break).
b.Print numbers from 1 to 10, skipping the number 5 (use continue).
c.Write a loop that goes through numbers 1 to 5, but does nothing for number 3 (use pass).

'''

# for i in range (1,11):
#     if(i==7):
#         break
#     print(i,end=" ")

# for i in range (1,11):
#     if(i==5):
#         continue
#     print(i,end=" ")


# for i in range(1,6):
#     match i:
#         case 1:
#             print(i)
#         case 2:
#             print(2)
#         case 3:
#             pass
#         case 4:
#             print(4)
#         case 5:
#             print(5)


    
