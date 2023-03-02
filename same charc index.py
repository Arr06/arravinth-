s1=input("enter the string:")
s2=input("enter the string:")
c=0
b=0
for i in s1:
    for j in s2:
        if(i in j):
            c+=1
        else:
            b+=0
            
print(c)
