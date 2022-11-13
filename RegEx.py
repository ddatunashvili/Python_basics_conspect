# regular expression - ძებნის პატერნები
import re

txt = "The rain in Spain"
# იწყება  "The" ით და მთავრდება "Spain" ით
x = re.search("^The.*Spain$", txt)
print(x)

# რეგექსის ფუნქციები
# Findall()
print("\n")
x = re.findall("ai", txt)
print(x)

# Search()
print("\n")
x = re.search("^The.*Spain$", txt)
print(x)

# Split()
print("\n")
x = re.split("\s", txt)
print(x)

# Sub()
x = re.sub("\s", "9", txt)
print(x)
