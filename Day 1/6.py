#Problem 12
roll=767
name="Aakshat"
m1=98
m2=94
m3=97
total=m1+m2+m3
perc=total/3
print("Total Marks Obtained:",total)
print("Percentage:",perc)
if(perc>90):
    print("First Division")
elif(perc>80):
    print("Second Division")
elif(perc>60):
    print("Third Division")
elif(perc>40):
    print("Fourth Division")
elif(perc<40):
    print("Failed")

