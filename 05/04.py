n=int(input())


c=False
for i in range(n):
    s=str(input())
    if "Кот" in s or "кот" in s:
        c=True
        print("МЯУ")
        break

    
if not c:
    print("НЕТ")    