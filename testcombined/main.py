import datetime, bday_massages

next_birthday = datetime.date(2025, 4, 18)
today = datetime.date.today()
time_differancce =  next_birthday - today 
print(f"Time until next birthday: {time_differancce.days} days")
if today == next_birthday:
    print(bday_massages.random_message)
else:
    print("my next borthday is in", time_differancce.days, "days")