# FactoryPatternExample.py
# @ author: Administrator
# Date: 21/11/23

# Python Code for factory method 
# it comes under the creational 
# Design Pattern

class FrenchLocalizer:
	# it simply returns the french version
	def __init__(self):
		self.translations = {"car": "voiture", "bike": "bicyclette",
							"cycle":"cyclette"}
	def localize(self, msg):
		# change the message using translations
		return self.translations.get(msg, msg)

class SpanishLocalizer:
	# it simply returns the spanish version

	def __init__(self):
		self.translations = {"car": "coche", "bike": "bicicleta",

							"cycle":"ciclo"}
	def localize(self, msg):
		# change the message using translations
		return self.translations.get(msg, msg)

class EnglishLocalizer:
	# Simply return the same message
	def localize(self, msg):
		return msg

def Factory(language ="English"):
	# Factory Method
	localizers = {
		"French": FrenchLocalizer,
		"English": EnglishLocalizer,
		"Spanish": SpanishLocalizer,
	}

	return localizers[language]()

if __name__ == "__main__":

	f = Factory("French")
	e = Factory("English")
	s = Factory("Spanish")

	message = ["car", "bike", "cycle"]

	for msg in message:
		print(f.localize(msg))
		print(e.localize(msg))
		print(s.localize(msg))


'''
Here the Factory method is calling the language classes using the
EnglishLocalizer as the default language. Therefore we can see that the language
classes are not being called through a variable, but rather the variable being
assigned to the factory method. This allows us to use the factory method as the
calling method to construct language classes, which are used as the base that
the factory method works from. This is a cleaner and more efficient approach
to coding, as it allows you to create different objects using similar
functionality, such as a language. Therefore you can input data that is shared
between classes and produce different outputs with this data, much like a
factory works. Again, we are using the Single Responsibility Principle, to
create each language. This makes it easier for us to test any problems that may
arise from the separate language code blocks.
In the example above, we use the initializer to translate a given message into
different languages. Because these languages have translation in common, we can
use this as the starting initializer that can be called from a factory method
in order to create different language outputs of a message.
'''
