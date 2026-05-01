# Break and Continue

`break` က loop ကိုရပ်ပစ်တယ်။

`continue` က loop တစ်ခု iteration တစ်ခုကို ကျော်ပြီး ဆက်လုပ်တယ်။


> break

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```

```plaintext
1
2
```

> continue

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

```plaintext
1
2
4
5
```

---