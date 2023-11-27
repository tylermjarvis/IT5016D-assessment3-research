# LA43_DictionaryReading.py
# @ author: Administrator
# Date: 27.10.23
 
city_population = {"New York City": 8_550_405, 
                   "Los Angeles": 3_971_883, 
                   "Toronto": 2_731_571, 
                   "Chicago": 2_720_546, 
                   "Houston": 2_296_224, 
                   "Montreal": 1_704_694, 
                   "Calgary": 1_239_220, 
                   "Vancouver": 631_486, 
                   "Boston": 667_137}

print(city_population["New York City"])
# output = 8550405
print(city_population["Toronto"])
# output = 2731571
print(city_population["Boston"], "\n")
# output = 667137

'''
# A value that does not exist in the dictionary will result in a key error
city_population["Detroit"]
OUTPUT:
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-5-80e422418d76> in <module>
----> 1 city_population["Detroit"]

KeyError: 'Detroit'
'''

'''
# You cannot treat dictionaries like an ordered list
city_population[0]
OUTPUT:
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-7-a4816f909f86> in <module>
----> 1 city_population[0]

KeyError: 0
'''

# Defining a dictionary/ Adding values and keys to it
city_population2 = {}
city_population2['New York City'] = 8550405
city_population2['Los Angeles'] = 3971883
print(city_population2, "\n")
# output = {'New York City': 8550405, 'Los Angeles': 3971883}

# Multiple keys result in the latest key being used
food = {"bacon" : "yes", "spam" : "yes", "egg" : "yes", "spam" : "no" }
print(food, "\n")
# output = {'bacon': 'yes', 'spam': 'no', 'egg': 'yes'}

# Nesting values
de_fr = {"rot": "rouge", "grün": "vert", "blau": "bleu", "gelb": "jaune"}
en_de = {"red": "rot", "green": "grün", "blue": "blau", "yellow": "gelb"}
print(en_de, "\n")

print(en_de["red"], "\n")

de_fr = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}
print("The French word for red is: " + de_fr[en_de["red"]])
# output = {'red': 'rot', 'green': 'grün', 'blue': 'blau', 'yellow': 'gelb'}
# rot
# The French word for red is: rouge

# Only immutable types can be used as keys
# dic = {[1,2,3]: "abc"} This will cause an error

# Tuples are okay to use as keys
dic = {(1, 2, 3): "abc", 3.1415: "abc"}
print(dic, "\n")
# output = {(1, 2, 3): 'abc', 3.1415: 'abc'}

# Creating a dictionary of dictionaries
en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
de_fr = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}
de_tr = {"rot": "kırmızı", "grün": "yeşil", "blau": "mavi", "gelb": "jel"}
en_es = {"red" : "rojo", "green" : "verde", "blue" : "azul", "yellow":"amarillo"}

dictionaries = {"en_de" : en_de, "de_fr" : de_fr, "de_tr": de_tr, "en_es": en_es}
print(dictionaries, "\n")

# Adding to the dictionary above
cn_de = {"红": "rot", "绿" : "grün", "蓝" : "blau", "黄" : "gelb"}
de_ro = {'rot': 'roșu', 'gelb': 'galben', 'blau': 'albastru', 'grün': 'verde'}
de_hex = {"rot" : "#FF0000", "grün" : "#00FF00", "blau" : "0000FF", "gelb":"FFFF00"}
en_pl = {"red" : "czerwony", "green" : "zielony", 
         "blue" : "niebieski", "yellow" : "żółty"}
de_it = {"rot": "rosso", "gelb": "giallo", "blau": "blu", "grün": "verde"}
dictionaries["cn_de"] = cn_de
dictionaries["de_ro"] = de_ro
dictionaries["de_hex"] = de_hex
dictionaries["en_pl"] = en_pl
dictionaries["de_it"] = de_it
print(dictionaries, "\n")

print(dictionaries["de_fr"], "\n") # german to french

print(dictionaries["de_fr"]["blau"], "\n") # equivalent to de_fr['blau'], output = bleu

# User input
lang_pair = input("Which dictionary, e.g. 'de_fr', 'en_de': ")
word_to_be_translated = input("Which colour: ")

d = dictionaries[lang_pair]
if word_to_be_translated in d:
    print(word_to_be_translated + " --> " + d[word_to_be_translated])

# output = Which dictionary, e.g. 'de_fr', 'en_de': de_fr
# Which colour: gelb
# gelb --> jaune

# for loops, to iterate through a dictionary
for value in de_fr.values():
    print(value)
for key, value in de_fr.items():
    print(key, value)
fr_de = {}
fr_de['rouge'] = 'rot'
fr_de['vert'] = "grün"
fr_de = {}
for key, value in de_fr.items():
    fr_de[value] = key # key and value are swapped
print(fr_de, "\n")

de_cn = {}
for key, value in cn_de.items():
    de_cn[value] = key
print(de_cn, "\n")

# More iteration
d = {"a":123, "b":34, "c":304, "d":99}
for key in d:
     print(key)
print("\n")
# However, it's possible to use the method keys(),
# we will get the same result:
for key in d.keys():
     print(key)
print("\n")
# The method values() is a convenient way for iterating
# directly over the values:
for value in d.values():
    print(value)
print("\n")
# The above loop is logically equivalent to the following one:
for key in d:
    print(d[key])
print("\n")

# pop() = removes the key and returns the value, e.g Vienna
capitals = {"Austria":"Vienna", "Germany":"Berlin", "Netherlands":"Amsterdam"}
capital = capitals.pop("Austria")
print(capital, "\n")
# output = Vienna

# If the key doesn't exist, by adding a value to that key, you can create a safety net and therefore no error will be thrown
capital = capitals.pop("Switzerland", "Bern")
print(capital, "\n")


# popitem(), this returns a (key, value) pair as a 2-tuple
capitals = {"Springfield": "Illinois", 
            "Augusta": "Maine", 
            "Boston": "Massachusetts", 
            "Lansing": "Michigan", 
            "Albany": "New York", 
            "Olympia": "Washington", 
            "Toronto": "Ontario"}
(city, state) = capitals.popitem()
print(capitals.popitem(), "\n")
print(capitals.popitem(), "\n")


# Accessing non-existing keys
locations = {"Toronto": "Ontario", "Vancouver": "British Columbia"}
province = "Ottawa"

if province in locations: 
    print(locations[province])
else:
    print(province + " is not in locations \n")

# Another way to access non-existing keys
proj_language = {"proj1":"Python", "proj2":"Perl", "proj3":"Java"}
print(proj_language.get("proj4", "Python"), "\n")


# copy() this is a shallow copy, a deep copy contains no reference to the original list or dictionary
words = {'house': 'Haus', 'cat': 'Katze'}
w = words.copy()
words["cat"]="chat"
print(w)
print(words, "\n")
# output = {'house': 'Haus', 'cat': 'Katze'}
# {'house': 'Haus', 'cat': 'chat'}

# Another example
trainings = { "course1":{"title":"Python Training Course for Beginners", 
                         "location":"Frankfurt", 
                         "trainer":"Steve G. Snake"},
              "course2":{"title":"Intermediate Python Training",
                         "location":"Berlin",
                         "trainer":"Ella M. Charming"},
              "course3":{"title":"Python Text Processing Course",
                         "location":"München",
                         "trainer":"Monica A. Snowdon"}
              }

trainings2 = trainings.copy()
trainings["course2"]["title"] = "Perl Training Course for Beginners"
print(trainings2, "\n")
'''
# output
{'course1': {'title': 'Python Training Course for Beginners', 'location': 'Frankfurt', 'trainer': 'Steve G. Snake'},
'course2': {'title': 'Perl Training Course for Beginners', 'location': 'Berlin', 'trainer': 'Ella M. Charming'},
'course3': {'title': 'Python Text Processing Course', 'location': 'München', 'trainer': 'Monica A. Snowdon'}}
'''


# Merging dictionaries
knowledge = {"Frank": {"Perl"}, "Monica":{"C","C++"}}
knowledge2 = {"Guido":{"Python"}, "Frank":{"Perl", "Python"}}
knowledge.update(knowledge2)
print(knowledge, "\n")

# output = {'Frank': {'Perl', 'Python'}, 'Monica': {'C', 'C++'}, 'Guido': {'Python'}}

'''
One example above is the language dictionary. This example is a good example for
the Adapter Method, as we can have numerous language classes, that may require
us to display a word in multiple languages. Therefore we can use an adapter
class which will adapt the object created by the language classes. We would
replace the method in those classes with the adapter method logic. This would
be one way for us to get access to all of those classes and adapt a new logic
to them, updating the dictionary of each class.
Therefore, each class is solely responsible for holding the logic required by
the adapter class. This is why this pattern works well to follow the Single
Responsibility Principle.
'''

