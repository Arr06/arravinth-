def match(str1,str2):
    count=0
    for i in range(min(len(str1),len(str2))):
        if str1[i]==str2[i]:
            count+=1
            return count
str1=input("enter the string1:")
str2=input("enter the string2:")
print(match(str1,str2))
