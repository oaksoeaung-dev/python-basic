from datetime import datetime

current_datetime = datetime.now()

print(current_datetime)

today = datetime.now();

formatted_day1 = today.strftime("%d-%m-%Y, %H Hour %M Minutes");
formatted_day2 = today.strftime("%d Date %m Month %Y Year %H:%M:%S");

print(formatted_day1);
print(formatted_day2);

str_birthday = "05-03-2000"

birthday = datetime.strptime(str_birthday, "%d-%m-%Y");

print(birthday);