n=int(input())


ans=False
for i in range(n):
    s=str(input())
    if "Кот" in s or "кот" in s:
        c=True

if c:
    print("МЯУ")
else:
    print("НЕТ")