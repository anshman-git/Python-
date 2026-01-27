# calculator 

try:
    a=int(input("Enter number :"))
    b=input("Enter operator:")
    c=int(input("Enter second number:"))
    if(b=='+') :
        print(a+c)
    elif(b=='-') :
        print(a-c)
    elif(b=='*') :
        print(a*c)
    elif(b=='/') :
        print(a/c)
    else :
        print("Enter only +,-,*,/")
except ValueError:
    print("Enter valid operations and number.")
