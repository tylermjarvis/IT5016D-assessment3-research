# Dictionary.py
# @ author: Administrator
# Date: 26.10.23
 
dictionary_1 = {"V344LDA":2000,
                "J245DWE":6350,
                "K265QWS":500}
 
# retrieving a value from the dictionary
print("The car with registration V344LDA is worth $", dictionary_1["V344LDA"])
 
# now for a more challenging example.....
 
# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
 
# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
 
# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
 
# print out some cities
print ('-' * 10)
print ("NY State has: ", cities['NY'])
print ("OR State has: ", cities['OR'])
 
# print some states
print ('-' * 10)
print ("Michigan's abbreviation is: ", states['Michigan'])
print ("Florida's abbreviation is: ", states['Florida'])
 
# do it by using the state then cities dict
print ('-' * 10)
print ("Michigan has: ", cities[states['Michigan']])
print ("Florida has: ", cities[states['Florida']])
 
# print every state abbreviation
print ('-' * 10)
for state, abbrev in states.items():
    print("{0} is abbreviated {1}".format(state, abbrev))
 
# print every city in state
print( '-' * 10)
for abbrev, city in cities.items():
    print ("{0} has the city {1}".format(abbrev, city))
 
# now do both at the same time
print ('-' * 10)
for state, abbrev in states.items():
    print ("{0} state is abbreviated {1} and has city {2}".format(
        state, abbrev, cities[abbrev]))
 
print ('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')
 
if not state:
    print ("Sorry, no Texas.")
 
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print ("The city for the state 'TX' is: {0}".format(city))
 
'''
The car with registration V344LDA is worth $ 2000
----------
NY State has:  New York
OR State has:  Portland
----------
Michigan's abbreviation is:  MI
Florida's abbreviation is:  FL
----------
Michigan has:  Detroit
Florida has:  Jacksonville
----------
New York is abbreviated NY
Michigan is abbreviated MI
Oregon is abbreviated OR
California is abbreviated CA
Florida is abbreviated FL
----------
MI has the city Detroit
NY has the city New York
FL has the city Jacksonville
OR has the city Portland
CA has the city San Francisco
----------
New York state is abbreviated NY and has city New York
Michigan state is abbreviated MI and has city Detroit
Oregon state is abbreviated OR and has city Portland
California state is abbreviated CA and has city San Francisco
Florida state is abbreviated FL and has city Jacksonville
----------
Sorry, no Texas.
The city for the state 'TX' is: Does Not Exist
'''

'''
In this example we could approach a large scale version of this with many states
that include more state information. Therefore we may have a lot of data that we
may want to replace during runtime. A good way to deal with this would be to use
the Adapter Method pattern as we can replace methods to change the data at run
time. This makes having a large amount of data easier to control as we only need
to update the adapter class in order to change the desired output, assuming
that the state class method has the method that we want to adapt to.
This approach is good as we are more likely to follow the Open/Close design
principle, due to using the adapter to change the desired outcome, as opposed to
the state class.
'''

