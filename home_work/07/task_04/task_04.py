"""
Сделайте игру крестики - нолики, человек должен играть с ботом, поле 3*3.
Конечно, бот не должен ходить на занятые поля
Если есть желание, то можете наделить бота псевдоинтеллектом,чтоб он ходил как можно ближе к своим занятым клеткам
После каждого хода на экран должна выводиться текущая обстановка на поле.
Например,

|     |  Х |  O   |

|     |  O |  X   |

|     |  O |      |

При ходе пользователя у надо спрашивать номер строки и столбца, куда он хочет сделать ход
"""
import random
from decimal import Decimal

#Вначале определим случайным образом, кто ходит первым - первый ход всегда начинает крестик, в зависимости от того, кто ходит первым:
#компьютер или игрок - назначим константу в виде строки X или О для игрока и компьютера. Делаю вначале, т.к. константы объявляют сразу после импортов
if random.randint(1, 2) == 1:
    print("Игрок ходит первым")
    PLAYER_TURN = "X"
    COMPUTER_TURN = "O"
else:
    print("Компьютер ходит первым")
    PLAYER_TURN = "O"
    COMPUTER_TURN = "X"


def input_validation_int(invitation_text: str) -> int:
    variable = None
    while variable == None:
        value = input(invitation_text)
        try:
            buff = Decimal(value)
            if buff == int(buff):
                variable = int(buff)
                return variable
            else:
                raise
        except:
            print("\033[6m\033[31m{}\033[0m".format(
                "Вы ввели не целое число, повторите ввод"))

#Функция хода игрока, если игрок ошибается и ходит на не существующее или занятое поле - возникает исключение и ввод нужно повторить
def player_turn(game_list):
    while True:
        try:
            line_number = input_validation_int(
                "Введите номер строки, куда хотите сделать ход: ")
            row_number = input_validation_int(
                "Введите номер столбца, куда хотите сделать ход: ")
            if game_list[line_number - 1][row_number - 1] == " ":
                game_list[line_number - 1][row_number - 1] = PLAYER_TURN
                break
            else:
                raise
        except:
            print("\033[6m\033[31m{}\033[0m".format(
                "Вы пытаетесь ходить на уже занятое или не существующее поле, повторите ввод"))
    return game_list


#Случайный ход компьютера, если он пытается сделать ход на занятое поле - возникает исключение и случайные значения для хода вычисляются ещё раз,
#Пока компьютер не попадёт в пустое поле. Прикручивать логику к ходам компьютера я не решился, слишком для меня сложно, но принцип куда копать я примерно понял
#на примере функции, определяющей кто выиграл и когда игра закончится
def computer_turn(game_list):
    while True:
        try:
            line_number = random.randint(0, 2)
            row_number = random.randint(0, 2)
            if game_list[line_number][row_number] == " ":
                game_list[line_number][row_number] = COMPUTER_TURN
                break
            else:
                raise
        except:
            ''
    return game_list

#Функция по определению конца игры - проверяет есть ли на игровом поле одинаково заполненная линия и возвращает символ, которым она заполнена
#Если все поля заполнены и нет заполненной линии - вернётся XO, которое означает ничью. Работает по логике, преобразования списка из потенциальной линии
#во множество и проверки его длины, если она 1 - следовательно можно считать, что линия заполнена. Используется дополнительный список, который поочерёдно
#заполняется символами из линий
#Так же проверяется, есть ли на поле пустые клетки, если их нет и до этого ни одно условие не сработало следовательно объявляется ничья
def check_end_game(game_list: list):
    buff_list = list()    
    for i in range(3):
        if len(set(game_list[i])) == 1:
            return ''.join(set(game_list[i]))
    for i in range(3):
        for j in range(3):
            buff_list.append(game_list[j][i])
        if len(set(buff_list)) == 1:
            return ''.join(set(buff_list))
        buff_list.clear()
    for i in range(3):
        buff_list.append(game_list[i][i])
    if len(set(buff_list)) == 1:
        return ''.join(set(buff_list))
    buff_list.clear()
    for i in range(3):
        buff_list.append(game_list[i][2-i])
    if len(set(buff_list)) == 1:
        return ''.join(set(buff_list))
    buff_list.clear
    buff_list = sum (game_list, [])
    if " " not in buff_list:
        return "XO"


#Поочерёдные ходы игрока и компьютера, логика слишком прямолинейная, но работает
#Возможно стоило сделать функцию, с несколькими аргументами, чтобы избежать повтора похожего кода
def tic_tac_toe_game(game_list: list):
    while True:
        if PLAYER_TURN == "X":
            print("Ход игрока:")
            player_turn(game_list)
            print_table(game_list)
            if check_end_game(game_list) == 'X':
                print("Победил игрок")
                break
            elif check_end_game(game_list) == 'O':
                print("Победил компьютер")
                break
            elif check_end_game(game_list) == 'XO':
                print("Ничья")
                break
            print("Ход Компьютера:")
            computer_turn(game_list)
            print_table(game_list)
            if check_end_game(game_list) == 'X':
                print("Победил игрок")
                break
            elif check_end_game(game_list) == 'O':
                print("Победил компьютер")
                break
            elif check_end_game(game_list) == 'XO':
                print("Ничья")
                break
        else:
            print("Ход Компьютера:")
            computer_turn(game_list)
            print_table(game_list)
            if check_end_game(game_list) == 'X':
                print("Победил компьютер")
                break
            elif check_end_game(game_list) == 'O':
                print("Победил игрок")
                break
            elif check_end_game(game_list) == 'XO':
                print("Ничья")
                break
            print("Ход игрока:")
            player_turn(game_list)
            print_table(game_list)
            if check_end_game(game_list) == 'O':
                print("Победил игрок")
                break
            elif check_end_game(game_list) == 'X':
                print("Победил компьютер")
                break
            elif check_end_game(game_list) == 'XO':
                print("Ничья")
                break

#Функция вывода на экран игрового поля
def print_table(game_list: list):
    for i in range(3):
        print(f"|{'|'.join(game_list[i])}|")


#Создаём список списков и заполняем его пробелам, которые означают пустые клетки
game_list = list()
for i in range(3):
    game_list.insert(i, [" " for _ in range(3)])

tic_tac_toe_game(game_list)