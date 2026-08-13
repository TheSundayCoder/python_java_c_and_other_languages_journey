#this is  single line comment

''' (triple single quote) multi line comment
gang
this 
is
a 
multiple 
line
comment
'''

'''
escape sequences

used to include special characters in strings

common escape sequences ->
\n : Newline
\t : tab
\\ : Backslash
\" :Double quote
\' : Single quote...and alot more
'''



# print("Hey how are you

#       I am good")  error...we cant terminate a string literal in next line in python

# print("Hey how \\ are \" you \'  \n  \t I am good")

# a = " hi bro"
# print(a)

 
print('Hello   "  World')  #print('hello'world') error due to confusion


#print('hello world' , "harry",5)  #a space is printed between world and harry..its automatic

print("hello world","harry",5,sep=",") #prints , instead of space( ) ..by default sep = space( )

print("aditya",end="pppp")  #end is written at last of the statement (also after sep).....separated by comma, its default value is "\n"
print("sinha",end =    "//")#new line added due to default end = "\n"
 


#print("aditya",end="\n","sinha") it is error
#print("aditya",end="\n",sep = " ;") error

print("adi" , "\\")  #bhai "\\" se ek hi \ print hoga....python rule \\   \"    \'
