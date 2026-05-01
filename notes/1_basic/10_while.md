# While Loop

while loop က condition မှန်နေသရွေ့ loop ပတ်နေမှာဖြစ်တယ်။ Condition မမှန်တော့တဲ့အချိန်ကြရင် loop ရပ်သွားတယ်။ condition အမြဲတမ်းမှန်နေရင် infinite loop ဖြစ်နိုင်တယ်။

```python
i = 1
while i < 5:
    print(i)
```

အပေါ်က code ဆိုရင် condition အမြဲမှန်နေတဲ့အတွက်ကြောင့် infinite loop ဖြစ်တယ်။

```python
i = 1
while i < 5:
    print(i)
    i += 1
```

loop တစ်ခါပတ်တိုင်းမှာ i ကို 1 တိုးတိုးသွားတယ်။ i က 5 ဒါမှမဟုတ် 5 ကို ကျော်သွားရင် condition က false ဖြစ်ပြီး loop ကရပ်သွားတယ်။

---