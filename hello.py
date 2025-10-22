# CHAPTER 1              MODULE,COMMENTS & PIP
# print("Hello World")
# print(''' Welcome to Anshman codes 
# here are some python codes''')

# CHAPTER 2              VARIABLES AND DATATYPES
# print sum of two number
# a=5
# b=6
# c=a+b
# print(c)

# print sum of two number given by user
# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# c=a+b
# print(c)

# write a python program to find remainder when a no. divided by z
# a=int(input("Enter any number:"))
# z=int(input("Enter z:"))
# b=a%z
# print("remainder is ",b)

# check the type of variable assighned using input function 
# a=3
# b='a'
# print(type(a))
# print(type(b))

# use comparison to find out whether a given variable a is greater than b or not
# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# print("a>b:",a>b)
# print("a<b",a<b)

# write a pyhon program to find average of two number entered by user 
# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# print("Average of a and b is ",(a+b)/2)

# write a program to calculate the sq. of a no. input by user
# a=int(input("Enter no.:"))
# print("Square of a is ",a*a)             #or print("Square of a is ",a**2)  iska matlab a ki power 2


# CHAPTER 3             STRINGS

# a= 'Single quote string'
# b="Double quote string"
# c='''Triple quote string'''
# print(a)
# print(b)
# print(c)

# String slicing
# name = "ANSHMAN"
# sl=name[2:4]
# print(sl)
# sl2=name[0:]
# print(sl2)

# string with skip values
# word="abcdefgh"
# print(word[1:4:2])       #it will print bd

# String function
# a="anshman"
# 1. len(a)  #return 4
# 2. a.endwith("an") #returns true
# 3. a.count("a") #return 2
# 4. a.capatalize() #return Anshman
# 5. a.find("m") #return 4
# 6. a.replace(old word,new word)

#Escape sequence
# \n , \t , \: , etc

# Practice Questions

# 1. Write a python program to display a user entered name followed by Good Afternon using input() function

#  a=str(input("User name:"))
# print(f"Good afternoon {a}")


# 2. write a program to fill in a letter template given below with name and date 
# Dear <name> 
# You are selected!
# <date>

# a=str(input("User name: "))
# b=int(input("Date(dd/mm/yyyy):"))
# print(f'''Dear {a}
# You are selected!
# Date {b}''')

# 3. write a program to detect double space in a string
# name=str(input("Enter any strng to detect double space : "))
# print(name.find("  "))
 
# 4. replace the double space from 3 with single space
# name=str(input("Enter any string to detect double space : "))
# print(name.replace("  "," "))

..............

