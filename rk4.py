from math import sin,cos,e

def f1(x,y):
    return x*y + x - y**3

def f2(x,y):
    return sin(x) + e**(x**2 - 2*y)

def f3(x,y):
    return cos(x+y) + x**2 - (x*y)

def f(ch,x,y):
    if ch==1:
        return f1(x,y)
    elif ch==2:
        return f2(x,y)
    else:
        return f3(x,y)
   
print("\nChoose the differential equation:\n")
print("1. y' = xy + x - y^3\n2. y' = sin x + e^(x^2 - 2y) \n3. y' = cos(x + y) + x^2 -xy")

ch=eval(input("Enter your choice : "))

x0=eval(input("Enter x0 : "))
x1=eval(input("Enter x1 : "))
y0=eval(input("Enter y0 : "))

h=x1-x0

k1=h*f( ch, x0, y0)
k2=h*f( ch, x0+h/2 , y0+k1/2)
k3=h*f( ch, x0+h/2 , y0+k2/2)
k4=h*f( ch, x0+h   , y0+k3 )

k=( k1 + 2*k2 + 2*k3 + k4  )/6

#print(k)
y=y0+k

print("\nThe required approximate value of y  : ",round(y,3))

