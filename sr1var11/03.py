count = -1
ans = ''
while True:
    line = input().split(sep="; ")
    count+=1
    if '100500' in line:
        break
    else:
        return_line=list()
        num = line[0]
        for number in line:
            if int(number)%int(num)==0:
                
                return_line.append(int(number))
        return_line=set(return_line)
        return_line=list(return_line)
        
        return_line.sort(reverse=False)
        
        return_line.pop(0)
        for elem in return_line:
            ans+=str(elem)+' '
        if count%2==0:
            ans+=str(return_line[-1])
        else:
            ans+=str(return_line[0])
        ans+='\n'

ans=ans.rstrip()

print(ans)