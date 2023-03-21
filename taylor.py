from math import e,sin
from sympy import symbols,Derivative

x=symbols('x')
y=symbols('y')

def fact(n):
    pr=1
    for i in range(1,n+1):
        pr=pr*i
    return pr

def getexp(n):
    if n==1:
        expr=x+y*y
    elif n==2:
        expr=sin(x*x)/(1+x*x-y)
    else:
        expr=(e**(x*x-1))/(1+x*y+x**3)
    return expr
    
def f(x_,y_,expr):
    return expr.subs([(x,x_),(y,y_)])
    
print("\nChoose the differential equation:\n")
print("1. y' = x+y^2")
print("2. y' = sin(x^2)/(1+x^2-y)")
print("3. y' = e^(x^2-1)/(1+xy+x^3)")

n=int(input("Enter choice: "))
x0=float(input("Enter x0: "))
y0=float(input("Enter y0: "))

xp=float(input("Enter point at which function value is to be found: "))

exp=getexp(n)
d1=exp
d2=Derivative(exp,x).doit()+Derivative(exp,y).doit()*exp.subs([(x,x0),(y,y0)])
d3=Derivative(d2,x).doit()+Derivative(d2,y).doit()*exp.subs([(x,x0),(y,y0)])
d4=Derivative(d3,x).doit()+Derivative(d3,y).doit()*exp.subs([(x,x0),(y,y0)])
d=[d1,d2,d3,d4]

sol= y0

for i in range(1,5):
    sol+= (1/fact(i))*((x-x0)**i)*f(x0,y0,d[i-1]) 
    
yp=sol.subs(x,xp)

print('\n y(',xp,") = %.4f"%yp)


