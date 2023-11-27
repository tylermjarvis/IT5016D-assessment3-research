# LA39_Exercise21.py
# @ author: Administrator
# Date: 25.10.23

result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or (row == 6 and column != 0 and column < 6)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);

'''
Here we can see the words row and column being used as the iterators instead
of i. They achieve the same result as they are still countered as iterators.
This is important to note as it means you can use words that make more sense
towards the data that you are searching through. For example a ticket in a
number of tickets or a car in a group of cars.
'''
