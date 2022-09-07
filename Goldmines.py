import matplotlib.pyplot as plt
import numpy as np
list_normal = []
list_dar = []
list_time = []
time = 0
for time in range (1 , 1000):
    time = time + 1
    list_time.append(time)

def Any_gold():

   gold_mine = 12
   super_gold_mine = 0
   sum_of_gold = 0
   wood = 0
   for time in range (1, 1000):
    
        
     sum_of_gold = sum_of_gold + 2*gold_mine +8*super_gold_mine
      
     if(wood - 50000 == 0):
        
         super_gold_mine = super_gold_mine + 1
         wood = 0
        
     wood = wood + 10000
     list_dar.append(sum_of_gold)
    


def dar_god_gold():

    gold_mine = 12
    super_gold_mine = 0
    wood = 0

    sum_of_gold = 0
    for time in range (1 , 1000):
    
       
       sum_of_gold = sum_of_gold + 2*gold_mine +8*super_gold_mine
      
       if gold_mine > 0 and wood - 40000 == 0:
            
            gold_mine = gold_mine - 1
            super_gold_mine = super_gold_mine + 1
            wood = 0
            
       elif gold_mine == 0 and wood - 50000 == 0:
        
            super_gold_mine = super_gold_mine + 1
            wood = 0
        
       wood = wood + 10000
       list_normal.append(sum_of_gold) 
     
Any_gold()
dar_god_gold()

plt.plot(list_time , list_normal , list_dar)
print(len(list_time))
print(len(list_normal))
print(len(list_dar))
plt.grid()
plt.show()
