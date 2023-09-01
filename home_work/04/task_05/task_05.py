"""
Даны два многочлена, которые вводит пользователь. как две строки.
Задача - сформировать многочлен, содержащий сумму многочленов, и вывести как строку.

Степени многочленов могут быть разные.

например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
на выходе будет 5x^3 - x^2 + 4х - 7 = 0
можно использовать модуль re 
"""
# Идея состоит в том, что бы сначала с помощью регулярных выражений получить список ключей для словаря,
# Далее из этого списка так же с помощью регулярных выражений, получаем степень, преобразовываем в int (далее понадобится для сортировки)
# И получаем словарь - где ключ - это значение степени (ключ 0 для константы) и список в этом ключе - коэффициенты
# Объединяем полученные словари, складываем в нём все коэффициенты и собираем строку-ответ суммы многочленов на основе итогового словаря, сортируя при этом ключи
import re



# Функция получения словаря ключ-степень:список коэффициентов 
def create_dict_coeff (polynom: str) -> dict:
    coeff_dict = dict()
    # Удаляем из строки многочлена пробелы и знаки *
    polynom = polynom.replace(' ', '')
    polynom = polynom.replace('*', '')
    # получаем с помощью функции re.findall список членов многочлена, но без констант
    parsing = re.findall(r'[-+]?\d*x\^?\d*', polynom)
    #Вычисляем список констант, убирая из строки многочлена все выражения с переменной x, но если есть несколько подряд идущий чисел (5+1-6) получим в списке такое значение
    const_parsing = re.split(r'[-+]?\d*x\^?\d*', polynom)
    #Чтобы избавиться от подряд идущих констант, склеим список обратно в строку и найдём уже все значения по регулярному выражению любого числа
    const_parsing = "".join(const_parsing)
    const_parsing = re.findall(r'[+-]?\d+', const_parsing)  
    #Преобразуем все числа в int тип в списке констант и
    #Начнём заполнение словаря многочлена с констант, ключ для констант будет 0
    coeff_dict[0] = list()    
    if const_parsing == []:  #Если в многочлене нет констант, запишем в словарь 0
        coeff_dict[0].append(0)
    for i in range (len(const_parsing)):
        const_parsing[i] = int (const_parsing[i])
        coeff_dict[0].append(const_parsing[i])
    #Проходим по списку членов многочлена и добавляем в словарь: ключ(является показателем степени) и список значений, если в многочлене есть повторяющие степени
    for i in range(len(parsing)):
        buff = ''.join(map(str, re.findall(r'x\^?\d*', parsing[i])))
        buff = ''.join(map(str, re.findall(r'\d*$', buff)))
        if buff == "": #Условие для x в первой степени
            buff = 1
        else:
            buff = int(buff)
        #проверка, если в словаре нет ключа, добавляем с словарь ключ-степень:значение
        if buff not in coeff_dict:
            coeff_dict[buff] = list()
            coeff_dict[buff].append(
                ''.join(map(str, re.findall(r'^[-+]?\d*', parsing[i]))))
        else: #Если же ключ есть, то просто добавляем в него ещё один коэффициент
            coeff_dict[buff].append(
                ''.join(map(str, re.findall(r'^[-+]?\d*', parsing[i]))))    
    #Проходим по всем значениям словаря, кроме констант (ключ:0), если пустая строка или +, то значение 1 (в случае x, x^2 ит.д.), если -, то -1
    for key in coeff_dict:
        for i in range(len(coeff_dict[key])):
            if (coeff_dict[key][i] == '' or coeff_dict[key][i] == '+')  and key != 0:
                coeff_dict[key][i] = 1
            elif coeff_dict[key][i] == '-' and key != 0:
                coeff_dict[key][i] = -1            
            else: #И преобразуем все значения в int
                coeff_dict[key][i] = int(coeff_dict[key][i])
    return coeff_dict


#Получив несколько словарей многочленов со значениями: ключ-степень и список их коэффициентов, объединим эти словари, создав общий ключ-степень:список коэффициентов
#Просуммируем каждый список коэффициентов, получив итоговый словарь, являющийся суммой многочленов
def merging_list_dicts(list_dicts: list) -> dict:
    result_dict = dict()
    for i in range(len(list_dicts)):
        for key in list_dicts[i]:
            if key in result_dict:
                result_dict[key] += list_dicts[i][key]
            else:
                result_dict[key] = list_dicts[i][key]
    for key in result_dict:
        sum = 0
        for i in range(len(result_dict[key])):
            sum += result_dict[key][i]
        result_dict[key] = sum

    return result_dict

#Собираем строку-ответ из итогового словаря
def assembling_polynom(polynom_dict: dict) -> str:
    #Т.к. словарь это не упорядоченная коллекция данных, создадим список ключей словаря, которые у нас являются int значениями и сортируем список
    key_list = sorted(polynom_dict.keys())
    #Записываем в обратом порядке (получается обратно отсортированный список), получив полное соответствие в порядке убывания степеней итогового многочлена
    key_list.reverse()
    #Создания строки, в которой будет собираться многочлен из словаря
    result = str()
    #Начинаем сборку многочлена, нужно описать множество условий, вычислив начальный итератор, в зависимости есть ли начальные нулевые коэффициенты,
    #что бы не было лишнего + в начале, если многочлен начинается с x без степени не было записи вида x^1, а так же вернуть "0", если все коэффициенты равны нулю
    for i in range(len(key_list)):
        if polynom_dict.get(key_list[i]) != 0 and polynom_dict.get(key_list[i]) != 1 and polynom_dict.get(key_list[i]) != -1 and key_list[i] != 1 and key_list[i] != 0:
            result += f"{polynom_dict.get(key_list[i])}*x^{key_list[i]}"
            start_index = i + 1
            break
        elif polynom_dict.get(key_list[i]) == 1 and key_list[i] != 1 and key_list[i] != 0:
            result += f"x^{key_list[i]}"
            start_index = i + 1
            break
        elif polynom_dict.get(key_list[i]) == -1 and key_list[i] != 1 and key_list[i] != 0:
            result += f"-x^{key_list[i]}"
            start_index = i + 1
            break
        elif key_list[i] == 1 and polynom_dict.get(key_list[i]) != 0 and polynom_dict.get(key_list[i]) != 1 and polynom_dict.get(key_list[i]) != -1:
            result += f"{polynom_dict.get(key_list[i])}x"
            start_index = i + 1
            break
        elif key_list[i] == 1 and polynom_dict.get(key_list[i]) == 1:
            result += "x"
            start_index = i + 1
            break
        elif key_list[i] == 1 and polynom_dict.get(key_list[i]) == -1:
            result += "-x"
            start_index = i + 1
            break
        elif key_list[i] == 0:
            result = f"{polynom_dict.get(key_list[i])}"
            return result
    #Основной цикл сборки многочлена, со множеством условий, как и при начале 
    for i in range(start_index, len(key_list)):
        if polynom_dict.get(key_list[i]) > 0 and polynom_dict.get(key_list[i]) != 1 and polynom_dict.get(key_list[i]) != -1 and i != len(key_list) - 2 and i != len(key_list) - 1:
            result += f" + {polynom_dict.get(key_list[i])}*x^{key_list[i]}"
        elif polynom_dict.get(key_list[i]) < 0 and polynom_dict.get(key_list[i]) != 1 and polynom_dict.get(key_list[i]) != -1 and i != len(key_list) - 2 and i != len(key_list) - 1:
            result += f" - {abs(polynom_dict.get(key_list[i]))}*x^{key_list[i]}"
        elif polynom_dict.get(key_list[i]) == 1 and i != len(key_list) - 2 and i != len(key_list) - 1:
            result += f" + {abs(polynom_dict.get(key_list[i]))}*x^{key_list[i]}"
        elif polynom_dict.get(key_list[i]) == -1 and i != len(key_list) - 2 and i != len(key_list) - 1:
            result += f" - {abs(polynom_dict.get(key_list[i]))}*x^{key_list[i]}"
        elif i == len(key_list) - 2 and polynom_dict.get(key_list[i]) > 0:
            result += f" + {polynom_dict.get(key_list[i])} * x"
        elif i == len(key_list) - 2 and polynom_dict.get(key_list[i]) < 0:
            result += f" - {abs(polynom_dict.get(key_list[i]))} * x"
        elif i == len(key_list) - 1 and polynom_dict.get(key_list[i]) > 0:
            result += f" + {polynom_dict.get(key_list[i])}"
        elif i == len(key_list) - 1 and polynom_dict.get(key_list[i]) < 0:
            result += f" - {abs(polynom_dict.get(key_list[i]))}"
    return result





polynom1 = "-5x+87x^2-44x^3+15+44x^5+5-10"
polynom1_dict = create_dict_coeff(polynom1)
polynom2 = "5x-87x^2+44x^3+15+5x^6"
polynom2_dict = create_dict_coeff(polynom2)
polynom3 = "5x^6+5+8+19+5x^3-10x"
polynom3_dict = create_dict_coeff(polynom3)
result_dict = [polynom1_dict, polynom2_dict, polynom3_dict]
result = merging_list_dicts(result_dict)
result = assembling_polynom(result)
print (result) #10*x^6 + 44*x^5 + 5*x^3 - 10 * x + 57