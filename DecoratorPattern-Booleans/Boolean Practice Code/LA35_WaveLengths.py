# LA35_WaveLengths.py
# @ author: Administrator
# date: 25.10.23
 
print("Welcome to wavelength to colour converter\n")
wave_length = int(input("Please enter an integer wavelength between 380 and 750\n"))
print("Thank you, the wavelength that you entered in nanometres is ", wave_length,"\n")
print("The colour for this wavelength is...", end="")

 # The order of this conditional is important, as the higher values need to run first
 # This is because each colour should be displayed at different wave lengths
if wave_length > 750:
    print ("The wavelength entered is higher than the visible spectrum! This is infrared.")
elif wave_length >= 620:
    print ("Red") 
elif wave_length >= 590:
    print("Orange")
elif wave_length >= 570:
    print("Yellow")
elif wave_length >= 495:
    print("Green")
elif wave_length >= 450:
    print("Blue")
elif wave_length >= 380:
    print("Violet")
else:
    print("Indeterminate, :-(, the number entered is "
          "outside the visible spectrum!") # It is important to have a case that deals with
                                           # an incorrect entry or an entry outside of the desired input
 
# test case assertion 1
'''
wave_length = 385
colour is Violet
'''
 
'''
Welcome to wavelength to colour converter
 
Please enter an integer wavelength between 380 and 750
385
Thank you, the wavelength that you entered in nanometres is  385 
 
The colour for this wavelength is...Violet
'''
