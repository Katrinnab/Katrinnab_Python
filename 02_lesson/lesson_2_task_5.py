def month_to_season(month):
    if month < 1 or month > 12:
        return "Некорректный номер месяца"
    if month < 3:
        return "Зима"
    elif month < 6:
        return "Весна"
    elif month < 9:
        return "Лето"
    elif month < 12:
        return "Осень"
    else:
        return "Зима"


month = int(input("Введите номер месяца: "))
print(month_to_season(month))
