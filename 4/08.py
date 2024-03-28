num=int(input())
if(num>=0):
    for i in range(num+1):          #выводов на 1 больше, чем само число
        print(f"Осталось секунд: {num-i}")
print("Пуск")