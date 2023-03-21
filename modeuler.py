from math import cos,sin,e

def f(x,y):
    return x+y
    #return x-y+cos(x+y)
    #return (x**2-y**2)/(x**2+y**2)
    #return (e**(x+y))*sin(x*y)
    
x0=float(input("Enter x0: "))
y0=float(input("Enter y0: "))

xp=float(input("Enter point at which function is to be found: "))

n=int(input("Enter number of steps: "))

h=(xp-x0)/n

print("x\t\tdy/dx\tM_Slope\tnew y\n")

for i in range(n):
    if i==0:
        currx=x0
        curry=y0
    
    diff=f(currx,curry)
    newy= curry+h*diff
    
    print("%.4f\t%.4f\t   -   \t%.4f"%(currx,diff,newy))  
    
    currx=currx+h
    ytemp=newy
    while(1):
        df=f(currx,ytemp)
        mslp=0.5*(diff+df)
        newytemp=curry+h*mslp
        
        print("%.4f\t%.4f\t%.4f\t%.4f"%(currx,df,mslp,newytemp))
        if round(newytemp,4)==round(ytemp,4):
            break
        ytemp=newytemp
    print("\nWe take y(",("%.4f"%currx).rstrip('0').rstrip('.'),") = %.4f\n"%ytemp)
    curry=newytemp
