"""
df.query("housing_median_age > 51")
df.query("housing_median_age > 51 and total_rooms < 1000")
df [ df['population'] < 20 ] [['total_bedrooms', 'total_rooms']]
df.query("population < 20") [ ['total_bedrooms', 'total_rooms']]

df.loc[     df['population'] < 20,   ['total_bedrooms', 'total_rooms']    ]
df.loc[     df['median_income'] < 2,   [ 'median_house_value']    ]
df.loc[     df['median_income'] < 2,   [ 'median_house_value']    ]

print(df['median_house_value'].max())
print(df['median_house_value'].min())
df.query('median_income == 3.1250') [['median_house_value']].max()
apr = df['median_house_value'].min() * 1.45
df.query(f'median_house_value < {apr}') [['population']].max()
"""

from random import *
import json
films = []
films.append("Матрица")
films.append("Солярис")
films.append("Властелин колец")
films.append("Техасская резня бензопилой")
films.append("Санта Барбара")

def save():
    with open ("films.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii = False))
    print ("Наша фильмотека успешно сохранена")
    

while True:
    command = input("Введите команду: ")
    if command == "/start":
        print("Бот-фильмотека начал свою работу")
    elif command == "/stop":        
        print ("Бот остановил работу")
        break
    elif command == "/show all":
        print ("Весь список фильмов")
        print (films)
    elif command == "/add":
        f = input("Введите название фильма: ")
        films.append(f)
        print ("Фильм был успешно добавлен в коллекцию")
    elif command == "/del":
        delete =  input("Введите название фильма для удаления: ")
        films.remove(delete)
        print(f"Фильм {delete} успешно удалён")
    elif command == "/help":
        help = "Погладь манула ыыы"
        print (help)
    elif command == "/save":
        save()
    else:
        print("Неопознанная команда. Просьба изучить мануал через /help")
