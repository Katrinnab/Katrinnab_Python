def is_year_leap(year: int):
    return year % 4 == 0


year = 2019
print(f'Год {year}: {is_year_leap(year)}')
