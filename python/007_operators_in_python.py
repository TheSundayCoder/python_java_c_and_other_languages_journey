a = 33
b = 2

#1.arithematic operators   + - * / , %(modulus) , **(exponentiation) , //(floor division)

print("a+b= ",a+b)
print("a-b= ",a-b)
print("a*b= ",a*b)
print("a/b= ",a/b)
print("a%b= ",a%b) #remainder

print("a**b= ",a**b)  #a to the power b

print("a//b= ",a//b)  # a//b means ignoring decimal part...33//2 = 16

#comparision operator ->always return true or false  > < == >= <= ....(not = its assignment)
print(a==34)
print(a==33) #is a equal to 33?
print(a>4)
# print(b<a)
# print(b>34)
# print(a>=4)
# print(b<=2)
print(a !=33) #Is a not equal to 33? -> false, a = 33


#logical operators -> and , or , not ...operate on boolean

'''
print(true and false) -> false
print(true or false) -> true
print(not true ) -> false
'''
c = True
d = False
print("logical operators")
print(c and d)
print(c and c)
print(d and d)  
#print(false and false) -> false
print(d and c) 


print("for or logical operator")
print(True or False)
print(False or True)
print(True or True)
print(False or False)


print("for not operator")
print(not(True)) 
print(not(False))
#error print(!(true))


#assignment operators = , += , -= , *= , /= , **= , //=
print("assignment operators")

c = 32
d = 2
print(c)
c += 3
print(c)

c **= 2
print(c) #35 squARE
d *= 45
print(d)

#membership operators and identity operator covered later after lists