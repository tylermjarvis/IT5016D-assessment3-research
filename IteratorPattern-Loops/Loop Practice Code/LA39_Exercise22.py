# LA39_Exercise22.py
# @ author: Administrator
# Date: 25.10.23

result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):  
            result_str=result_str+"0 "    
        else:      
            result_str=result_str+"  "    
    result_str=result_str+"\n"    
print(result_str);

#test assertion
#output = M with 0's

'''
Very similar to exercise 21 where we are using row and column as the iterators.
This allows us to write an M with 0, as we loop through each row and column
(up until 7)and print a 0 on specific rows and columns. We can see that it is
an effective way to seach with a large area of information to print the result
that we require, for example an M over white space.
'''
