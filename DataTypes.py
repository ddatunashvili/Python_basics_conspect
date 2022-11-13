# მონაცემთა ტიპები
# ტექსტი : Str
# რიცხვობრივი : Int, Float, Complex
# ერთობლიობა : List, Tuple, Range
# ლექსიკონი : Dict
# სიმრავლე : Set, Frozenset
# ლოგიკური (): Bool
# ბინარული : Bytes, Bytearray, Memoryview

# type() ფუნქცია გვეუბნება მონაცემის ტიპს 

x = "Hello World"
print(type(x)) # Str

x = 5
print(type(x)) # Int

x = 5.5
print(type(x)) # Float

x = ["apple", "banana", "cherry"]
print(type(x)) # List

x = ("apple", "banana", "cherry")
print(type(x)) # Tuple

x = range(6)
print(type(x)) # Range

x = True
print(type(x)) # Bool

