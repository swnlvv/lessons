s=input().split()

stack=[]

for x in s:
    if x=='+':
        a=stack.pop()
        b=stack.pop()
        stack.append(a+b)
    elif x=='-':
        a=stack.pop()
        b=stack.pop()
        
        stack.append(b-a)
    elif x=='*':
        a=stack.pop()
        b=stack.pop()
        
        stack.append(a*b)
    else:
        stack.append(int(x))

print(stack[0])