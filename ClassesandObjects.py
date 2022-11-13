# პითონი ობიექტზე დაპროგრამების ენაა
#  თითქმის ყველაფერი რასაც ვწერთ გვაქვს ობიექტის სახით, სახეობისა და მეთოდიკის მიხედვით

# -----------------------------------------------------------
#  კლასები
#  კლასის შექმნა
class MyClass:
    x = 5


# ობიექტი
#  p1 ობიექტის შექმნა , x ის მნიშვნელობის ბეჭდვა
p1 = MyClass()
print(p1.x)

# -----------------------------------------------------------
#  __init__() ფუნქცია
#  ყველა კლასს აქვს ფუნქცია __init__(), რომელიც ეშვება კლასის განსაზღვრისთანავე.
#  __init__() ფუნქცია გამოიყენება რომ მივანიჭოთ მნიშვნელობა ობიექტის პროპერტის (properties),
# ან სხვა საჭირო ოპერაციებისთვის ვიყენებთ მნიშვნელობას
#  პიროვნების კლასის შექმნა,  __init__() ,ფუნქცია name ageმნიშვნელობის მისანიჭებლად გამოვიყენეთ


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("ANA", 15)

print(p1.name)
print(p1.age)

# -----------------------------------------------------------
# ობიექტის მეთოდები
# ობიექტებსაც აქვთ მეთოდები და ისინი წარმოადგენენ ობიექტის ფუნქციებს
# მისალმების ფუნქციის შექმნა, გაშვება p1 ობიექტიდან ფუნქციის გამოძახებით


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p2 = Person2("Arth", 15)
p2.myfunc()

# -----------------------------------------------------------
# Self პარამეტრი
# მისი მეშვეობით მაიფანკიდან ვიღებთ წვდომას ცვლადებზე რომელიც ინიტშია გაწერილი


class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self, abc):
        print("Hello my name is " + self.name)


p3 = Person3("Arth", 15)
p3.myfunc()
# დააერორებს
