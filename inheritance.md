# Inheritance

Class တစ်ခုရဲ့ properties တွေ method တွေကို နောက်ထပ် class တစ်ခုဆီကို လက်ဆင့်ကမ်းပေးလိုက်တာဖြစ်တယ်။ အမွေဆက်ခံခိုင်းလိုက်တာမျိုးဖြစ်တယ်။

Parent Class (Base Class) အမွေပေးတဲ့ class
Child Class (Derived Class) အမွေဆက်ခံတဲ့ class

`is-a` Relationship

class Dog က cllass Animal ကို inheritance လုပ်ထားတယ်ဆိုရင် class Animal နဲ့ class Dog ကြားမှာ `is-a` relationship ဖြစ်တယ်။

Inheritance လုပ်ထားတဲ့အတွက်ကြောင့် class တွေကို ထပ်ခါထပ်ခါထပ်ရေးနေစရာမလိုတော့ဘူး reuseablity ပိုဖြစ်တယ်။

---

```python
class Animal():
  def eat(self):
    print("Animal is eating")

  def sleep(self):
    print("Animal is sleeping")

class Dog(Animal):
  pass

class Cat(Animal):
  pass

dog = Dog()
dog.eat()
dog.sleep()

cat = Cat()
cat.eat()
cat.sleep()
```

---
