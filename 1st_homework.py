from datetime import datetime


def get_days_from_today(date: str) -> int:
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - given_date
        return delta.days
    except ValueError:
        print("Помилка: дата має бути у форматі YYYY-MM-DD")
        return 0


some_date = str(input(f"Введіть дату в форматі: РРРР-ММ-ДД: "))
result = get_days_from_today(some_date)


if result > 0:
    print(f"Від вказаної вами дати до сьогодні: {result} днів")
else:
    result = result*-1
    print (f"Вказана вами дата настане через {result} днів")
