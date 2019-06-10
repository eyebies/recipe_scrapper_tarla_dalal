# -*- coding: utf-8 -*-
"""
Created on Mon May  6 12:51:12 2019

@author: Rajesh
"""

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

import re
import pandas as pd
import csv 

data1 = pd.read_csv("ingredient_quantities.csv") 
data2 = pd.read_csv("ingred2.csv")

data1 = pd.DataFrame(data1)
data2 = pd.DataFrame(data2)
d = []
d.append(data2.loc[0,"name"])
count = 0

n1 = len(data1)
n2 = len(data2)
##################### updating the quantity table for repeatation ##########################
for i in range(len(data2)):
    if data2.loc[i,"name"] in d:
      #  print("already present :    ",data2.loc[i,"name"])
     #   print(d.index(data2.loc[i,"name"]))
        data1.loc[i,"ingredient_id"] = d.index(data2.loc[i,"name"])+1
        count = count+1
    else:
        d.append(data2.loc[i,"name"])
       # print(d[i])
    
        
data1.to_csv('ingredient_quantities.csv')




#data2 = pd.read_csv("ingredients.csv") 

c = []
clean = []
clean.append(' ')
######################## removing the repeatability in ingredients table ##########
for i in range(len(data2)):
    if data2.loc[i,"name"] in clean:
        print("   ")
        print("index",i)
        data2 = data2.drop(i)
     #   print(data2[:10])
       # print("index",i)
       # i = i-1
    else:
        clean.append(data2.loc[i,"name"])
        

data2.to_csv('ingred2.csv')

Words = ['Grated','Powder','Whole', 'Dry','Split','Cubes','Crushed','Chopped','Peeled','Sliced','Boiled','Whisked',
         'Yellow','Red','Green','Hung','Crumbled','Powdered','Paste','Dried','Boiled','Punjabi','Long','Grained',
         'Broken','Par','-',',','Instant','White','Black','Footlong','Freshly','Ground','Mozzarella','Garden','Whites',
         'Spring','Slices','Beaten','Whipped','Blanched','De-Skinned','And','Frozen','Vertically','Cooked','Soft',
         'Cooking','Quick','Strands','Icing','Plain','Kernels','Low','Fat','Toasted','Steamed','Purple','Shredded',
         'Melted','Deep-Fried','Halved','Mashed','Crumbs','Processed','In','Florets','Sprigs','Wedges','Finely',
         'Leaves','Soaked','Overnight','Roughly','Cut','Basic','Fresh','Thick','Iceberg','Parboiled','Jain','Diagonally',
         'Deseeded','Crush','Slit','Raw','Coarsely','Sprouted','Rock','Grilled','Extra','Roasted','Skimmed','Soya',
         'Mixed','Jelly','Syrup','Condensed','Seeds','Rectangular','Fried','Halves','Long-Grained','Dressing',
         'Calorie','Dough','Drained','Tempered','Essence','Non-Dairy','Whipping','Chilled','Seedless','Balls',
         'Loaf','French','Medium','Sized','Par-Boiled','Cubed','Strips','Juliennes','Low-Fat','Virgin','Self',
         'Rising','Flavoured','Unsweetened','Mix','Torn','Into','Pieces','Roundels','Flakes','Spears','Coloured',
         'Silvers','Round','Sea','Ripe','Sheets','Cube','Chips','Greek','Segments','Pulp','Sponge','Of','Healthy',
         'Baked','Clear','Stick','Large','Fingers','Puree','Mixture','Rich','Unbeaten','Big','Thinly','Peels',
         'Softened','Unpeeled','Tender','Style','Quatered','Ni','Thickly','Unsalted','Veg','Mm.']

data = pd.read_csv("ingred2.csv")
for i in range(len(data)):
    s = str(data.loc[i,"name"])
    print(s.split())
    n = len(s.split())
    w = s.split()
    print(w)
    a = '' 
    j = 0
    while j < n:
        if w[j] in Words:
            print("##############")
            print(w.remove(w[j]))
            n = n-1
            print(n)
         #   print(w)
           # print(w,len(w))
        else:
            j = j+1
            print("*******************")
    print(w)
    print("length",len(w))
    print("i",i)
    for k in range(len(w)):
        a = a+w[k]+' '
    print(a)
    data.loc[i,"name"] = a

data.to_csv('ingred2.csv')

#data.name[:7]
    #print(s)
       
         
#    data.loc[i,"name"] = s


dat = pd.read_csv("ingredients.csv")
for i in range(len(dat)):
    s = str(dat.loc[i,"name"])
    s = ''.join([i for i in s if not i.isdigit()])
    s = s.replace(',','')
    dat.loc[i,"name"] = s

dat.to_csv('ingredien.csv')  






    



