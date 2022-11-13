# ცვლადი კონტეინერია, რომელიც მნიშვნელობებს (ელემენტებს ინახავს)

# მესიჯი არის ცვლადი და მისი მნიშვნელობაა "Hello World"
# ნახე Variables.py
message = "Hello World"

# len() სტრინგის სიგრძე
print(len(message))

# ეს სამი სხვადასხვა ცვლადია რადგან ცვლადის სახელი განსხვავებულია
this = 1
This = 2
THIS = 3


# რამდენიმეს მინიჭება ერთ ხაზზე
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# შეგვიძლია რამდენიმე ცვლადს მივანიჭოთ ერთი
x = y = z = "Blop"
print(x)
print(y)
print(z)

# თუ ორმაგს იყენებ შეგიძლია შიგნით ერთიანი ბრჭყალი გამოიყენო სხვანაირად ვერ გამოიყენებ ტექსტში ' ს
another_message = "Arth's World"
#				   012345 678910

# [] სტრინგი იგივე სიმბოლოების სიაა ნახე lists.py და სიმბოლოებზე ინდექსებით წვდომა გვაქვს
print(another_message[4])

# სლაისინგი
# 0 დან 5 მდე
print(another_message[0:5])
# 0 დან 5 მდე
print(another_message[:5])
# 6 დან ბოლომდე
print(another_message[6:])

# ( ბოლოდან მეხუთე )დან (ბოლოს წინა) მდე
b = "Hello World"
print(b[-5:-2])

# მრავალხაზიანი სტრინგი
third_message = """So this is what you call 
Multiline String"""

# lower() პატარა ასოები
print(third_message.lower())

# upper() დიდი ასოები
print(third_message.upper())

# count() რაოდენობა "i" სიმბოლოების
print(third_message.count("i"))

# find() ლოკაციის გაგება
print(third_message.find("what"))

# replace() ჩანაცვლება ერთი სიმბოლოს მეორეთი (ან სტრინგის სტრინგით)
third_message = third_message.replace("String", "Strings")
print(third_message)


# Co სიების გაერთიანება
greeting = "Good evening"
name = "Arth"

# 1 გზა
combined = greeting + ", " + name + ". Welcome!"
print(combined)

# 2 გზა
# {} შეივსება დაფორმატებისას თანმიმდევრობით
# პირველი პირველს ავსებს მეორე მეორეს
combined = "{}, {}. Welcome!".format(greeting, name)
print(combined)

# 3 გზა
# შეგვიძლია პირდაპირ ჩავსვათ ცვლადების სტრინგში თუ f ს გავუწერთ სტრინგს წინ (ყველა სტრინგზე შეგვიძლია)
combined = f"{greeting}, {name}. Welcome!"
print(combined)
