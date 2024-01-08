a=int(input("num1 :"));
b=int(input("num2 :"));
c=int(input("num3 :"));
if a>b and a>c :
    print("Largest number is",a);
elif b>c and b>a :
    print("largest number is",b);
else :
    print("largest number is",c);
#find the smallest
if a<b and a<c :
    print("smallest number is",a);
elif b<c and b<a :
    print("smallest number is",b);
else :
    print("smallest number is",c);