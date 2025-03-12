# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 00:04:07 2021

@author: Hp
"""

#Random Strategy
#Selay Berker 2000005092

#passleri saydÄ±r her iteratiÄ±ndan sonra listeye kaydet
import array as ar
import random
from matplotlib import pyplot as plt
import numpy as np

door = []
for i in range(1,51):
    door.append(i)
random.shuffle(door)


door_in = []
for i in range(1,51):
    door_in.append(i)
random.shuffle(door_in)

door_rand = random.sample(door, 25)
print(f'doors to be visited are: {door_rand}')
print(f'number inside each door is: {door_in}')

contestant = []
for i in range(1,51):
    contestant.append(i)
print(f'contestant list: {contestant}')
#pass geÃ§tkten sonra saymaya devam ediyor loopu contion doÄŸru olduÄŸunda kÄ±racak bir ÅŸey
final_pass=[0]    

for itera in range(3000):

    passes=[0]
    random.shuffle(door_in)

    for a in contestant:
        random.shuffle(door)
        door_rand = random.sample(door, 25)
        for b in door_rand:
            if a == door_in[b-1]:
                passes[0] = passes[0]+1
                break
    final_pass.append(passes[0])
print()
print()
plt.hist(final_pass,bins=37,color="#b22222",edgecolor='black', linewidth=0.5)
plt.suptitle("Random Strategy")
plt.axis([0,50,0,400])  
plt.show()
print(final_pass)