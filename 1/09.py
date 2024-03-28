login=input()

mail=input()

if "@" in login:

    print("Некорректный логин")

elif "@" not in mail:

    print("Некорректный адрес")

else:

    print("OK")