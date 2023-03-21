from math import cos,sin,e

def f(x,y):
    return x-y+cos(x+y)
    #return (x**2-y**2)/(x**2+y**2)
    #return (e**(x+y))*sin(x*y)
    
x0=float(input("Enter x0: "))
y0=float(input("Enter y0: "))

xp=float(input("Enter point at which function is to be found: "))

n=int(input("Enter number of steps: "))

h=(xp-x0)/n

print("\nx\t\ty\t\tdy/dx\tnew y\n")

for i in range(n):
    if i==0:
        currx=x0
        curry=y0
    
    diff=f(currx,curry)
    newy=curry+h*diff
    
    print("%.2f\t%.2f\t%.2f\t%.2f"%(currx,curry,diff,newy))
    
    curry=newy
    currx=currx+h

print("%.2f\t%.2f"%(currx,curry))
print("\nApproximate value of y( %.2f"%xp,") = %.2f"%newy)