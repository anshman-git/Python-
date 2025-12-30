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

# CHAPTER 5             LISTS AND TUPLES

# Practice question 
# 1. WAP to store seven fruits in a list entered by the user
# fruits=[]
# f1=input("Enter fruit name: ")
# fruits.append(f1)
# f2=input("Enter fruit name: ")
# fruits.append(f2)
# f3=input("Enter fruit name: ")
# fruits.append(f3)
# f4=input("Enter fruit name: ")
# fruits.append(f4)
# f5=input("Enter fruit name: ")
# fruits.append(f5)
# print(fruits)

# 2. WAP to accept marks of 6 student and display them in a sorted manner
# marks=[]
# m1=int(input("Enter marks: "))
# marks.append(m1)
# m2=int(input("Enter marks: "))
# marks.append(m2)
# m3=int(input("Enter marks: "))
# marks.append(m3)
# m4=int(input("Enter marks: "))
# marks.append(m4)
# m5=int(input("Enter marks: "))
# marks.append(m5)
# marks.sort()
# print(marks)

# 3.Check that a type cannot be changed in python
# a=[1,87,"ansh"]
# a(2)="anshman"          #not possible

# 4. WAP to sum a list with 4 no.
# a = [22,65,44,34]
# print(sum(a))

# 5. Write a program to count the number of zeros in the following tuple
# a=[7,0,8,0,0,9]
# n=a.count(0)
# print(n)

# CHAPTER 5         DICTIONARY AND KEYS
# Dictionary is a collection of keys values pairs.
# Ex. 
# a={"Key":"values",
#    "name":"Ansh",
#    list:[1,2,9]
#    }

# Dictionaries Methods

# Sample={"name":"Anshman",
# "course":"BCA",
# "Section":"A"
# }

# print(Sample.items())
# print(Sample.keys())
# print(Sample.values())

# Sample.update({"name":"Harry"})
# print(Sample.items())

# print(Sample.get("name"))

# Sets
# set is a collection of non repititive elements
# OPERATIONS
# s={2,5,3,8,9}
# 1. len(s)          returns length
# 2. s.remove(2)     remove 2 from set s
# 3. s.clear()       clear the set
# s.union({53})
# s.intersection

# PRACTICE QUESTIONS
# 1. Write a program to create a dictionary of hindi word with values as their English translation.
# also provide user with an option to look it up.
# dic={
#     "madad":"Help",
#     "pani":"Water",
#     "jadu":"Magic"
# }
# word=(input("Enter word:-"))
# print(dic[word])

# 2.Write a program to input eight numbers from the user and display all the unique number at once
# a=int(input("enter number:-"))
# b=int(input("enter number:-"))
# c=int(input("enter number:-"))
# d=int(input("enter number:-"))
# e=int(input("enter number:-"))
# f=int(input("enter number:-"))
# g=int(input("enter number:-"))
# h=int(input("enter number:-"))
# s=set()
# s.add(a)
# s.add(b)
# s.add(c)
# s.add(d)
# s.add(e)
# s.add(f)
# s.add(g)
# s.add(h)
# print(s)

# 3.Create an empty dictionary.Allow 4 times to enter their favorite language
# d={}
# name=input("Enter your name:")
# lan=input("enter your language:")
# d.update({name:lan})
# name=input("Enter your name:")
# lan=input("enter your language:")
# d.update({name:lan})
# name=input("Enter your name:")
# lan=input("enter your language:")
# d.update({name:lan})
# name=input("Enter your name:")
# lan=input("enter your language:")
# d.update({name:lan})
# print(d)

# Chapter 6               Conditional Expressions

# if else and elif in python
# Questions
# 1.Write the program to find the greatest no. entered by the user
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# if(a>b) :
#     print("First number is greater")
# elif(b>a) :
#     print("Second number is greater")    
# else :
#     print("Same")

# 2.Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.
# maths=int(input("Enter maths marks:"))
# chemistry=int(input("Enter chemistry marks:"))
# physics=int(input("Enter physics marks:"))
# total=((maths+chemistry+physics)/3)
# if(total>=40 and physics>=33 and chemistry>=33 and maths>=33) :
#     print("PASS")
# else :
#     print("FAIL")

# 3.A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.
# mess=input("Enter the message:")
# if(mess=="Make a lot of money" or mess=="buy now" or mess=="subscribe this" or mess=="click this") :
#     print("This is spam comment")

# 4.Write a program to find whether a given username contains less than 10 characters or not.
# s=input("Enter username: ")
# l=len(s)
# if(l>10) :
#     print("Usename should be less than 10 words")

# 5.Write a program which finds out whether a given name is present in a list or not.
# l={"anshman","divya","eklavya","mona"}
# name=input("Enter your name :")
# if(name in l) :
#     print("Your name is present in the list")
# else :
#     print("Your name is not present in the list")

# 6.Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

# marks=int(input("Enter your marks"))
# if(marks>=90 and marks<=100) :
#     grade = "A"
# elif(marks>80 and marks<=90) :
#     grade = "B"
# elif(marks>70 and marks<=80) :
#     grade = "C"
# elif(marks>60 and marks<=70) :
#     grade = "D"
# elif(marks>50 ) :
#     grade = "F"
# print("Your grade is :",grade)

# 7.Write a program to find out whether a given post is talking about “Ansh” or not.
# post=input("Enter the post : ")
# if("Ansh".lower() in post.lower()) :
#     print("\"ansh\" is in post")
# else:
#     print("This post is not containing Ansh")


# Chapter 7            LOOPS IN PYTHON

# Types of loops : (a) for loop 
#                  (b) while loop

# print table of 2
# i=1
# for i in range(11) :
#     print(2*i)
#     i+=1

# for loop with else
# l=[1,65,'ansh']
# for i in l:
#     print(i)
# else :
#     print("done")

# break statement
# for i in range(100) :
#     if(i==34) :
#         break #exit from the loop
#     print(i)

# continue statement
# for i in range(100) :
#     if(i==34) :
        # continue  #skip this iteration
#     print(i)

# PRACTICE QUESTIONS 
# 1. Write a program to print multiplication table of a given number using for loop.
# n=int(input("Enter any number:"))
# i=1
# while(i<=10) :
#     print(n*i)
#     i+=1

# 2.Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

# l = ["Harry", "Soham", "Sachin", "Rahul"]
# for name in l :
#     print("Good morning",name)

# 3. Write a program to find whether a given number is prime or not.
# n=int(input("Enter any number:"))
# if(n%2==0) :
#     print("Even number")
# else :
#     print("Odd number")

# 5. Write a program to find the sum of first n natural numbers using while loop.
# n=int(input("Enter any number:"))
# i=1
# sum=0
# while(i<=n) :
#     sum+=i
#     i+=1
# print(sum)

# 6. Write a program to calculate the factorial of a given number using for loop.
# n=int(input("Enter any number:"))
# i=n
# fac=1
# while(i>0) :
#     fac*=i
#     i-=1
# print(fac)

# 7. Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3

# n = int(input("Enter any number: "))
# for i in range(1, n + 1):
#         print(" "*(n-i),end="")
#         print("*"*(2*i-1),end="")
#         print("")

# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3

# n = int(input("Enter any number: "))
# for i in range(1, n + 1):
#         print("*" * i)

# 9. Write a program to print the following star pattern.
# * * *
# *   * for n = 3
# * * *

# n = int(input("Enter any number: "))
# for i in range(1, n + 1):
#         if i == 1 or i == n:
#                 print("* " * n,end="")
#         else:
#                 print("* ",end="")
#                 print("  "*(n - 2),end="")
#                 print("*",end="")
#         print("")

# 10. Write a program to print multiplication table of n using for loops in reversed order.
# n = int(input("Enter any number: "))
# for i in range(1,11):
#         print(f"{n} x {11-i} = {n * (11-i)}")

# CHAPTER 8                        FUNCTIONS 
# function to print hello
# def fun1():
#     print("HELLO")

# write a program to write a code to say good morning to the user 
# def greet() :
#     name=input("Enter user name: ")
#     print(f"Good morning {name}")
# greet()

# TYPES OF FUNCTION 
# 1.Built in function
# 2.User defined function

# FUNCTION WITH ARGUMENT
# def goodday(name) :
#     print(f"Good bye {name}!")
# name=input("Enter your name : ")
# goodday(name)

# RECURSION
# def factorial(n) :
#         if n == 0 or n==1:
#                 return 1
#         else:
#                 return n * factorial(n-1)

# n=int(input("Enter any number : "))
# fac=factorial(n)
# print(f"Factorial of {n} is {fac}")

# PRACTICE QUESTION 
# 1.Write a program using functions to find greatest of three numbers.
# def greatest(a,b,c) :
#     if(a>b and a>c) :
#         return a
#     elif(b>c) :
#         return b
#     else :
#         return c
# a=int(input("Enter a number:"))
# b=int(input("Enter b number:"))
# c=int(input("Enter c number:"))
# great=greatest(a,b,c)
# print(f"Greatest number is {great}")

# 2.Write a python program using function to convert Celsius to Fahrenheit.
# def c_to_f(c) :
#     f=((9/5)*c) + 32
#     return f
# c=int(input("Enter Celsius:"))
# fah=c_to_f(c)
# print(f"Celsius to fahrenheit is {fah}")

#3. How do you prevent a python print() function to print a new line at the end.
# print("")

# 4.Write a recursive function to calculate the sum of first n natural numbers.
# def sum_of_n(n) :
#     if(n==0) :
#         return 0
#     else:
#         return n+sum_of_n(n-1)
# n=int(input("Enter any number :"))
# sum=sum_of_n(n) 
# print(f"Sum of n number is {sum}")

# 5.Write a python function to print first n lines of the following pattern:
# ***
# ** 
# *
# def pattern(n) :
#     for i in range(n,0,-1) :
#         print("*"*i)
# n=int(input("Enter rows number:"))
# pattern(n)
        
# 6.Write a python function which converts inches to cms.
# def i_to_c(inches) :
#     return inches*2.54
# inches=int(input("Enter inches:"))
# cm=i_to_c(inches)
# print(cm)

# 7.Write a python function to remove a given word from a list ad strip it at the same time.
# def remove_word(lst, word):
#         return [item.strip() for item in lst if item.strip() != word]

# lst = input("Enter list items separated by comma: ").split(",")
# word = input("Enter word to remove: ")
# result = remove_word(lst, word)
# print(result)

# 8.Write a program to print multiplication table of n using for loops in reversed order.
# def multiplication_table(n):
#                 for i in range(1, 11):
#                         print(f"{n} x {11-i} = {n * (11-i)}")

# n = int(input("Enter any number: "))
# multiplication_table(n)


# CHAPTER 9                       