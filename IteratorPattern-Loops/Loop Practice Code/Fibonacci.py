# Fibonacci.py
# @ author: Administrator
# Date: 25.10.23

print("The Fibonacci Sequence:\n")

# receiving a number that is greater than 3. If not then we loop again
p = "0"
while int(p) < 3:
  p = input("Please enter a number corresponding to the position in the sequence (should be at least 3:) ")

# receiving a positive number. If not then we loop again
q = 0
while q <= 0:
  q = int(input("Please enter number of terms to generate (should be a positive integer): "))
 
print("\n", q, "numbers in the sequence starting from term ", p, ":")
 
# convert p and q to integers
p, q = int(p), int(q)
 
# initialise term counters to zero
p_counter, q_counter = 2, 0
 
#initialise the first two terms in the sequence
n1, n2 = 0, 1

# print Fibonacci sequence based on user input given
# q is length of list
# p is the starting number of the Fibonacci list
while q_counter < q:
    nth = n1 + n2
    n1, n2 = n2, nth
    p_counter += 1
    if p_counter >= p:
        q_counter += 1
        if q_counter < q:
          print(nth, end = ", ")
        else:
          print(nth)
