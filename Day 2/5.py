name=input("Enter your name:")
id=int(input("Enter your customer id:"))
units=int(input("Enter units consumed:"))
rate=0
if(units<=199):
    rate=1.2*units
elif(units>200 and units<400):
    rate=1.5*units
elif(units>400 and units<600):
    rate=1.8*units
elif(units>=600):
    rate=2.0*units
print(rate)
if(rate<100):
    rate=0
elif(rate>400):
    rate+=rate*0.15
print("Customer Name:", name)
print("Customer ID:",id)
print("Units Consumed:",units)
print("Electricity Bill:",rate)