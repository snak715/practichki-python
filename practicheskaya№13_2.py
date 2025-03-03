from datetime import datetime

dates = ["12-04-2023", "23-05-2022", "15-03-2021", "09-06-2020"]
with open('dates.txt', 'w') as file:
    for date in dates:
        file.write(f"{date}\n")

with open('dates.txt', 'r') as file:
    dates = [datetime.strptime(line.strip(), "%d-%m-%Y") for line in file]

min_year = min(date.year for date in dates)
print(f"Год с наименьшим номером: {min_year}")

spring_dates = [date for date in dates if 3 <= date.month <= 5]
print("Весенние даты:", [date.strftime("%d-%m-%Y") for date in spring_dates])

latest_date = max(dates)
print(f"Самая поздняя дата: {latest_date.strftime('%d-%m-%Y')}")