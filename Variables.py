# მონაცემების შესანახი კონტეინერი
# პითონს არ სჭირდება ცვლადის გამოცხადება
# ცვლადი იქმნება მნიშვნელობის მინიჭებისთანაცე
# ცვლადი და მნიშვნელობა
x = 5
# Printing x
print(x)

# ცვლადი შეიძლება შევცვალოთ (ტიპებია ინტეჯერი და სტრინგი)
x = 4  # x  int
print(x)
print(type(x))

x = '9'  # str
print(x)
print(type(x))

###########################

# გლობალური ცვლადები
# ფუნქციის გარეთ ცვლადები გლობალური ცვლადებია
# შეგვიძლია ფუნქციის გარეთაც გავიტანოთ ფუნქციის შექმნილი ცვლადები
# Functions.py
x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

y = "awesome"


def myfunc2():
    # ფუნქციის შიდა ცვლადი
    # რჩება ფუნქციაში
    x = "fantastic"
    print("Python is " + y)


myfunc2()
# "Python is awesome"
print("Python is " + y)

# ცვლადის გატანა ფუნქციის გარეთ


def myfunc3():
    global x
    x = "fantastic"


myfunc3()
print("Python is " + x)
