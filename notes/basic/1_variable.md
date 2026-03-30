# Variable

# Creating variable

```python
name = "Mg Mg"
age = 20
```

Python ရဲ့ variable မှာ type မရှိဘူး။ Type ဆိုတာက `string`, `integer`, `boolean` စတာတွေကိုပြောတာဖြစ်တယ်။ value မှာပဲ type ရှိတယ်။ `name` ဆိုတဲ့ varialbe ထဲကို `Mg Mg` ဆိုတဲ့ string type ဖြစ်တဲ့ value ကို ထည့်လိုက်တာဖြစ်တယ်။

Python မှာ `name` ကို **stack memory** ပေါ်မှာသိမ်းပြီးတော့ `Mg Mg` ဆိုတဲ့ value ကို **heap memory** ပေါ်မှာသိမ်းတယ်။

---

Variable naming ပေးတဲ့အခါမှာ အောက်ပါ rules တွေကို လိုက်နာသင့်တယ်

- Variable name က letter or `_` (underscore) နဲ့စသင့်တယ်
- number နဲ့စလို့မရဘူး
- Variable name မှာ `A-z`, `0-9`, `_` စတာတွေပဲပါလို့ရတယ်
- Varable name တွေက case sensitive ဖြစ်တယ် (eg. `school`, `SCHOOL` က မတူညီတဲ့ varialbe တွေဖြစ်တယ်။)
- Python ရဲ့ keyword တွေကိုပေးလို့မရဘူး

> Valid Variable Name

```python
myname = "Kyaw Kyaw"
my_mane = "Kyaw Kyaw"
_my_name = "Kyaw Kyaw"
myName = "Kyaw Kyaw"
MYNAME = "Kyaw Kyaw"
myname2 = "Kyaw Kyaw"
```

Python မှာ များသောအားဖြင့် snake case ကို အသုံးများတယ်

> Invalid Varialbe Name

```python
2myage = 10
my-age = 10
my age = 10
```

---