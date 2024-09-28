import smtplib
import random
import pandas
import datetime

username = "Your username"
Password = "Your password"

data = pandas.read_csv("birthdays.csv")

current = datetime.datetime.now()
today_date = current.day
today_month = current.month
today = (today_month, today_date)

birthday_dict = {(rows["month"], rows["day"]): rows for (index, rows) in data.iterrows()}

if today in birthday_dict:
    n = random.randint(1, 3)
    file_path = f"letter_templates/letter_{n}.txt"
    with open(file_path) as file:
        contents = file.read()
        contents=  contents.replace("[NAME]", birthday_dict[today]["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=username, password=Password)
        connection.sendmail(from_addr=username, to_addrs=birthday_dict[today]["email"],
                            msg=f"Subject:Happy Birthday \n\n {contents}")
