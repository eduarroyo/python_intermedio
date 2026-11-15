from datetime import datetime, date, time, timedelta
from random import randint
from calendar import monthrange

# 1. Crea una variable con la fecha y hora actual.
now = datetime.now()
print(now)

# 2. Imprime solo el año, mes y día de la fecha actual.
current_date = date.today()
print(current_date)

# 3. Crea una fecha específica: 25 de diciembre de 2025 y muéstrala.
christmas = date(2025, 12, 25)
print(christmas)

# 4. Muestra solo la hora, los minutos y los segundos de un objeto time.
my_time = time(15,29,23)
print(my_time)

# 5. Calcula cuántos días faltan para el 1 de enero del año siguiente.
curent_date = date.today()
new_year = date(current_date.year+1, current_date.month+1, current_date.day)
diff = new_year - current_date
print(diff.days)

# 6. Crea una función que reciba una fecha y devuelva su timestamp.
def date_timestamp(date: datetime):
    return date.timestamp()

print(date_timestamp(datetime.now()))

# 7. Suma 30 días a la fecha actual usando timedelta.
today = date.today()
thirty_days = timedelta(days=30)
next_month = today + thirty_days
print(next_month)

# 8. Crea una fecha y añade 1 mes (consejo: hazlo sumando 30 días como simplificación).
# birthday = date(2025, 11, 28) + 30
my_date = date(2026,2,1)
delta = timedelta(days=30)
next_month = my_date + delta
print(next_month)

# 9. Compara dos fechas y muestra cuál es anterior.
date1 = date(2025, 12, randint(1,31))
date2 = date(2025, 12, randint(1,31))
if(date1 > date2):
    print(f"{date1} es mayor que {date2}")
else:
    print(f"{date2} es mayor que {date1}")


# 10. Crea una lista con varias fechas y ordénalas cronológicamente.
def random_date():
    year = randint(2020, 2026)
    month = randint(1,12)
    day = randint(1, monthrange(year, month)[1])
    return date(year, month, day)

dates = [ random_date() for _ in range(5) ]
dates.sort()
print(dates)
