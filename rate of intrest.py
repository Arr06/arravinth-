p=int(input("enter the principle amount:"))
t=int(input("enter the no.of years:"))
s=int(input("enter the age of the citizen:"))
if(s>=60):
    r=12
    si=(p*r*t)/100
    print("the simple intrest is:",si)
else:
    s<60
    r=10
    si=(p*r*t)/100
    print("the simple intrest is:",si)
