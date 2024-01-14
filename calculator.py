x=int(input("enter num1 :"))
y=int(input("enter num2 :"))
op=input("enter op :")
if op == '+' :
    print(x+y)
elif op == '-':
    print(x-y)
elif op == '*':
    print(x*y)
elif op == '/' :
    print(x/y)
elif op == '%' :
    print(x%y)
else :
    print("not a valid operator")