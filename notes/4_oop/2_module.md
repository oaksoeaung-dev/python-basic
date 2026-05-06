# Module

Module သုံးရတဲ့ရည်ရွယ်ချက်က function တွေ code တွေကို တစ်ခါရေးထားပြီးရင် project ရဲ့ကြိုက်တဲ့နေရာကနေခေါ်သုံးလို့ရတယ်။ Reuseable ဖြစ်တယ်။

Behaviour တူတဲ့ code တွေကို module တစ်ခုအောက်မှာရေးသင့်တယ်။

Module တွေမှာ

Built-in Modules - Python မှာအသင့်ပါလာပြီးသား module တွေဖြစ်တယ်။ (eg. os)

User-defined Modules - User ကိုယ်တိုင်ရေးထားတဲ့ module တွေဖြစ်တယ်။

External Modules - သူများရေးထားတဲ့ module တွေကို ကိုယ့် project ထဲကို install လုပ်ပြီးသုံးရတဲ့ module တွေဖြစ်တယ်။

---

## Creating Module and Using Module

**Folder Structure**

```
sample_code
├─── math_tool
│    └─── __init__.py
│    └─── math_helper.py
└─── module.py
```

`math_tool` ရဲ့ folder အောက်မှာ `__init__.py` ဆိုတဲ့ file လေးထည့်လိုက်တာက `math_tool` ဆိုတဲ့ folder ကို package အနေနဲ့ / module အနေနဲ့သုံးမယ်လို့ကြေငြာတာဖြစ်တယ်။


```python
# math_helper.py

def add(num1, num2):
  return num1 + num2

def sub(num1, num2):
  return num1 - num2
```

```python
# module.py

import math_tool.math_helper

result = math_tool.math_helper.add(10, 12)

print(result)
```

Module တစ်ခုလုံးကို import လုပ်လိုက်တာဖြစ်တယ်။ အသုံးပြုမယ်ဆိုရင်လည်း တစ်ခုလုံးကိုပြန်ခေါ်ပြီးသုံးပေးရမယ်။

---

```python
# module.py

import math_tool.math_helper as operation

sub_result = operation.sub(10, 2)
add_result = operation.add(20, 30)

print(sub_result)
print(add_result)
```

Module ကို အတိုကောက်နာမည်ပြောင်းပြီး သုံးတာဖြစ်တယ်။ အရှည်ကြီးရိုက်ပြီးသုံးစရာမလိုတော့ဘူး

---

```python
# module.py

from math_tool.math_helper import add

add_result = add(3, 4)

# sub_result = sub(4, 1) # Error: "sub" is not defined

print(add_result)
```

module ထဲက function တစ်ခုကိုပဲဆွဲထုတ်ပြီးသုံးတာဖြစ်တယ်။ `add` ကိုပဲ import လုပ်ထားတဲ့အတွက် `sub` ကိုသုံးလို့မရဘူး

---