# String

single quoute `'` or double quoute `"` ထဲမှာ value ထည့်လိုက်ရင် string value ဖြစ်တယ်။

```python
print("Hello!")
print('Nice to meet you.')
print("Hello! 'Harry'")
print('"Harry" is not my name.')
```

> Multi line string

```python
x = """Python is a popular, high-level, general-purpose 
programming language known for its simple, readable syntax that emphasizes clarity 
and allows developers to express
"""

y = '''Python is a popular, high-level, general-purpose 
programming language known for its simple, readable syntax that emphasizes clarity 
and allows developers to express
'''
```

---

# String Concatenation

String နှစ်ခုကိုပေါင်းချင်ရင် `+` သုံးရတယ်

```python
x = "Hello"
y = "World"
print(x + " " + y);
```

---

# Format String

String ထဲမှာ varialble ကို တစ်ခါထဲထည့်သုံးချင်ရင် format string ကိုသုံးရတယ်

```python
wheels = 4;
message = f"My car has {4} wheels"
print(message)
```

```python
cola_per_item = 1000
cola_total_items = 3

print(f"I bought {3} bottles of cola for {1000 * 3} kyats.")
```

---