# Encapsulation

**Datahiding** : Object တွေက သူတို့ထဲမှာရှိတဲ့ state(properties) နဲ့ behaviour(method) တွေကို လိုအပ်တာပဲပေးသုံးပြီး မလိုအပ်တာတွေကို ပေးမသုံးသင့်ဘူး။ Internal data တွေကို အပြင်ကနေ access လုပ်လို့ရအောင်လုပ်တာ access မရအောင်လုပ်တာက encapsulation သဘောတရားဖြစ်တယ်။ ဥပမာ laptop တစ်လုံးကိုကြည့်လိုက်မယ်ဆိုရင် keyboard တို့ touchpad တို့ screen တို့ကိုပဲ ထိလို့ရတယ် အထဲက motherboard တွေကို ထိလို့မရအောင်ဖုံးထားတယ်။ Motherboard ကိုထိခွင့်ပေးထားရင် မလိုအပ်တဲ့ error တွေခနခနတက်နေမှာဖြစ်တယ်။ Object တွေလည်းအဲ့လိုပဲ encapsulation သာမလုပ်ထားရင် state တွေ behaviour တွေကမှန်ကန်နေမှာမဟုတ်တော့ဘူး။

Encapsulation လုပ်ထားတဲ့ properties တွေကို control လုပ်ချင်ရင် ခွင့်ပြုထားတဲ့ method တွေကနေပဲလုပ်ခွင့်ရှိတယ်။ ဥပမာ getter, setter method တွေကနေဖြစ်တယ်။

**Validation** : Encapsulation လုပ်ထားတာက data validation အတွက်လည်းကောင်းတယ်။ ဥပမာ `Kid` ဆိုတဲ့ class တစ်ခုရှိမယ်။ သူ့ထဲမှာ `age` ဆိုတဲ့ properties တစ်ခုရှိမယ်။ အဲ့ peroperties ကို encapsulate လုပ်ထားမယ်။ အဲ့တာကြောင့် method ကနေပဲ age ကိုပြင်ခွင့်ရှိမယ်။ အဲ့ method ထဲမှာ validation လုပ်ထားမယ် 1 ကနေ 18 အထိပဲသတ်မှတ်လို့ရမယ်ဆိုတဲ့ validation။ အဲ့လိုသတ်မှတ်ထားတဲ့အတွက်ကြောင့် `age` ကို ကြိုက်တာထည့်လို့မရတော့ဘူး 1 ကနေ 18 အတွင်းပဲထည့်လို့ရတော့မှာဖြစ်တယ်။ တကယ်လို့ အဲ့လိုတာမလုပ်ထားရင် `age` ကိုအပြင်ကနေကြိုက်သလိုပြင် (1000 လို့ပြင်လိုက်တာဖြစ်ဖြစ်, 99999 လို့ ပြင်လိုက်တာဖြစ်ဖြစ်) လို့ရနေရင် `Kid` ဆိုတဲ့ object ရဲ့ state ကမှန်ကန်မှုရှိနေတော့မှာမဟုတ်ဘူး

---

## Private Properties

Class အတွင်းထဲက method ကနေပဲ access လုပ်ခွင့်ရှိတယ်။

`__` underscore နှစ်ခုကို property name ရဲ့ရှေ့ဆုံးမှာ ရေးလိုက်ရင် private property ဖြစ်သွားတယ်။

```python
class Student:
  def __init__(self, name):
    self.name = name
    self.__age = 0

mgmg = Student("Mg Mg")
# print(mgmg.__age) # Error: 'Student' object has no attribute '__age'
```

private property တွေကိုအပြင်ကနေယူသုံးလို့မရဘူး

## Protectd Properties

`_` underscore တစ်ခုကို property name ရဲ့ရှေ့ဆုံးမှာ ရေးလိုက်ရင် protected property ဖြစ်သွားတယ်။ Protected properties တွေကို class အပြင်ကနေသုံးလို့မရဘူး base class နဲ့ derived class (child class) တွေကနေပဲသုံးလို့ရတယ်။

## Getter

```python
class Student:
  def __init__(self, name):
    self.name = name
    self.__age = 0

  def get__age(self):
    return self.__age

mgmg = Student("Mg Mg")
age = mgmg.get__age()
print(age)
```

Getter method ကအမြဲတမ်း return ပြန်ပေးရမယ်။ get ပါလို့ getter သတ်မှတ်လိုက်တာမဟုတ်ဘူး။ private property ကို return ပြန်ထားတယ် အပြင်ကနေလည်းခေါ်သုံးလို့ရတဲ့အတွက်ကြောင့် getter method လို့ခေါ်တာဖြစ်တယ်။

## Setter

```python
class Student:
  def __init__(self, name):
    self.name = name
    self.__age = 0

  def get__age(self):
    return self.__age
  
  def set__age(self, age):
    if 1 <= age <= 18:
      self.__age = age
    else:
      print("Age must be between 1 and 18.")

mgmg = Student("Mg Mg")
mgmg.set__age(20)
age = mgmg.get__age()
print(age)
```

Setter ထဲမှာ validation လုပ်ထားတဲ့အတွက်ကြောင့် ထည့်ချင်တာထည့်လို့မရတော့ဘူး Object ကိုပိုပြီးမှန်ကန်စေတယ်။

## Decorator Property

```python
class Student:
  def __init__(self, name):
    self.name = name
    self.__age = 0

  def get__age(self):
    return self.__age

  @property
  def age(self):
    return self.__age
  
  @age.setter
  def age(self, age):
    if 1 <= age <= 18:
      self.__age = age
    else:
      print("Age must be between 1 and 18.")

mgmg = Student("Mg Mg")
mgmg.age = 10
print(mgmg.age)
```

အပေါ် getter, setter နဲ့ပုံစံတူတူပဲဖြစ်တယ်။

---