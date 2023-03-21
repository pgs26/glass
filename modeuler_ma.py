def f(x,y):
    return (2-y**2)/(5*x)

def ModifiedEuler(x0,y0,xp):
    n=10
    h=(xp-x0)/n
    for i in range(n):
        if i==0:
            currx=x0
            curry=y0
        
        diff=f(currx,curry)
        newy= curry+h*diff
        
        currx=currx+h
        ytemp=newy
        while(1):
            df=f(currx,ytemp)
            mslp=0.5*(diff+df)
            newytemp=curry+h*mslp
            
            if round(newytemp,4)==round(ytemp,4):
                break
            ytemp=newytemp
        curry=newytemp
    return newytemp

#Find starting values using Modified Euler Method
x=[4,4.1,4.2,4.3]
y=[1]
for i in x[1:]:
    y.append(ModifiedEuler(x[0],y[0],i))

print("\nUsing Modified Euler's method:\n")
for i in range(1,4):
    print("y(",x[i],")=","%.4f"%y[i])

print()

h=0.1

#value to be predicted at
xp=4.4

fl=[]
for i in range(4):
    fl.append(f(x[i],y[i]))
    
    
#Milne Method
print("\nMilne Method:\n")
    
#Predictor
yp=y[0]+(4*h/3)*(2*fl[1]-fl[2]+2*fl[3])
print("Predicted value of y(%.2f)=%.4f"%(xp,yp))

f4=f(xp,yp)

#Corrector
yc=y[2]+(h/3)*(fl[2]+4*fl[3]+f4)
print("Corrected value of y(%.2f)=%.4f"%(xp,yc))


############################


#Adam Bashforth Method
print("\nAdams Bashforth method:\n")

#predictor
yp2=y[3]+(h/24)*(55*fl[3]-59*fl[2]+37*fl[1]-9*fl[0])
print("Predicted value of y(%.2f)=%.4f"%(xp,yp2))

f4_=f(xp,yp2)

#corrector
yc2=y[3]+(h/24)*(9*f4_+19*fl[3]-5*fl[2]+fl[1])
print("Corrected value of y(%.2f)=%.4f"%(xp,yc2))

