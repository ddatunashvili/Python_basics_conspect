# დალაგებულია მაგრამ შეუცვლადი
thisisTuple = ("apple", "banana", "cherry")
print(thisisTuple)


# სიაში გადაყვანა და შემდეგ შეცვლა
x  = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# დანარჩენი იგივეა როგორც სიებზე!

