# How will you set the starting value in generating random numbers? 

import random
random.seed(42)
print(random.randint(1,10)) 
print(random.random())        
random.seed(42)
print(random.randint(1,10))  
print(random.random()) 