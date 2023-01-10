while True:
    age = input('Ваш возраст: ')
    name = str(input('Ваше имя: '))

    for i in age:
        if int(age) > 100:
            print(name.capitalize(), "Вы лжёте, в наше время столько не живут... ")
            break
        elif 0 <= int(age) <= 10:
            print("Привет шкет,", name.capitalize())
            break
        elif 10 < int(age) <= 18:
            print("Как жизнь", name.capitalize(), "?")
            break
        elif 18 < int(age) <= 100:
            print("Что пожелаете", name.capitalize(), '?')
            break
    cont = input(' Хотите продолжить? Напишите Y/N:')
    if cont == "n" or cont == "N":
        break
