# Exception

Error တွေကို exception လို့ခေါ်တယ်။ Program တစ်ခုမှာ error တက်ရင် program ကလုံးဝရပ်သွားတယ်။ အဲ့လိုရပ်မသွားအောင် handle လုပ်တာကို exception handling လုပ်တယ်လို့ခေါ်တယ်။

handle လုပ်ဖို့ `try` `catch` statement ကိုသုံးတယ်။

`try` - `try` block ထဲမှာ code တွေကို error တက်မတက် run ကြည့်တယ်။

`except` - `except` block ထဲမှာ error တွေကို ဘယ်လိုပြမယ် log မှတ်မယ် စတာတွေကိုလုပ်တယ်။

`else` - error မရှိမှ else block ထဲက code တွေကို run တယ်။

`finally` - `finally` block ထဲက code တွေက error တက်တာပဲဖြစ်ဖြစ် မတက်တာပဲဖြစ်ဖြစ် နောက်ဆုံးမှာ run တယ်။

---

```python
try:
    result = 1 / 0
    print(f"result = {result}")
except ZeroDivisionError as ex:
    print(f"Error: {ex}")
finally:
    print("All Done!")
```

အပေါ်က code ကို run ကြည့်လိုက်ရင် `ZeroDivisionError` နဲ့ပတ်သတ်တာကိုပဲပြတယ်။ တကယ်လို့ error က `ZeroDivisionError` မဟုတ်ဘူးဆိုရင်မပြတော့ဘူး အောက်က example code ကိုကြည့်ပါ။

```python
try:
    fruits = ["apple", "banana", "cherry"]
    print(f"My favorite fruit is {fruits[7]}")
except ZeroDivisionError as ex:
    print(f"Error: {ex}")
finally:
    print("All Done!")
```

List မှာရှိနေတဲ့ index ထက်ကျော်ပြီး print လုပ်ထားတာဖြစ်တယ်ဒါပေမယ့် exception က `ZeroDivisionError` ကိုပဲ except လုပ်တာဖြစ်တဲ့အတွက် handle မလုပ်နိုင်ပဲ program ကရပ်သွားတယ်။

```python
try:
    fruits = ["apple", "banana", "cherry"]
    print(f"My favorite fruit is {fruits[7]}")
except Exception as ex:
    print(f"Error: {ex}")
finally:
    print("All Done!")
```

ဒီလိုမျိုး `Exception` နဲ့ရေးလိုက်ရင် ဘယ် error မဆို except လုပ်နိုင်တယ်။ ဘာလို့လုပ်နိုင်တာလည်းဆိုတော့ error exception တိုင်းက `Exception` ကို inheritance လုပ်ထားတာကြောင့်ဖြစ်တယ်။

