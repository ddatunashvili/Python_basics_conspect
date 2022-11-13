# მონაცემთა სტრუქტურა რომელიც შეგვიძლია პოზიციები შევუცვალოთ ან ელემენტი შევუცვალოთ
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#              0        1         2         3        4        5        6
#             -7       -6        -5        -4       -3       -2        -1
print(thisList)


# წვდომა ელემენტებზე
print(thisList[1])
print(thisList[-2])
# სლაისინგი (რეინჯებით)
# დაიწყება 2 დან და 4 მდე მივა
print(thisList[2:5])
# თუ არ მივუთითებთ საწყისს ნულიდან დაიწყება
print(thisList[:4])
print(thisList[4:])
# (ბოლოდან მეოთხე)-დან ბოლომდე
print(thisList[-4:-1])


# ელემენტის შეცვლა
thisList[3] = "Guava"
print(thisList)


# ჩაციკვლა
# ნახე Loops.py
for x in thisList:
    print(x)


# პირობები
# ნახე IfElse.py
if 'apple' in thisList:
    print("Yes, 'apple' is in the fruits list.")


# ელემენტის დამატება
thisList.append("strawberry")
print(thisList)


# ლემენტის ჩასმა პოზიციაზე ინდექსის მიხედვით
thisList.insert(1, "pineapple")
print(thisList)


# ელემენტის წაშლა
thisList.remove("banana")
print(thisList)


