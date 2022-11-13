# ფუნქცია კოდის ბლოკია, რომელიც გამოძახებით ეშვება.
# შეგიძლია მიაწოდო მონაცემები, პარამეტრის სახით, რომელიც ფუნქცის შიგნით იარსებებს.

def myfunction():
    print("Hello from a function")
myfunction()

# არგუმენტები
# ფრჩხილებში იწერება ფუნქციის სახელის შემდეგ
# რამდენი არგუმენტიც გინდათ დაამატეთ, მძიმით გამოყავით
# ამ ფუნქციას აუცილებლად ორი არგუმენტი სჭირდება
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Tobias", "Great")
my_function("Linus", "TooGreat")
my_function("Emil", "MuchGreat")

# თუ არვიცით რამდენ პარამეტრს ვაძლევ
def my_kids(*kids):
    print("The youngest child is " + kids[2])
my_kids("Emil", "Tobias", "Linus")

# შესაძლებელია გასაღები= მნიშვნელობა სინტაქსით მიაწოდო მნიშვნელობები
def mykids(child3, child2, child1):
    print("The youngest child is " + child3)


mykids(child1= "Emil", child2= "Tobias", child3= "Linus")

def my_list(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_list(fruits)



