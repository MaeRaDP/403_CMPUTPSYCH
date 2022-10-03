# List operations exercises

import numpy as np

# 1. Create numlist. Multiply this by 2
numlist = [1,2,3]
numlist * 2

# 2. Create numpy aray numarr. Multiply by 2
numarr = np.array([1,2,3])
numarr * 2

print(numlist*2)
print(numarr*2)

# 3. Create strlist. Use operations to create ff. output
strlist = ['do', 're', 'mi', 'fa']

# ['dodo','rere','mimi','fafa']
print([strlist[0]*2] +
      [strlist[1]*2] +
      [strlist[2]*2] +
      [strlist[3]*2])

# ['do','re','mi','fa','do','re','mi','fa']
print(strlist*2)

# ['do','do','re','re','mi','mi','fa','fa']
print([strlist[0]] + [strlist[0]] + 
      [strlist[1]] + [strlist[1]] + 
      [strlist[2]] + [strlist[2]] + 
      [strlist[3]] + [strlist[3]])


# [['do','do'],['re','re'],['mi','mi'],['fa','fa']]
print([[strlist[0]*2],
      [strlist[1]*2],
      [strlist[2]*2],
      [strlist[3]*2]])



