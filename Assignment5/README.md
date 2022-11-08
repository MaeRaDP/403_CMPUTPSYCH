# PSYCH 403 - Assignment 5 exercises: MPacificar

## Experiment structure exercises + Import Exercises
```
#=====================
#IMPORT MODULES
#=====================

#-import numpy and/or numpy functions *
import numpy as np

#-import psychopy functions
from psychopy import core, gui, visual, event

#-import file save functions
import json

#-(import other functions as necessary: os...)
import os

#=====================
#PATH SETTINGS
#=====================

#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()
print(main_dir)

#-define the directory where you will save your data
data_dir = os.path.join(main_dir,'data')
print(data_dir)

#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'images')
print(image_dir)

#-check that these directories exist
if not os.path.isdir(data_dir):
    raise Exception("Could not find the path!")
if not os.path.isdir(image_dir):
    raise Exception("Could not find the path!")

#=====================
#COLLECT PARTICIPANT INFO
#=====================

#-create a dialogue box that will collect current participant number, age, gender, handedness

#get date and time

#-create a unique filename for the data

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================

#-number of trials and blocks *
nTrials = 10
nBlocks = 2

#-stimulus names (and stimulus extensions, if images) *
faces = ['image_dir']*10 #from level 1 = first string of counterbalanced tuple = name of the image directory you want experiment to go to
print(faces)

imageCounter = 1
pics = [] #from level 1 = second string of counterbalanced tuple = image name from inside directory to present
while imageCounter < 11:
    pics.append('face' + f"{imageCounter:02d}" + '.jpg')
    imageCounter = imageCounter + 1
print(pics)
        
#-stimulus properties like size, orientation, location, duration *
stimSize = [200,200];
stimOrient = [10];
stimLoc = [0,0];
stimDur = 1

#-start message text *
startMessage = "Welcome to the experiment, press any key to begin"

#=====================
#PREPARE CONDITION LISTS
#=====================

#-check if files to be used during the experiment (e.g., images) exist
ims_in_dir = sorted(os.listdir(image_dir))
for pic in pics:
    if pic in ims_in_dir:
        print(pic + " was found!")
    else: raise Exception("The image does not exist!")

#-create counterbalanced list of all conditions *
faceStims = list(zip(faces, pics))
print(faceStims)

#=====================
#PREPARE DATA COLLECTION LISTS
#=====================

#-create an empty list for correct responses (e.g., "on this trial, a response of X is correct") *
correctResp = []

#-create an empty list for participant responses (e.g., "on this trial, response was a X") *
participantResp = []

#-create an empty list for response accuracy collection (e.g., "was participant correct?") *
respAccuracy = []

#-create an empty list for response time collection *
RT = []

#-create an empty list for recording the order of stimulus identities *
stimId_order = []

#-create an empty list for recording the order of stimulus properties *
stimProp_order = []

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================

#-define the monitor settings using psychopy functions

#-define the window (size, color, units, fullscreen mode) using psychopy functions

#-define experiment start text unsing psychopy functions

#-define block (start)/end text using psychopy functions

#-define stimuli using psychopy functions

#-create response time clock

#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================

#-present start message text

#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================

#-for loop for nBlocks *
for block in range(nBlocks):
    print('Welcome to block' + str(block + 1))
    #-present block start message
    #-randomize order of trials here *
    np.random.shuffle(faceStims)
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    
    #-for loop for nTrials *
    for trial in range(nTrials):
        print('Trial' + str(trial + 1))
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        #-draw stimulus
        #-...
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        

#-write data to a file
#-close window
#-quit experiment
```

## Import Exercises
```
#=====================
#IMPORT MODULES
#=====================

#-import numpy and/or numpy functions *
import numpy as np

#-import psychopy functions
from psychopy import core, gui, visual, event

#-import file save functions
import json

#-(import other functions as necessary: os...)
import os
```
## Directory Exercises
1. Automate the creation of the list of images ("pics"). Do not write them all out manually.
```
imageCounter = 1
pics = []
while imageCounter < 11:
    pics.append('face' + f"{imageCounter:02d}" + '.jpg')
    imageCounter = imageCounter + 1
print(pics)
```
2. Automate the task of finding out whether each image (as listed in "pics") exists in the "images" directory. Use a for loop and if statements to print "cat1.jpg was found!", "cat2.jpg was found!"... etc. Raise an exception if an image does not exist.
```
ims_in_dir = sorted(os.listdir(image_dir))
for pic in pics:
    if pic in ims_in_dir:
        print(pic + " was found!")
    else: raise Exception("The image does not exist!")
```
3. Fill in the following sections of the experiment structure:
```
#=====================
#PATH SETTINGS
#=====================

#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()

#-define the directory where you will save your data
data_dir = os.path.join(main_dir,'data')

#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'images')

#-check that these directories exist
if not os.path.isdir(data_dir):
    raise Exception("Could not find the path!")
if not os.path.isdir(image_dir):
    raise Exception("Could not find the path!")
    
#=====================
#PREPARE CONDITION LISTS
#=====================

#-check if files to be used during the experiment (e.g., images) exist
imageCounter = 1
pics = []
while imageCounter < 11:
    pics.append('face' + f"{imageCounter:02d}" + '.jpg')
    imageCounter = imageCounter + 1
print(pics)

ims_in_dir = sorted(os.listdir(image_dir))
for pic in pics:
    if pic in ims_in_dir:
        print(pic + " was found!")
    else: raise Exception("The image does not exist!")
```
