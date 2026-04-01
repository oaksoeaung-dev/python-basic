# Python DateTime Module

## Using DateTime in App

```python
from datetime import datetime
```
datetime object ကိုအသုံးပြုဖို့ အရင်ဆုံး import လုပ်ပေးရမယ်

datetime ဆိုတဲ့ library ကနေ datetime module ကို import လုပ်ပါ ဆိုတဲ့သဘောမျိုးဖြစ်တယ်။

---

## Current Date And Time

> Usage

```syntax
datetime.now():
```

> Example

```python
current_datetime = datetime.now()

print(current_datetime)
```

> Output

```
2026-02-05 18:27:28.916094
```

ကိုယ့် laptop ရဲ့ လက်ရှိ timezone ပေါ်မူတည်ပြီး result ရလာတာဖြစ်တယ်။

`2026-02-05` = `Year-Month-Day`

`18:27:28.916094` = `Hour:Minute:Seconds`

---

## Formatting Datetime with `strftime()`

> Usage

```
datetime_obj.strftime(format)
```

`strftime()` က datetime object ကို ကိုယ်လိုချင်တဲ့ format ပုံစံနဲ့ datetime string ကိုပြောင်းပေးတယ်။

> Example

```python
today = datetime.now();

formatted_day1 = today.strftime("%d-%m-%Y, %H Hour %M Minutes");
formatted_day2 = today.strftime("%d Date %m Month %Y Year %H:%M:%S");

print(formatted_day1);
print(formatted_day2);
```


`%m`, `%d` စတဲ့ အသုံးပြုလို့ရတဲ့ format တွေကို [ဒီနေရာကိုနှိပ်ပြီး](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) ကြည့်ပါ။

> Output

```
05-02-2026, 19 Hour 51 Minutes
05 Date 02 Month 2026 Year 19:51:04
```

---

## Dateime string to datetime object

> Usage

```
datetime.strptime(datetime, formatstring)
```

> Example

```python
str_birthday = "05-03-2000"

birthday = datetime.strptime(str_birthday, "%d-%m-%Y");

print(birthday);
```

> Output

```
2000-03-05 00:00:00
```

---