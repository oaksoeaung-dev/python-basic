# Casting

Variable တစ်ခုရဲ့ data type ကို နောက် data type တစ်မျိုးကို ပြောင်းလဲသတ်မှတ်တာဖြစ်တယ်။

- `int()`
- `float()`
- `str()`
- `bool()`

---

## `int()`

Integer အဖြစ်ပြောင်းပေးတယ်။ Float data type ကိုပြောင်းရင် ဒဿမ တွေကိုဖြုတ်ပြီး ကိန်းပြည့်ဖြစ်အောင်ပြောင်းပေးတယ်။ Number string ကိုလည်း integer ဖြစ်အောင်ပြောင်း‌ပေးတယ်။

```python
a = int(1)
b = int(3.6)
c = int("5")
# d = int("H") # Error

print(a) # 1
print(b) # 3
print(c) # 5
```

## `float()`

Integer or number string တွေကို float အဖြစ်ပြောင်းပေးတယ်။

```python
d = float(10) 
e = float(10.7) 
f = float("20.4") 
g = float("3") 

print(d) # 10.0
print(e) # 10.7
print(f) # 20.4
print(g) # 3.0
```

## `str()`

ဘယ် data type ကိုမဆို string အဖြစ်ပြောင်းပေးတယ်။

```python
h = str("python")
i = str(4.12)
j = str(20)

print(h) # python
print(i) # 4.12
print(j) # 20
```

## `bool()`

Data type တိုင်းကို boolean ပြောင်းပေးတယ်။ boolean ပြောင်းတဲ့အခါမှာ Truthy value or Falsy value ကိုကြည့်ပြီးပြောင်းတယ်။

```python
k = bool(1)
l = bool("Hello")
m = bool(0)
n = bool("")

print(k) # True
print(l) # True
print(m) # False
print(n) # False
```
---