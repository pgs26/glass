def f(x,y):
    return (0.5)*(1+x**2)*(y**2)

#prior values
x=[0,0.1,0.2,0.3]
y=[1,1.06,1.12,1.21]

h=0.1

#value to be predicted at
xp=0.4

#Milne Method
print("\nMilne Method:\n")
fl=[]
for i in range(4):
    fl.append(f(x[i],y[i]))
    
#Predictor
yp=y[0]+(4*h/3)*(2*fl[1]-fl[2]+2*fl[3])
print("Predicted value of y(%.2f)=%.4f"%(xp,yp))

f4=f(xp,yp)

#Corrector
yc=y[2]+(h/3)*(fl[2]+4*fl[3]+f4)
print("Corrected value of y(%.2f)=%.4f"%(xp,yc))


#############################


#Adam Bashforth Method
print("\nAdams Bashforthh method:\n")

#predictor
yp2=y[3]+(h/24)*(55*fl[3]-59*fl[2]+37*fl[1]-9*fl[0])
print("Predicted value of y(%.2f)=%.4f"%(xp,yp2))

f4_=f(xp,yp2)

#corrector
yc2=y[3]+(h/24)*(9*f4_+19*fl[3]-5*fl[2]+fl[1])
print("Corrected value of y(%.2f)=%.4f"%(xp,yc2))







