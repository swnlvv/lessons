s1=input()
s2=input()

while True:
    if(s1[-1]==s2[0]):
        s1=s2
        s2=input()
    else:
        print(s2)