num=int(input("enter the number:"))
m=str(num)
a=m[:len(m)//2]
b=m[len(m)//2:]
c=int(a)+int(b)
d=c**2
if(d==num):
    print(num,"is a tech number")
else:
    print(num,"is not a tech number")
