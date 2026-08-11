#in python, variables are used to store data that can be used and manipulated throughout a program .
#A variable is created the moment you 
#assign a value to it using the
#assignment operator(=).

age = 34 #variable , integer datatype
name = "harry" #string
cgpa = 4.55 #float

# Rules of defining a variable in Python
# Variables name must start with a letter (a-z,A-Z) or an underScore(_)
# they can contain letter number and underscore only
# variable names are case sensitive(age and Age are different)
# Avoid using python keywords (eg. if , for , while) as variable names.
#No SPECIAL CHARACTERS LIKE #$%^&*! ..only _ underscore is accepted.
#a_b_c_7 = "hello"   -> valid
#7hiihi  = "hi"    -> invalidddd

#python supports several built in data types:
 
#   integers (int )
#   floats ( float)
#   Strings (str)
#   Booleans( bool):True / False   not true/false
#   Lists : Ordered , immutable collections (eg. [1,2,3])
#   tuples: ordered , immutable collections (eg. (1,2,3))
#   sets: unordered collections of unique elements ( eg. {1,2,3})
#   Dictionaries : key-value pairs (eg. {"name" : "alice" , "age": 25})  

age = 24
print(age)
print(type(age))


name = "harry"
print(name)
print(type(name))

cgpa = 9.9
print(cgpa)
print(type(cgpa))

is_completed = True #can also be False
print(is_completed)  #output -> true
print(type(is_completed))
