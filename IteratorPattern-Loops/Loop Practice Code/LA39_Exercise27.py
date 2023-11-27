# LA39_Exercise27.py
# @ author: Administrator
# Date: 25.10.23

result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 3 or (row == 0 and column > 0 and column <6)):  
            result_str=result_str+"C"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);

#test assertion
#output = T with C's

'''
Same as last exercises (exercise 22 and 21), only the result is a T using the
letter C.
'''
