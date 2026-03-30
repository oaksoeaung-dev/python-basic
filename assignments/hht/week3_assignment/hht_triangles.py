def ask_rows():
  while True:
    rows = int(input("How many rows do you want to create?"))
    if rows > 15:
      print("Rows must not be larger than 15!")
    else:
      return rows

rows = ask_rows()
display =""
for row in range(1,rows+1):
  for star in range(row):
    display += "*"
  display += "\n"
print(display)

display =""
for row in range(1, rows+1):
  for space in range(rows - row):
    display += " "
  for star in range(row):
    display += "*"
  display += "\n"
print(display)

display =""
for row in range(1, rows+1):
  for space in range(rows - row):
    display += " "
  for star in range(row):
    display += "* "
  display += "\n"
print(display)

display =""
for row in range(1, rows+1):
  for space in range(rows - row):
    display += " "
  for star in range(2 * row - 1):
    display += "*"
  display += "\n"
print(display)


  
