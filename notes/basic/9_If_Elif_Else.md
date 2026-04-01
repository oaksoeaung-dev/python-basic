# `IF`...`Elif`...`Else`

Python မှာ comparison operator, logical operator တွေကို သုံးပြီး logic တွေကိုစစ်တယ်။ စစ်လိုက်တဲ့ logical condition ပေါ်မူတည်ပြီး `True` ဖြစ်ရင်ဘာလုပ်မယ် `False` ဖြစ်ရင်ဘာလုပ်မယ်ဆိုတာကိုဆုံးဖြတ်ရင် if statement ကိုသုံးတယ်။

```python
name = "John Doe"
nickname = "John"

if name == nickname:
    print("Name and nickname are same.")
else:
    print("Name and nickname are not same.")
```

condition က `True` ဖြစ်ရင် `if` blockထဲက code တွေကအလုပ်လုပ်သွားမယ် `else` block ထဲက code တွေကတော့အလုပ်မလုပ်ဘူး။ Condition `False` ဖြစ်မှ `else` block ထဲက code တွေကအလုပ်လုပ်မယ်။

```python
score = 75
if score >= 80:
    print("Excellent")
elif score >= 60:
    print("Good")
elif score >= 40:
    print("Bad")
else:
    print("Fail")
```

`if` ကနေစပြီး condition တွေ တစ်ခုပြီးတစ်ခု စစ်သွားတယ် condition တစ်ခုမှန်ရင် အောက်က condition တွေကိုထပ်မစစ်တော့ဘူး condition တွေတစ်ခုမှမမှန်ဘူးဆိုရင် `else` block ထဲက code တွေအလုပ်လုပ်တယ်။

```python
day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid")
```

ဒီလိုနေရာမျိုးမှာဆိုရင် `elif` ကိုသုံးသင့်တယ်။ Condition တစ်ခု true ဖြစ်သွားပြီဆိုတာနဲ့ အောက်က condition တွေကိုထပ်မစစ်တော့ဘူး။

```python
day = 1

if day == 1:
    print("Monday")
    
if day == 2:
    print("Tuesday")
    
if day == 3:
    print("Wednesday")
    
if day == 4:
    print("Thursday")
    
if day == 5:
    print("Friday")
    
if day == 6:
    print("Saturday")
    
if day == 7:
    print("Sunday")
    
if day >= 8:
    print("Invalid")
```

`elif` မသုံးပဲ `if` တွေနဲ့ အပေါ်ကလိုမျိုး စစ်ရင် day က 1 ဖြစ်တဲ့အတွက် ပထမ condition မှာ တင်မှန်နေပြီဖြစ်တယ် ဒါပေမယ့် အောက်က တစ်ခြား condition တွေကိုပါ မလိုအပ်ပဲ ထပ်စစ်သွားတယ်။