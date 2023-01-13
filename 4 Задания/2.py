age = input('Ваш возраст: ')
name = str(input('Ваше имя: '))

for i in age:
    if int(age) > 100:
        print(name.title(), "Вы лжёте, в наше время столько не живут... ")
        break
    elif 0 <= int(age) <= 10:
        print("Привет шкет,", name.title())
        break
    elif 10 < int(age) <= 18:
        print("Как жизнь", name.title(), "?")
        break
    elif 18 < int(age) <= 100:
        print("Что пожелаете", name.title(), '?')
        break
