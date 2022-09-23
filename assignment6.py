# (question-1).........................................
# n1=int(input("Enter n1 : "))
# if n1>0:
#     print("Positive")
# else:
#     print("Non-positive")


# (question-2)........................................
# n2=int(input("Enter n2 : "))
# if n2%5==0:
#     print("Divisible")
# else:
#     print("Non-divisible")


# (question-3).........................................
# n3=int(input("Enter n3 : "))
# if n3%2==0:
#     print("Even")
# else:
#     print("Odd")


# (question-4).........................................
# a=int(input("Enter a : "))
# b=int(input("Enter b : "))
# if a>b:
#     print("a greater than b")
# elif a==b:
#     print("Even")
# else:
#     print("b is greater than a")


# (quetion-6)............................................
# n4=(input("Enter n1 : "))
# if len(n4)==3:
#     print("three digit number")
# else:
#     print("not three digit number")


# (question-7)...........................................
# n1=int(input("Enter n1 : "))
# if n1>0:
#     print("Positive")
# elif n1<0:
#     print("negative")
# else:
#     print("zero")


# (question-8)..........................................
# import math
# a,b,c=int(input("Enter a : ")),int(input("Enter b : ")),int(input("Enter c : "))
# d=b**2-4*a*c
# # print(type(x1),type(x2))
# # print(x1,x2)
# if d>0:
#     x1=((-b)+((d)**0.5))/2*a
#     x2=((-b)-((d)**0.5))/2*a
#     print("bothe are real and distinct number : x1=%.2f and x2=%.2f"%(x1,x2))
# elif d==0:
#     x1=((-b)+((d)**0.5))/2*a
#     print("both are equal roots : x1=%.2f"%x1)
# else: 
#     x1=x2=((-b)+((d)**0.5))/2*a
#     imaginary=math.sqrt(-d)/2*a
#     print("imaginary root : x1=.%2f+%.2f and x2=.%2f-%.2f"%(x1,imaginary,x2,imaginary))


# (question-9)...................................................
# year=int(input("Enter year : "))
# if year%4==0:
#     if year%100!=0:
#         print(year,"Leap year")
#     else:
#         print(year,"not a Leap year")
# elif year%400==0:
#     print(year,"Leap year")
# else :
#     print(year,"not a Leap year")

# (question-10)...................................................
# a=int(input("Enter a : "))
# b=int(input("Enter b : "))
# c=int(input("Enter c : "))
# if a>b:
#     if a>c:
#         print("a greater than b and c : ",a)
#     else:
#         print("c is greeater than a and b: ",c)
# elif b>c:
#     print("b is bigger than c  and a: ",b)
# else:
#     print("c is greater than b and a : ",c)


# (question-11)........................................................
# month=int(input("Enter month : "))
# if month in (1,3,5,7,8,10,12):
#     number_of_days=31
#     print("month %d is having "%(number_of_days),"number of days")
# elif month in (4,6,9,11):
#     number_of_days=30
#     print("month %d is having "%(number_of_days),"number of days")
# elif month==2:
#         year=int(input("Enter year : "))
#         if (year%400 & year %100 !=0) or (year%4==0):
#             number_of_days=29
#             print("Number of days in month %d : "%(number_of_days))
#         else:
#             number_of_days=28
#             ("Number of dats in month %d : "%(number_of_days))
# else:
#     print("Invalid month")


# (question-12)...........................................................
from cmath import sqrt
import math
m,n=int(input("Enter m : ")),int(input("Enter n : "))
z=complex(m,n)
print("the real part of complex number : ",z.real)
print("the imaginary part of the complex number : ",z.imag)
if z.real > z.imag:
    print(z.real,"is greater than",z.imag)
else:
    print(z.imag,"is greater than",z.real)