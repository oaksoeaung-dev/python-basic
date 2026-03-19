# OOP (Object Oriented Programming)

OOP သုံးရတဲ့ရည်ရွယ်ချက်က code တွေကို စနစ်တကျလုပ်ချင်တယ်၊ reuseable ဖြစ်စေချင်တယ်၊ Project ကြီးလာရင်လည်း code တွေက maintain လုပ်ရတာလွယ်ကူစေတယ်။ Feature အသစ်တွေထည့်မယ်ဆိုရင်လည်း စနစ်တကျထည့်နိုင်တယ်။

## 4 Pilar of OOP

- Encapsulation
- Inheritance
- Polymorphism
- Abstration

---

## Class and Object

**class** နဲ့ **object** တွေက OOP ရဲ့ အရေးပါတဲ့ concept တွေဖြစ်တယ်။

`class` ဆိုတာက blueprint တစ်ခုဖြစ်တယ်။ (ဥပမာ: car တစ်စီးရဲ့ design ပုံစံ)

`object` ဆိုတာက အဲ့ blueprint ကို သုံးပြီး တည်ဆောက်လိုက်တဲ့အရာဖြစ်တယ်။ (ဥပမာ: car တစ်စီးရဲ့ design ကိုသုံးပြီး ကားတစ်စီးဆောက်လိုက်တာမျိုး)


```python
class Car:
  number_of_wheel = 4

my_car = Car()
```

class တစ်ခုကိုဖန်တီးချင်ရင် `class` keyword ကိုသုံးပြီး create လုပ်လို့ရတယ်။

`my_car = Car()` ဆိုတာက Object တစ်ခုကို create လုပ်တာဖြစ်တယ်။ Instantiating လုပ်တယ်လို့လည်းခေါ်တယ်။

## `self` Parameter

`self` ဆိုတာလက်ရှိ အလုပ်လုပ်နေတဲ့ Instance (Object) ကိုရည်ညွှန်းတာဖြစ်တယ်။ Class ထဲက properties တွေ methods တွေကို ပြန်သုံးချင်ရင် `self.` နဲ့ခေါ်ပြီးသုံးလို့ရတယ်။

```python
class Person:
  name = "Kyaw Kyaw"

  def get_name(self):
    print(f"Name is {self.name}")

person1 = Person()
person1.get_name() # Name is Kyaw Kyaw
```

> Method တိုင်းရဲ့ ပထမဆုံး argument မှာ `self` ကအမြဲပါနေရမယ်။

Code ကိုကြည့်လိုက်ရင် `self` က Person ဆိုတဲ့ class ကိုရည်ညွှန်းတယ်။

## `__init__()` Method

Constructor လို့လည်းခေါ်တယ်။

class ကို initiate လုပ်လိုက်တိုင်း (object တစ်ခု create လုပ်လိုက်တိုင်း) မှာ invoke လုပ်တယ်။ Object create လုပ်ရာမှာလိုအပ်တဲ့ data တွေကို `__init__()` method ထဲကို parameter အနေနဲ့ pass ပေးလိုက်လို့ရတယ်။

## `__del__()` Method

Destructor လို့လည်းခေါ်တယ်။

Object တစ်ခု ကို RAM ပေါ်ကနေဖယ်လိုက်တဲ့အခါ (Reference မရှိတော့တဲ့အခါ) Garbage Collector ကနေ auto ခေါ်ပေးတဲ့ method ဖြစ်တယ်။

---

```python
class Robot:
  def __init__(self, name):
    self.name = name
    print(f"{self.name} is created.")

  def speak(self, message):
    print(f"{self.name} says: {message}")
  
  def __del__(self):
    print(f"{self.name} is shutting down.")

bot1 = Robot("RoboCop")
bot1.speak("Don't move.")
```

Output :

```
RoboCop is created.
RoboCop says: Don't move.
RoboCop is shutting down.
```

---