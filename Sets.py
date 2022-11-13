# სიმრავლე - ერთობლიობა ელემენტების რომელსაც არ აქვს პოზიციონირება და ინდექსაცია
thisisset = {"apple", "banana", "cherry"}
print(thisisset)

# ელემენტების შეცვლა
# როცა სიმრავლე შეიქმნება მას ვეღარ შეცვლი, თუმცა შეგიძლია ელემენტები დაამატო
# add() ერთი
thisisset.add("orange")
print(thisisset)
# update() რამდენიმე
thisisset.update(["orange", "mango", "grapes"])
print(thisisset)

# წაშლა
thisisset.discard("banana")
print(thisisset)

# დანარჩენი იგივეა რაც სიებში !
