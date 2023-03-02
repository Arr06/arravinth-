n=int(input("enter the number:"))
rv=0
while n>0:
    rv=rv*10+n%10
    n=n//10
print("reverse of the number:",rv)
