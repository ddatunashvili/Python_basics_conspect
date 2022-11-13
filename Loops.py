# ციკლები
# While loop
# სანამ პირობა არის True იქამდე იმუშავებს ციკლი

i = 1
# როცა აი არის 6 ზე ნაკლები მაშინ
while i < 6:
    # ამ ხაზის ყოველ გაშვებაზე იპრინტება
    print(i)
    # ყოველ გაშვებაზე ერთით იზრდება 
    i += 1


# Continue
# მესამე იტერაციის გამორთვა და შემდეგ იტერაციაზე გადასვლა
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Else
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i აღარაა ნაკლები, i მეტია 6 ზე")

# For loop
# ფორ ციკლი არის კონკრეტული ოდენობის ერთიანობის იტერაციებისთვის (list tuple dict set string)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


# სიაზე
for x in "banana":
    print(x)


# Break
for x in fruits:
    print(x)
    if x == "banana":
        break


# Continue
for x in fruits:
    print(x)
    if x == "banana":
        continue
    print(x)


# Range
for x in range(6):
    print(x)

# Else
for x in range(6):
  print(x)
else:
  print("ციკლის დასრულება!")
