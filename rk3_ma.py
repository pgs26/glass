def f(x,y):
    return (2*x*y)/(1+x*x)

def RungeKutta(x0,y0,x1):
    h=x1-x0

    k1=h*f(x0, y0)
    k2=h*f(x0+h/2 , y0+k1/2)
    k_pr = h*f(x0+h , y0+k1)
    k3=h*f(x0+h , y0+k_pr)

    k=( k1 + 4*k2 + k3 )/6
     
    y=y0+k
    return y

#Find starting values using RungeKutta method of third order
x=[0,0.1,0.2,0.3]
y=[1]
for i in x[1:]:
    y.append(RungeKutta(x[0],y[0],i))

print("\nUsing Runge Kutta method:\n")
for i in range(1,4):
    print("y(",x[i],")=","%.4f"%y[i])

print()

h=0.1

#value to be predicted at
xp=0.4

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


#############################


#Adam Bashforth Method
print("\nAdams Bashforth method:\n")

#predictor
yp2=y[3]+(h/24)*(55*fl[3]-59*fl[2]+37*fl[1]-9*fl[0])
print("Predicted value of y(%.2f)=%.4f"%(xp,yp2))

f4_=f(xp,yp2)

#corrector
yc2=y[3]+(h/24)*(9*f4_+19*fl[3]-5*fl[2]+fl[1])
print("Corrected value of y(%.2f)=%.4f"%(xp,yc2))


