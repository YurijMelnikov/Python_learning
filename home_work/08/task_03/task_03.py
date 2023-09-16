import json


phonebook = dict()
exit = None


def save():
    with open("phonebook.json", "w", encoding="utf-8") as pb:
        pb.write(json.dumps(phonebook, ensure_ascii=False))
    print("Изменения в телефонном справочнике сохранены")


try:
    with open("phonebook.json", "r", encoding="utf-8") as pb:
        phonebook = json.load(pb)
    print("Телефонный справочник загружен")
except:
    phonebook = dict()


while True:
    command = input("Введите команду: ")

    if command == "/stop":
        save()
        print("Телефонный справочник закрыт и сохранён")
        break

    elif command == "/add":
        print("Добавление нового контакта или дополнительного телефона к уже существующему")
        name = input("Введите имя контакта: ")
        if name not in phonebook:
            phonebook[name] = list()
            while True:
                phone_number = input(
                    f"Введите номер телефона для контакта {name}: ")
                phonebook[name].append(phone_number)
                save()
                exit = input(
                    f"Хотите добавить ещё один номер телефона для контакта {name} yes/no: ")
                if exit == "no":
                    exit == None
                    break
        else:
            while True:
                phone_number = input(
                    f"Введите номер телефона для контакта {name}: ")
                phonebook[name].append(phone_number)
                save()
                exit = input(
                    f"Хотите добавить ещё один номер телефона для контакта {name} yes/no: ")
                if exit == "no":
                    exit == None
                    break

    elif command == "/replace":
        while True:
            while True:
                name = input(
                    "Введите имя контакта, в котором хотите заменить номер телефона: ")
                if name in phonebook:
                    break
                elif name not in phonebook:
                    print("Такого контакта в телефонном справочнике не существует")
                    exit = input("Хотите повторить ввод? yes/no: ")
                if exit == "no":
                    break
            if exit == "no":
                exit = None
                break
            print(f"Телефоны контакта {name}")
            for i in range(len(phonebook[name])):
                print(f"тел.{i+1}: {phonebook[name][i]}")
            while True:
                try:
                    number = int(
                        input("Какой по счёту номер телефона нужно изменить?"))
                    phone_number = input("Введите новый номер телефона: ")
                    phonebook[name][number - 1] = phone_number
                    save()
                    break                    
                except:
                    print ("Телефона, с таким порядковым номером не существует")
                    exit = input("Хотите повторить ввод? yes/no: ")
                    if exit == "no":
                        break
            if exit == "no":
                exit = None
                break
            exit = input("Хотите изменить ещё один номер телефона? yes/no: ")
            if exit == "no": break
                    

    elif command == "/del":
        while True:
            while True:
                name = input(
                    "Введите имя контакта, который вы хотите удалить: ")
                if name in phonebook:
                    break
                elif name not in phonebook:
                    print("Такого контакта в телефонном справочнике не существует")
                    exit = input("Хотите повторить ввод? yes/no: ")
                if exit == "no":
                    break
            if exit == "no":
                exit = None
                break
            check = int(input(
                "Если хотите удалить все телефоны и сам контакт, введите 1, если удалить один из телефонов контакта, введите 2: "))
            if check == 1:
                del phonebook[name]
                print(f"Контакт {name} удалён")
                save()
                exit = input("Хотите удалить ещё один контакт? yes/no: ")
            if exit == "no":
                exit = None
                break
            if check == 2:
                while True:
                    print(f"Номера телефонов контакта {name}:")
                    for i in range(len(phonebook[name])):
                        print(f"   тел.{i+1}: {phonebook[name][i]}")
                    try:
                        number = int(
                            input("Введите порядковый номер телефона, который хотите удалить: "))
                        del phonebook[name][number - 1]
                        print("Номер успешно удалён")
                        save()
                        exit = input(
                            f"Хотите удалить ещё один телефон контакта {name} yes/no: ")
                        if exit == "no":
                            break
                    except:
                        print(
                            "Номера телефона с таким порядковым номером не существует")
                        exit = input("Хотите повторить ввод? yes/no: ")
                        if exit == "no":
                            break
            if exit == "no":
                exit = None
                break

    elif command == "/show all":
        print("Вывод всего телефонного справочника: ")
        for item in phonebook:
            print(item)
            for i in range(len(phonebook[item])):
                print(f"    тел.{i+1}: {phonebook[item][i]}")

    elif command == "/show all cont":
        print("Имена всех контактов в справочнике и сколько телефонов указано в каждом контакте:")
        for item in phonebook:
            print(f"{item}: {len(phonebook[item])}")

    elif command == "/show cont":
        while True:
            while True:
                name = input("Введите имя контакта: ")
                if name in phonebook:
                    break
                elif name not in phonebook:
                    print("Контакта с таким именем не существует")
                    exit = input("Хотите повторить ввод? yes/no: ")
                if exit == "no":
                    break
            if exit == "no":
                exit = None
                break
            print(f"Телефоны контакта {name}")
            for i in range(len(phonebook[name])):
                print(f"тел.{i+1}: {phonebook[name][i]}")
            exit = input(
                "Хотите вывести телефоны ещё одного контакта? yes/no: ")
            if exit == "no":
                exit = None
                break

    elif command == "/help":
        help = "Список команд\n\
                /show all - вывести весь телефонный справочник\n\
                /show all cont - вывести имена всех контактов и количество телефонов привязанных к ним\n\
                /show cont - вывести телефоны заданного контакта\n\
                /add - добавить в справочник новый контакт или телефон к уже существующему контакту\n\
                /del - удалить контакт или один из номеров телефона в контакте\n\
                /replace - изменить один из номеров телефона в существующем контакте\n\
                /stop - сохранить и закрыть телефонный справочник\n"
        print(help)
    else:
        print("Такой команды не существует, воспользуйтесь справкой /help")