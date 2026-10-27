# Проект FitLife - MVP версия 1.0

user_name = input("Как тебя зовут? ")
user_age = int(input("Cколько тебе лет? "))
user_weight = float(input("Сколько ты весишь? "))
user_height = float(input("Какой у тебя рост? (в метрах) "))


def body_mass_index(user_weight, user_height):

    bmi = user_weight / user_height ** 2
    return bmi


def water_needed(user_weight):

    water = round(user_weight * 30 / 1000, 2)
    return water


bmi = body_mass_index(user_weight, user_height)
water_count= water_needed(user_weight)

print(
    f"Отчет для пользователя: {user_name} ({user_age} лет). \n"
    f"Твой bmi: {round(bmi, 1)}, а норма воды {water_count} л."
)
print("Расчет окончен. Будьте здоровы!")