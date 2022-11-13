# კოლექციაა dict() არ არის წყობა არეული, შეცვლადი , ინდექსირებული.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# -------------------------------------------------
# წვდომა ელემენტებზე
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)

# -------------------------------------------------
# მნიშვნელობის შეცვლა
thisdict["year"] = 2020
print(thisdict)

# -------------------------------------------------
#  ციკლში გატარება
for x in thisdict:
    print(x)

for x in thisdict.values():
    print(x)

for x,y in thisdict.items():
    print(x, y)

# -------------------------------------------------
# პირობა
if "model" in thisdict:
    print("კი, 'model'  არის ლექსიკონში")

# -------------------------------------------------
# წაშლა დამატება ლექსიკონში
thisdict["color"] = "red"
print(thisdict)

thisdict.pop("model")
print(thisdict)

# -------------------------------------------------
# კოპირება
mydict = thisdict.copy()
print(mydict)

# -------------------------------------------------
# წყობა ლამაზად
myfamily  = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)


