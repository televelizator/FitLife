# Проект FitLife - MVP версия 1.0

user_name = input("Как тебя зовут? ")
user_age = int(input("Cколько тебе лет? "))
user_weight = float(input("Сколько ты весишь? "))
user_height = float(input("Какой у тебя рост? (в метрах) "))

def body_mass_index(user_weight, user_height):
    bmi = user_weight / user_height ** 2
    return round(bmi, 1)

def water_needed(user_weight):
    water = user_weight * 30
    return round(water / 1000, 1)

bmi = body_mass_index(user_weight, user_height)
water_count = water_needed(user_weight)

print("Отчет для пользователя:", user_name, user_age, 'лет.')
print('Твой bmi:', bmi, ', а норма воды', water_count, 'л.')
print()
print("Расчет окончен. Будьте здоровы!")