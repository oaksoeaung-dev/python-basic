# Polymorphism

Polymorphism ဆိုတာ name တူတဲ့ method တွေမှာ လုပ်ဆောင်ချက်အမျိုးမျိုးရှိနေတာကိုပြောတာဖြစ်တယ်။ ဥပမာ ဦးလှက ကျောင်း မှာဆိုကျောင်းဆရာ စာသင်တယ် အိမ်မှာဆိုရင် အဖေ သားသမီးတွေကို ပြုစုပျိုးထောင်တယ်။ ဦးလှကတော့ တစ်ယောက်ထဲ ဒါပေမယ့် အလုပ်တွေအမျိုးမျိုးလုပ်နိုင်တယ် နေရာပေါ်လိုက်ပြီး ကျောင်းမှာဆိုကျောင်းဆရာ အိမ်မှာဆိုအဖေ

> Polymorphism လုပ်ဖို့ဆိုရင် inheritance ရှိနေဖို့လိုတယ်။

---

```python
class Animal():
  def __init__(self, name):
    self._name = name

  def eat(self):
    print("Animal is eating")

  def sleep(self):
    print("Animal is sleeping")

class Dog(Animal):
  def eat(self):
    print(f"{self._name} is eating in dog form.")

class Cat(Animal):
  def eat(self):
    print(f"{self._name} is eating in cat form.")

  def eat(self):
    print(f"{self._name} is sleeping in cat form.")

  def makeSound(self): # ထပ်ထဲ့ချင်တဲ့ method လည်းထည့်လို့ရတယ်။
    print(f"{self._name} said Meow Meow.")

dog = Dog("Dog")
dog.eat()
dog.sleep() # Dog class မှာ sleep ကို morph မလုပ်ထားတဲ့အတွက် parent class ကအတိုင်းပဲရလာတယ်။

cat = Cat("Cat")
cat.eat()
cat.sleep()
cat.makeSound()
```