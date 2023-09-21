import sqlite3
import easygui

#Подключаем базу данных, создаём переменную cursor
try:
    connection = sqlite3.connect('phonebook.db')
    cursor = connection.cursor()
    print("База данных телефонного справочника успешно подключена к SQLite")
except:
    pass

#Создаём две таблицы, контакты и номера телефонов, если таблицы созданы, пропускаем исключение
try:
    contacts_table = '''CREATE TABLE "contacts"(
                            contact_id INTEGER PRIMARY KEY AUTOINCREMENT,                        
                            first_name TEXT NOT NULL,
                            second_name TEXT,
                            surname TEXT,
                            contact_comment TEXT);'''

    cursor.execute(contacts_table)
except:
    pass
try:
    phone_numbers_table = '''CREATE TABLE "phone numbers"(
                            phone_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            phone_number TEXT NOT NULL,
                            whose_phone INTEGER NOT NULL,
                            phone_comment TEXT,
                            FOREIGN KEY (whose_phone)
                                REFERENCES contacts (contact_id));'''

    cursor.execute(phone_numbers_table)
except:
    pass

#Стартовый экран в easygui
def start_screen():
    choices = ["Добавить контакт в телефонный справочник",
               "Добавить номер телефона к существующему контакту",
               "Изменить имя контакта",
               "Изменить номер телефона у определённого контакта",
               "Удалить контакты и связанные с ними номера телефонов",
               "Удалить номер телефона у определённого контакта",
               "Вывести весь телефонный справочник",
               "Вывести телефоны определённых контактов",
               "Закрыть и сохранить телефонный справочник"]
    msg = ""
    title = "Телефонный справочник"
    choice = easygui.choicebox(msg, title, choices)
    if choice == "Добавить контакт в телефонный справочник":
        return 1
    elif choice == "Добавить номер телефона к существующему контакту":
        return 2
    elif choice == "Изменить имя контакта":
        return 3
    elif choice == "Изменить номер телефона у определённого контакта":
        return 4
    elif choice == "Удалить контакты и связанные с ними номера телефонов":
        return 5
    elif choice == "Удалить номер телефона у определённого контакта":
        return 6
    elif choice == "Вывести весь телефонный справочник":
        return 7
    elif choice == "Вывести телефоны определённых контактов":
        return 8
    elif choice == "Закрыть и сохранить телефонный справочник":
        return 0

#Блок с запросами в базу данных

#Добавляем данные в таблицу контакты, на вход принимает список значений
def insert_contact(values: list):
    try:
        contact_insert = '''INSERT INTO "contacts"
                            (first_name, second_name, surname, contact_comment)
                            VALUES (?,?,?,?);'''
        cursor.execute(contact_insert, values)
        connection.commit()
    except:
        pass


#Добавляем данные в таблицу номера телефонов, на вход принимает список значений
def insert_phone_number(values: list):
    try:
        phone_number_insert = '''INSERT INTO "phone numbers"
                                (phone_number,whose_phone,phone_comment)
                                VALUES (?,?,?);'''
        cursor.execute(phone_number_insert, values)
        connection.commit()
    except:
        pass

#Select запрос на все данные из таблицы контакты
def request_contacts():
    request_contact_list = '''SELECT contact_id,\
                                first_name,\
                                second_name,\
                                surname,\
                                contact_comment\
                                from "contacts"'''
    cursor.execute(request_contact_list)
    request_contacts_list = cursor.fetchall()
    return request_contacts_list

#Select запрос в таблицу номера телефонов, по id контакта
def request_phone(contact_id: int):
    request_phone = f'''SELECT phone_id,\
                               phone_number,\
                               phone_comment\
                        FROM "phone numbers"\
                        WHERE whose_phone = {contact_id}'''
    cursor.execute(request_phone)
    request_phone_list = cursor.fetchall()
    return request_phone_list

#Select запрос на все данные из таблицы номера телефонов
def request_all_phones():
    request = '''SELECT *\
                FROM "phone numbers"'''
    cursor.execute(request)
    all_phone_list = cursor.fetchall()
    return all_phone_list


#Запрос на получение данных выбранных контактов, id контактов в списке
def request_specified_contacts(id_contact_list: list):
    request_specified_contacts_list = list()
    for i in range(len(id_contact_list)):
        request = f'''SELECT *\
                     FROM "contacts"\
                     WHERE contact_id = {id_contact_list[i]}'''
        cursor.execute(request)
        request_specified_contacts_list.extend(cursor.fetchall())
    return request_specified_contacts_list


#Запрос на получение данных телефонов, выбранных контактов, id контактов в списке
def request_specified_phone(id_contact_list: list):
    request_specified_phone_list = list()
    for i in range(len(id_contact_list)):
        request = f'''SELECT *\
                     FROM "phone numbers"\
                     WHERE whose_phone = {id_contact_list[i]}'''
        cursor.execute(request)
        request_specified_phone_list.extend((cursor.fetchall()))
    return request_specified_phone_list


#Запрос на удаление телефонов выбранных контактов, id контактов в списке, если id контакта одиночный int, в запросе это обрабатывается
def request_delete_contact_phone(contact_id_list: list):
    if type(contact_id_list) == list:
        for i in range(len(contact_id_list)):
            delete_request_phone = f'''DELETE from "phone numbers"\
                                    WHERE whose_phone = {contact_id_list[i]}'''
            cursor.execute(delete_request_phone)
            delete_request_contact = f'''DELETE from "contacts"\
                                        WHERE contact_id = {contact_id_list[i]}'''
            cursor.execute(delete_request_contact)
    else:
        delete_request_phone = f'''DELETE from "phone numbers"\
                                WHERE whose_phone = {contact_id_list}'''
        cursor.execute(delete_request_phone)
        delete_request_contact = f'''DELETE from "contacts"\
                                    WHERE contact_id = {contact_id_list}'''
        cursor.execute(delete_request_contact)
    connection.commit()


#Удаление телефона по его id
def request_delete_phone(phone_id):
    if type(phone_id) == list:
        for i in range(len(phone_id)):
            delete_request_phone = f'''DELETE from "phone numbers"\
                                        WHERE phone_id = {phone_id[i]}'''
            cursor.execute(delete_request_phone)
    else:
        delete_request_phone = f'''DELETE from "phone numbers"\
                                    WHERE phone_id = {phone_id}'''
        cursor.execute(delete_request_phone)
    connection.commit()


#Изменение контакта, на вход принимается id контакта и список значений для обновления
def request_update_contact(contact_id: int, values: list):
    contact_update = f'''UPDATE "contacts"\
                         SET\
                            first_name = ?,\
                            second_name = ?,\
                            surname = ?,\
                            contact_comment = ?\
                        WHERE contact_id = {contact_id};'''
    cursor.execute(contact_update, values)
    connection.commit()


#Изменение номера телефона, на вход принимается id контакта и список значений для обновления
def request_update_phone(phone_id: int, values: list):
    phone_update = f'''UPDATE "phone numbers"\
                            SET\
                              phone_number = ?,\
                              whose_phone = ?,\
                              phone_comment = ?\
                        WHERE phone_id = {phone_id};'''
    cursor.execute(phone_update, values)
    connection.commit()


#Добавление нового контакта
def add_contact():
    while True:
        msg = "Добавление контакта в телефонный справочник"
        title = "Введите данные контакта, имя является обязательным полем"
        name_values = ["Имя", "Фамилия", "Отчество", "Комментарий"]
        values_contact = easygui.multenterbox(msg, title, name_values)
        if values_contact == None:
            return
        elif values_contact[0] == "":
            selection = question_yes_no(
                "Поле имя не должно быть пустым, желаете повторить ввод?")
            if not selection:
                return
        elif values_contact[0] != "":
            break
    for i in range(len(values_contact)):
        if values_contact[i] == "":
            values_contact[i] = None
    insert_contact(values_contact)
    request_contacts_tuple = request_contacts()
    list_of_choice = get_list_of_choice(request_contacts_tuple)
    try:
        while True:
            values_contact.remove("NULL")
    except:
        pass
    try:
        while True:
            values_contact.remove("")
    except:
        pass
    try:
        while True:
            values_contact.remove(None)
    except:
        pass
    choice = " ".join(values_contact)
    contact_id = get_id(request_contacts_tuple, list_of_choice, choice)
    add_phone_number(contact_id)

#Добавление номера телефона по входящему id контакта
def add_phone_number(contact_id: int):
    while True:
        while True:
            msg = "Добавление номера телефона к контакту"
            title = "Введите номер телефона и комментарий"
            phone_values = ["Номер телефона", "Комментарий"]
            values_phone_numbers = easygui.multenterbox(
                msg, title, phone_values)
            if values_phone_numbers == None:
                return
            elif values_phone_numbers[0] == "":
                easygui.msgbox(
                    "Поле \"Номер телефона\" не должно быть пустым, повторите ввод")
            elif values_phone_numbers[0] != "":
                break
        for i in range(len(values_phone_numbers)):
            if values_phone_numbers[i] == "":
                values_phone_numbers[i] = None
        values_phone_numbers.insert(1, contact_id)
        insert_phone_number(values_phone_numbers)
        values_phone_numbers.clear()
        selection = question_yes_no(
            "Желаете добавить к контакту ещё один номер телефона?")
        if not selection:
            break


#Добавление телефона к существующему контакту
def add_phone_number_to_contact():
    request_contacts_tuple = request_contacts()
    choice_list = get_list_of_choice(request_contacts_tuple)
    sorted_choice_list = choice_list.copy()
    sorted_choice_list.sort()
    if len(sorted_choice_list) == 0:
        easygui.msgbox("Телефонный справочник пуст")
    elif len(sorted_choice_list) == 1:
        choice = sorted_choice_list[0]
        check = question_yes_no(f"В телефонном справочнике только один контакт {choice}\n\
                        Добавить к нему номер телефона?")
        if not check:
            return
        contact_id = get_id(request_contacts_tuple, choice_list, choice)
        add_phone_number(contact_id)
    else:
        choice = easygui.choicebox(
            "Выберите контакт для добавления телефона", "Добавление телефона", sorted_choice_list)
        if choice == None:
            return
        elif choice != None:
            contact_id = get_id(request_contacts_tuple, choice_list, choice)
            add_phone_number(contact_id)


#Изменение данных существующего контакта
def change_contact_name():
    request_contacts_tuple = request_contacts()
    choice_list = get_list_of_choice(request_contacts_tuple)
    sorted_choice_list = choice_list.copy()
    sorted_choice_list.sort()
    if len(sorted_choice_list) == 0:
        easygui.msgbox("Телефонный справочник пуст")
        return
    elif len(sorted_choice_list) == 1:
        choice = sorted_choice_list[0]
        check = question_yes_no(f"В телефонном справочнике только один контакт {choice}\n\
                        Изменить имя контакта?")
        if not check:
            return
    else:
        choice = easygui.choicebox(
            "Переименовать контакт", "Выберите контакт", sorted_choice_list)
        if choice == None:
            return
    contact_id = get_id(request_contacts_tuple, choice_list, choice)
    while True:
        msg = f"Изменение контакта {choice}"
        title = "Внесите изменения, поле имя не должно быть пустым"
        name_values = ["Имя", "Фамилия", "Отчество", "Комментарий"]
        values_contact = easygui.multenterbox(
            msg, title, name_values)
        if values_contact == None:
            return
        elif values_contact[0] == "":
            selection = question_yes_no(
                "Поле имя не должно быть пустым, желаете повторить ввод?")
            if not selection:
                return
        elif values_contact[0] != "":
            break
    for i in range(len(values_contact)):
        if values_contact[i] == "":
            values_contact[i] = None
    request_update_contact(contact_id, values_contact)
    easygui.msgbox(f"Контакт {choice} успешно изменён")


#Изменение телефона у существующего контакта
def change_phone():
    request_contacts_tuple = request_contacts()
    choice_list = get_list_of_choice(request_contacts_tuple)
    sorted_choice_list = choice_list.copy()
    sorted_choice_list.sort()
    if len(sorted_choice_list) == 0:
        easygui.msgbox("Телефонный справочник пуст")
        return
    elif len(sorted_choice_list) == 1:
        choice = sorted_choice_list[0]
        check = question_yes_no(f"В телефонном справочнике только один контакт {choice}\n\
                        Изменить его номер телефона?")
        if not check:
            return
    else:
        choice = easygui.choicebox(
            "Изменить номер телефона у выбранного контакта", "Выберите контакт", sorted_choice_list)
        if choice == None:
            return
    contact_id = get_id(request_contacts_tuple, choice_list, choice)
    while True:
        request_phone_tuple = request_phone(contact_id)
        choice_phone_list = get_list_of_choice(request_phone_tuple)
        if len(choice_phone_list) == 0:
            easygui.msgbox(
                f"У контакта {choice} телефоны в справочнике отсутствуют")
            return
        elif len(choice_phone_list) == 1:
            choice_phone = choice_phone_list[0]
        else:
            choice_phone = easygui.choicebox(
                f"Изменить номер телефона контакта {choice}", "Выберите телефон", choice_phone_list)
            if choice_phone == None:
                return
        while True:
            msg = f"Изменение номера телефона контакта {choice}"
            title = "Введите номер телефона и комментарий"
            phone_values = ["Номер телефона", "Комментарий"]
            values_phone_numbers = easygui.multenterbox(
                msg, title, phone_values)
            if values_phone_numbers == None:
                return
            elif values_phone_numbers[0] == "":
                easygui.msgbox(
                    "Поле \"Номер телефона\" не должно быть пустым, повторите ввод")
            elif values_phone_numbers[0] != "":
                break
        for i in range(len(values_phone_numbers)):
            if values_phone_numbers[i] == "":
                values_phone_numbers[i] = None
        values_phone_numbers.insert(1, contact_id)
        phone_id = get_id(request_phone_tuple, choice_phone_list, choice_phone)
        request_update_phone(phone_id, values_phone_numbers)
        easygui.msgbox("Номер телефона успешно изменён")
        values_phone_numbers.clear()
        if len(choice_phone_list) > 1:
            selection = question_yes_no("Хотите изменить ещё один телефон?")
            if not selection:
                return
        else:
            return


#Удаление контакта и всех телефонов связанных с ним
def delete_contact():
    request_contacts_tuple = request_contacts()
    choice_list = get_list_of_choice(request_contacts_tuple)
    sorted_choice_list = choice_list.copy()
    sorted_choice_list.sort()
    if len(sorted_choice_list) == 0:
        easygui.msgbox("Телефонный справочник пуст")
        return
    elif len(sorted_choice_list) == 1:
        choice = sorted_choice_list[0]
        check = question_yes_no(f"В телефонном справочнике только один контакт {choice}\n\
                        Удалить его?")
        if not check:
            return
        contact_id = get_id(request_contacts_tuple, choice_list, choice)
        request_delete_contact_phone(contact_id)
        easygui.msgbox("Контакт успешно удален")
    else:
        choice = easygui.multchoicebox(
            "Выберите контакты для удаления", "Удаление контактов", sorted_choice_list)
        if choice == None:
            return
        check = question_yes_no(
            "Вы уверены, что хотите удалить выбранные контакты?")
        if check:
            contact_id_list = get_id_list(
                request_contacts_tuple, choice_list, choice)
            request_delete_contact_phone(contact_id_list)
            easygui.msgbox("Выбранные контакты успешно удалены")


#Удаление выбранного номера телефона у существующего контакта
def delete_phone():
    request_contacts_tuple = request_contacts()
    choice_list = get_list_of_choice(request_contacts_tuple)
    sorted_choice_list = choice_list.copy()
    sorted_choice_list.sort()
    if len(sorted_choice_list) == 0:
        easygui.msgbox("Телефонный справочник пуст")
        return
    elif len(sorted_choice_list) == 1:
        choice = sorted_choice_list[0]
        check = question_yes_no(f"В телефонном справочнике только один контакт {choice}\n\
                        Удалить его телефон?")
        if not check:
            return
    else:
        choice = easygui.choicebox(
            "Удалить номер телефона у выбранного контакта", "Выберите контакт", sorted_choice_list)
        if choice == None:
            return
    contact_id = get_id(request_contacts_tuple, choice_list, choice)
    request_phone_tuple = request_phone(contact_id)
    choice_phone_list = get_list_of_choice(request_phone_tuple)
    if len(choice_phone_list) == 0:
        easygui.msgbox(f"У контакта {choice} телефоны отсутствуют")
        return
    elif len(choice_phone_list) == 1:
        choice_phone = choice_phone_list[0]
        phone_id = get_id(request_phone_tuple, choice_phone_list, choice_phone)
        check = question_yes_no(
            f"Удалить телефон {choice_phone} контакта {choice}?")
        if check:
            request_delete_phone(phone_id)
            easygui.msgbox("Телефон успешно удалён")
        else:
            return
    else:
        choice_phone = easygui.multchoicebox(
            f"Удаление номеров телефона контакта {choice}", "Выберите телефоны", choice_phone_list)
        if choice_phone == None:
            return
        phone_id_list = get_id_list(
            request_phone_tuple, choice_phone_list, choice_phone)
        check = question_yes_no(
            f"Удалить выбранные телефоны {choice_phone} контакта {choice}?")
        if check:
            request_delete_phone(phone_id_list)
            easygui.msgbox("Выбранные телефоны успешно удалены")
        else:
            return

#Функция вывода данных из двух связанных таблиц, получилось слишком длинно, но вывод сортируется по алфавиту 
def print_table(request_contacts: list, request_phone: list):
    contacts_name_list = list()
    for i in range(len(request_contacts)):
        request_contacts[i] = list(request_contacts[i])
        request_contacts[i].insert(1, list())
        for j in range(2, 6):
            request_contacts[i][1].append(request_contacts[i][j])
        for j in range(4):
            request_contacts[i].pop()
        for j in range(4):
            if request_contacts[i][1][j] == None:
                request_contacts[i][1][j] = " "
        request_contacts[i][1] = " ".join(request_contacts[i][1])
        contacts_name_list.append(request_contacts[i][1])
    contacts_name_list.sort()
    for i in range(len(request_phone)):
        request_phone[i] = list(request_phone[i])
        request_phone[i].insert(1, list())
        for j in range(2, 5, 2):
            request_phone[i][1].append(request_phone[i][j])
        request_phone[i].pop()
        request_phone[i].pop(2)
        for j in range(2):
            if request_phone[i][1][j] == None:
                request_phone[i][1][j] = " "
        request_phone[i][1] = " ".join(request_phone[i][1])
    final_string = str()
    buff_string = str()
    buff_phone_list = list()
    buff_contact_id = int()
    for i in range(len(contacts_name_list)):
        for j in range(len(request_contacts)):
            if contacts_name_list[i] == request_contacts[j][1]:
                buff_contact_id = request_contacts[j][0]
        for j in range(len(request_phone)):
            if buff_contact_id == request_phone[j][2]:
                buff_phone_list.append(request_phone[j][1])
        buff_string = f"{contacts_name_list[i]}\n"
        for j in range(len(buff_phone_list)):
            buff_string += f"   тел. {j+1}: {buff_phone_list[j]}\n"
        final_string += buff_string
        buff_string = ""
        buff_phone_list.clear()
        buff_contact_id = None
    easygui.textbox("", "", final_string)

#Вывод всего телефонного справочника
def print_all_phonebook():
    request_contacts_tuple = request_contacts()

    if request_contacts_tuple == []:
        easygui.msgbox("Телефонный справочник пуст")
        return
    request_phone_tuple = request_all_phones()
    print(request_contacts_tuple)
    print(request_phone_tuple)
    print_table(request_contacts_tuple, request_phone_tuple)


#Вывод телефонов указанных контактов
def print_specified():
    request_contacts_tuple = request_contacts()
    choice_list = get_list_of_choice(request_contacts_tuple)
    if len(choice_list) == 0:
        easygui.msgbox("Телефонный справочник пуст")
        return
    elif len(choice_list) == 1:
        print_all_phonebook()
        return
    sorted_choice_list = choice_list.copy()
    sorted_choice_list.sort()
    choice = easygui.multchoicebox(
        "Выберите контакты для вывода их телефонов", "Вывод телефонов указанных контактов", sorted_choice_list)
    if choice == None:
        return
    id_contacts_list = get_id_list(request_contacts_tuple, choice_list, choice)
    specified_request_contacts_tuple = request_specified_contacts(
        id_contacts_list)
    specified_request_phone_tuple = request_specified_phone(id_contacts_list)
    print_table(specified_request_contacts_tuple,
                specified_request_phone_tuple)


#Получение списка для .multchoicebox и .choicebox, внутри функций так же используется сортировка по алфавиту
def get_list_of_choice(request_tuple: tuple) -> list:
    choice_list = request_tuple.copy()
    for i in range(len(choice_list)):
        choice_list[i] = list(choice_list[i])
    for i in range(len(choice_list)):
        del choice_list[i][0]
        try:
            while True:
                choice_list[i].remove("NULL")
        except:
            pass
        try:
            while True:
                choice_list[i].remove("")
        except:
            pass
        try:
            while True:
                choice_list[i].remove(None)
        except:
            pass
    try:
        for i in range(len(choice_list)):
            choice_list[i] = " ".join(choice_list[i])
        return choice_list
    except:
        pass

#Получение списка id на основе изначального запроса, списка для выбора (они соответствующие по индексам) и списка, который возвращает .multchoicebox
def get_id_list(request_list: tuple, choice_list: list, choice: list) -> list:
    id_list = list()
    for item in choice:
        if item in choice_list:
            id_list.append(request_list[choice_list.index(item)][0])
    return id_list

#Получение одного id, при тех же входных данных, как и в предыдущей функции
def get_id(request_list: tuple, choice_list: list, choice: str) -> int:
    return request_list[choice_list.index(choice)][0]

#Закрыть и сохранить телефонный справочник и базу данных
def close_phone_book():
    connection.commit()
    cursor.close()
    connection.close()
    easygui.msgbox("Телефонный справочник сохранён и закрыт")

#Запрос
def question_yes_no(msg: str) -> bool:
    yes_no = ["Да", "Нет"]
    selection = easygui.ynbox(msg, "", yes_no)
    return selection


while True:
    choice = start_screen()
    if choice == 1:
        add_contact()
    elif choice == 2:
        add_phone_number_to_contact()
    elif choice == 3:
        change_contact_name()
    elif choice == 4:
        change_phone()
    elif choice == 5:
        delete_contact()
    elif choice == 6:
        delete_phone()
    elif choice == 7:
        print_all_phonebook()
    elif choice == 8:
        print_specified()
    elif choice == None or choice == 0:
        check = question_yes_no(
            "Закрыть и сохранить телефонный справочник?")
        if check:
            close_phone_book()
            break