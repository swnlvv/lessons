def ask_password():
    first=input()
    if first=='password':
        print('Пароль принят')
    else:
        second = input()
        if second=='password':
            print('Пароль принят')
        else:
            third = input()
            if third=='password':
                print('Пароль принят')
            else:
                print("В доступе отказано")
    