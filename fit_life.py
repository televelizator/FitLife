# Проект FitLife - MVP версия 1.0


# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани в переменную user_age (не забудь преобразовать в число)
user_name = input("Привет!!! Как тебя зовут?")
user_age = int(input("Cколько тебе лет?"))

# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
# TODO: Запроси рост (в метрах, например 1.75) и сохрани в user_height (тип float)
user_weight = float(input("Сколько ты весишь?"))
user_height = float(input("Какой у тебя рост? (в метрах)"))

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
def body_mass_index(user_weight, user_height):
    bmi = user_weight/user_height**2
    return bmi

bmi = body_mass_index(user_weight, user_height)

# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
def water_needed(user_weight):
    water = round(float(user_weight*30/1000),2)
    return water

water_count= water_needed(user_weight)

# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие, например: "Привет, Иван!"
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.

print(f"""
Отчет для пользователя: {user_name} ({user_age} лет). 
Твой bmi {round(bmi, 1)}, а норма воды {water_count} л.
""")
print("Расчет окончен. Будьте здоровы!")