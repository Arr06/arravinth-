s=input("enter the string:")
c="".join (sorted(s))
for i in range(len(c)-1):
    if c[i]==c[i+1]:
        rc=c.index(c[i])
        print("sorted string:",c)
        print("starting index:",rc)
        break
else:
    print("no repeated char found in string")
