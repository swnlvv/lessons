def who_are_you_and_hello():
    name = input()
    first_letter=name[0]
    ending=name[1:]
    if not name.isalpha():
        who_are_you_and_hello()   
    elif first_letter.isupper()==False:
        who_are_you_and_hello()
    elif ending.islower()==False:
        who_are_you_and_hello()
    else:
        print(f"Привет, {name}!\n")
