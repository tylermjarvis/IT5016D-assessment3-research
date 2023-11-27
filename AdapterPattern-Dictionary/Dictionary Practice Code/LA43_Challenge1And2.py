# LA43_Challenge1And2.py
# @ author: Administrator
# Date: 26.10.23

# Dictionary
drum_equipment = {
    "Snare": "SN",
    "Kick Drum": "KD",
    "High Tom": "HT",
    "Med Tom": "MT",
    "Low Tom": "LT",
    "Hi-Hat": "HH"
}

# Updating dictionary
drum_equipment["Crash Cymbal"] = "CC"

cymbals = {
    "Ride": "RD",
    "Splash Cymbal": "SC"
}

# printing original dictionary
print(drum_equipment, "\n")

drum_equipment.update(cymbals)

# printing uodated dictionary
print(drum_equipment, "\n")

'''
The adapter design pattern works in the same way within the dictionary as it
would in a class. It allows us to update the dictionary, regardless of
whether the blocks of code recognise the other block of code.
For example we can add cymbals to drum_equipment through the use of update.
'''
