def check(s,s1):
    if(sorted(s)==sorted(s1)):
        print("the strings are anagram")
    else:
        print("the strings are not anagram")
        
s=input("enter the string:")
s1=input("enter the string:")
check(s,s1)
