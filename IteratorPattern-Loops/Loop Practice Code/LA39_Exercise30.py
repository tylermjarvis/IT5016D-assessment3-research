# LA39_Exercise30.py
# @ author: Administrator
# Date: 25.10.23

result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((row == 0 or row == 6) and column >= 0 and column <= 6) or row+column==6):  
            result_str=result_str+"5"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);

#test assertion
#output = Z with 5's

'''
Same as last exercises (exercise 22, 21 and 27), only the result is a Z using
the number 5. It shows that we can use a repeating for loop with iterators to
achieve the same thing with different outcomes. This shows the effectiveness
of iteration and how effective the Iterator Method Pattern can be.
'''
