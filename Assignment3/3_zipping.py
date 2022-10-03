# Zipping exercises
import numpy as np

# VARIABLES
# 1. faces / houses present 1st
face_1st = ['face1.png']*5 + ['face2.png']*5 + ['face3.png']*5 + ['face4.png']*5 + ['face5.png']*5
house_1st = ['house1.png']*5 + ['house2.png']*5 + ['house3.png']*5 + ['house4.png']*5 + ['house5.png']*5

# 2. faces / houses present 2nd
face_2nd = ['face1.png','face2.png','face3.png','face4.png','face5.png']*5
house_2nd = ['house1.png','house2.png','house3.png','house4.png','house5.png']*5

# 3. post-cues
postcues = ['cue1']*25 + ['cue2']*25

print(face_1st)
print(house_1st)
print(face_2nd)
print(house_2nd)
print(postcues)


# TRIALS
# Face presented first, house second
imgs_order1 = list(zip(face_1st, house_2nd))*2
print(imgs_order1)
print(len(imgs_order1))

# Half of all the possible trials, face presented first
TrialHalf1 = list(zip(imgs_order1, postcues))
print(TrialHalf1)

# House presented first, face second
imgs_order2 = list(zip(house_1st, face_2nd))*2
print(imgs_order2)
print(len(imgs_order2))

# Half of all the possible trials, house presented first
TrialHalf2 = list(zip(imgs_order2, postcues))
print(TrialHalf2)

# All trials combined
Alltrials = TrialHalf1 + TrialHalf2
print(Alltrials)

# Randomize list of trials
np.random.shuffle(Alltrials)
print(Alltrials)
print(len((Alltrials)))