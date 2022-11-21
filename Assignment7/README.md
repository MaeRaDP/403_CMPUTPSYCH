# PSYCH 403 - Assignment 7 exercises: MPacificar

## Wait exercises
Fill in the following pseudocode with the real code you have learned so far using "core.wait" (and run it to make sure it works):
```
        #=====================
        #START TRIAL
        #===================== 
        #-draw fixation
        fix_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(.5) #-wait 0.5 seconds, then:
        
        #-draw image
        my_image.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(.5) #-wait 0.5 seconds, then:
        
        #-draw end trial text
        end_trial_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(.5) #-wait 0.5 seconds, then next trial
```



## Clock exercises

1. Create a "wait_timer" to find out exactly how long core.wait(2) presents each image. Make sure this is not counting the time of the whole trial, but only the duration of each image. How precise is core.wait?
- **Answer: core.wait seems to be a little bit precise, however all the trials in both blocks when I did a test run were over by 0.01 seconds which may be crucial for some experiments (e.g., trial 3 in block 1, the image presentation was 1.016... seconds).**
```
from psychopy import gui, core, visual, monitors, event
from datetime import datetime
import numpy as np
import os

# path settings:
os.chdir('C:\Psychopy Exercises') #stuff you only have to define once at the top of your script
main_dir = os.getcwd() #stuff you only have to define once at the top of your script
image_dir = os.path.join(main_dir,'images') #stuff you only have to define once at the top of your script

# stimulus and trial settings:
nTrials = 10
nBlocks = 2

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=38.3, distance=60) 
mon.setSizePix([1920,1080])
mon.save()
#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, size = [1920, 1080], color=["black"], units='pix', fullscr=True)
# get screen size
screenSize = mon.getSizePix()
screenWidth = screenSize[0] # get screen width in pixel
screenHeight = screenSize[1] # get screen height in pixel

#-define experiment start text using psychopy functions
start_msg = "Welcome to the experiment! Press any key to begin."
start_text = visual.TextStim(win, text = start_msg)
#-define block (start)/end text using psychopy functions
block_msg = "Press any key to continue to the next block."
end_trial_msg = "End of trial"
block_text = visual.TextStim(win, text = block_msg)
end_trial_text = visual.TextStim(win, text = end_trial_msg)

#-define stimuli using psychopy functions (images, fixation cross)
faceStims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg', 
             'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']
fix_text = visual.TextStim(win, text = '+')
my_image = visual.ImageStim(win, units = 'pix', size = (400,400))
horizMult = [-1, 1, 1, -1, -1, 1, 1, -1, -1, 1] # list of all possible horizontal positions for 10 trials
vertMult = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1] # list of all possible vertical positions for 10 trials
xCoord = []
yCoord = []
# get all possible horizontal positions in each quadrant per screen width
for i in horizMult:
    xCoord.append(i*(screenSize[0]/4)) 
# get all possible vertical positions in each quadrant per screen height
for i in vertMult:
    yCoord.append(i*(screenSize[1]/4))
# make a list of all X,Y coordinates for image presentation
imageCoords = list(zip(xCoord, yCoord))
# time the duration of stimuli presentation
wait_timer = core.Clock()

#=====================
#START EXPERIMENT
#=====================
#-present start message text
start_text.draw()
win.flip()
#-allow participant to begin experiment with button press
event.waitKeys()

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks
for block in range(nBlocks):
    print('Welcome to block ' + str(block + 1))
    #-present block start message
    block_text.draw()
    win.flip()
    #-randomize order of trials here
    np.random.shuffle(faceStims)
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
    for trial in range(nTrials):
        print('Trial ' + str(trial + 1))
        #-set stimuli and stimulus properties for the current trial
        my_image.image = os.path.join(image_dir,faceStims[trial])
        my_image.pos = imageCoords[trial] # go through imageCoords list for image position
        
        #=====================
        #START TRIAL
        #=====================  
        #-draw fixation
        fix_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(.5) #-wait 0.5 seconds, then:
        
        # reset timer before the image appears
        wait_timer.reset()
        #-draw image
        my_image.draw()
        fix_text.draw() #draw fixation with image
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(1) #-wait 1 second, then:
        # get duration of image presentation
        stimDur = wait_timer.getTime()
        
        #-draw end trial text
        end_trial_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(.5) #-wait 0.5 seconds, then:
        
        print("The duration of image presentation is {} seconds".format(stimDur))
        
#======================
# END OF EXPERIMENT
#======================        
#-close window
win.close()
```

2. Create a "clock_wait_timer" to find out exactly how long each image is presented when you use a clock + while loops. How precise is this?
- **Answer: the precision of clock + while loop is better than the previous one using core.wait. When I ran the code, the first block had 5 out of 10 trials with 1.000...seconds presentation, 1 trial with 1.00...seconds presentation, and 4 trials with 1.0...seconds presentation. The second block had 7 trials with 1.000...seconds presentation, and 3 trials with 1.0...seconds presentation.**

```
from psychopy import gui, core, visual, monitors, event
from datetime import datetime
import numpy as np
import os

# path settings:
os.chdir('C:\Psychopy Exercises') #stuff you only have to define once at the top of your script
main_dir = os.getcwd() #stuff you only have to define once at the top of your script
image_dir = os.path.join(main_dir,'images') #stuff you only have to define once at the top of your script

# stimulus and trial settings:
nTrials = 10
nBlocks = 2

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=38.3, distance=60) 
mon.setSizePix([1920,1080])
mon.save()
#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, size = [1920, 1080], color=["black"], units='pix', fullscr=True)
# get screen size
screenSize = mon.getSizePix()
screenWidth = screenSize[0] # get screen width in pixel
screenHeight = screenSize[1] # get screen height in pixel

#-define experiment start text using psychopy functions
start_msg = "Welcome to the experiment! Press any key to begin."
start_text = visual.TextStim(win, text = start_msg)
#-define block (start)/end text using psychopy functions
block_msg = "Press any key to continue to the next block."
end_trial_msg = "End of trial"
block_text = visual.TextStim(win, text = block_msg)
end_trial_text = visual.TextStim(win, text = end_trial_msg)

#-define stimuli using psychopy functions (images, fixation cross)
faceStims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg', 
             'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']
fix_text = visual.TextStim(win, text = '+')
my_image = visual.ImageStim(win, units = 'pix', size = (400,400))
horizMult = [-1, 1, 1, -1, -1, 1, 1, -1, -1, 1] # list of all possible horizontal positions for 10 trials
vertMult = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1] # list of all possible vertical positions for 10 trials
xCoord = []
yCoord = []
# get all possible horizontal positions in each quadrant per screen width
for i in horizMult:
    xCoord.append(i*(screenSize[0]/4)) 
# get all possible vertical positions in each quadrant per screen height
for i in vertMult:
    yCoord.append(i*(screenSize[1]/4))
# make a list of all X,Y coordinates for image presentation
imageCoords = list(zip(xCoord, yCoord))
# time the duration of stimuli presentation + using while loops
clock_wait_timer = core.Clock()

#=====================
#START EXPERIMENT
#=====================
#-present start message text
start_text.draw()
win.flip()
#-allow participant to begin experiment with button press
event.waitKeys()

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks
for block in range(nBlocks):
    print('Welcome to block ' + str(block + 1))
    #-present block start message
    block_text.draw()
    win.flip()
    #-randomize order of trials here
    np.random.shuffle(faceStims)
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
    for trial in range(nTrials):
        print('Trial ' + str(trial + 1))
        #-set stimuli and stimulus properties for the current trial
        my_image.image = os.path.join(image_dir,faceStims[trial])
        my_image.pos = imageCoords[trial] # go through imageCoords list for image position
        
        #=====================
        #START TRIAL
        #=====================  
        #-draw fixation
        fix_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(.5) #-wait 0.5 seconds, then:
        
        # reset image presentation timer before the image appears
        clock_wait_timer.reset()
        #-draw image using while loop
        while clock_wait_timer.getTime() <= 1: #1 second
            my_image.draw() #-draw image
            fix_text.draw() #draw fixation with image
            #-flip window
            win.flip()
            # get duration of image presentation
            stimDur = clock_wait_timer.getTime()
        
        #-draw end trial text
        end_trial_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(.5) #-wait 0.5 seconds, then:
        
        print("The duration of image presentation is {} seconds".format(stimDur))
        
#======================
# END OF EXPERIMENT
#======================        
#-close window
win.close()
```

3. Create a "countdown_timer" to find out exactly how long each image is presented when you use a CountdownTimer + while loops. How precise is this?
- **Answer: the CountdownTimer function + while loop compared to the previous clock and while loop timer is not better in precision. However, compared to the core.wait, it is a bit better. When I did a test run: the first block had 6 trials with presentation of 1.00... seconds and 4 trials with 1.01... seconds; the second block had 8 trials with 1.00 seconds presentation and 2 with 1.01 seconds presentation. The output for this version sends a warning after each trial about root:DEPRECATED Clock.add() deprecated in favor of .addTime() - this may pose a problem when running the experiment with this timer**

```
from psychopy import gui, core, visual, monitors, event
from datetime import datetime
import numpy as np
import os

# path settings:
os.chdir('C:\Psychopy Exercises') #stuff you only have to define once at the top of your script
main_dir = os.getcwd() #stuff you only have to define once at the top of your script
image_dir = os.path.join(main_dir,'images') #stuff you only have to define once at the top of your script

# stimulus and trial settings:
nTrials = 10
nBlocks = 2

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=38.3, distance=60) 
mon.setSizePix([1920,1080])
mon.save()
#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, size = [1920, 1080], color=["black"], units='pix', fullscr=True)
# get screen size
screenSize = mon.getSizePix()
screenWidth = screenSize[0] # get screen width in pixel
screenHeight = screenSize[1] # get screen height in pixel

#-define experiment start text using psychopy functions
start_msg = "Welcome to the experiment! Press any key to begin."
start_text = visual.TextStim(win, text = start_msg)
#-define block (start)/end text using psychopy functions
block_msg = "Press any key to continue to the next block."
end_trial_msg = "End of trial"
block_text = visual.TextStim(win, text = block_msg)
end_trial_text = visual.TextStim(win, text = end_trial_msg)

#-define stimuli using psychopy functions (images, fixation cross)
faceStims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg', 
             'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']
fix_text = visual.TextStim(win, text = '+')
my_image = visual.ImageStim(win, units = 'pix', size = (400,400))
horizMult = [-1, 1, 1, -1, -1, 1, 1, -1, -1, 1] # list of all possible horizontal positions for 10 trials
vertMult = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1] # list of all possible vertical positions for 10 trials
xCoord = []
yCoord = []
# get all possible horizontal positions in each quadrant per screen width
for i in horizMult:
    xCoord.append(i*(screenWidth/4)) 
# get all possible vertical positions in each quadrant per screen height
for i in vertMult:
    yCoord.append(i*(screenHeight/4))
# make a list of all X,Y coordinates for image presentation
imageCoords = list(zip(xCoord, yCoord))
# countdown timer for stimuli presentation + using while loops
countdown_timer = core.CountdownTimer()
#timer setup used to get image presentation duration
stimTimer = core.Clock() 

#=====================
#START EXPERIMENT
#=====================
#-present start message text
start_text.draw()
win.flip()
#-allow participant to begin experiment with button press
event.waitKeys()

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks
for block in range(nBlocks):
    print('Welcome to block ' + str(block + 1))
    #-present block start message
    block_text.draw()
    win.flip()
    #-randomize order of trials here
    np.random.shuffle(faceStims)
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
    for trial in range(nTrials):
        print('Trial ' + str(trial + 1))
        #-set stimuli and stimulus properties for the current trial
        my_image.image = os.path.join(image_dir,faceStims[trial])
        my_image.pos = imageCoords[trial] # go through imageCoords list for image position
        
        #=====================
        #START TRIAL
        #=====================  
        #-draw fixation
        fix_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(.5) #-wait 0.5 seconds, then:
        
        # reset image presentation timer before the image appears
        countdown_timer.reset()
        countdown_timer.add(1) #add 1 second = trial is 1 second
        imgStartTime = stimTimer.getTime() # get start time of img presentation
        #-draw image using while loop and CountdownTimer function
        while countdown_timer.getTime() > 0: #1 second
            my_image.draw() #-draw image
            fix_text.draw() #draw fixation with image
            win.flip() #-flip window
            imgEndTime = stimTimer.getTime() # get end time of img presentation
        # compute duration of image presentation
        stimDur = imgEndTime - imgStartTime 
        
        #-draw end trial text
        end_trial_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(.5) #-wait 0.5 seconds, then:
        
        print("The duration of image presentation is {} seconds".format(stimDur))
        
#======================
# END OF EXPERIMENT
#======================        
#-close window
win.close()
```
4. Edit your main experiment script so that the trials loop according to a clock timer. Also create and implement a block_timer and a trial_timer.
- **Edited main experiment with CountdownTimer as clock timer to follow instruction per last instruction from Frame-based timing exercises.** 
```
#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions 
import numpy as np
#-import psychopy functions
from psychopy import core, gui, visual, event, monitors
#-import file save functions
import json
#-(import other functions as necessary: os...)
import os
from datetime import datetime

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
os.chdir('C:\Psychopy Exercises')
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
    raise Exception("Could not find the path to data_dir")
if not os.path.isdir(image_dir):
    raise Exception("Could not find the path to image_dir")

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 'gender':'', 'session': 1}
print(exp_info)
# participant info dialog box customization:
my_dlg = gui.DlgFromDict(dictionary = exp_info, title = 'subject info', fixed = ['session'], order = ['session','subject_nr','age','gender','handedness'], show = False)
print("All variables have been created! Now ready to show the dialog box!")
my_dlg.show() # show dialog box after printing variables have been created

#get date and time
date = datetime.now()
print(date)
exp_info['date'] = str(date.hour) + '-' + str(date.day) + '-' + str(date.month) + '-' + str(date.year)
print(exp_info['date'])

#-create a unique filename for the data
filename =  str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'
print(filename)
sub_dir = os.path.join(main_dir,'sub_info',filename)

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks 
nTrials = 10
nBlocks = 2

#-stimulus names (and stimulus extensions, if images) 
imageCounter = 1
pics = [] #from level 1 zipping tutorial = second string of counterbalanced tuple = image name from inside directory to present
while imageCounter < 11:
    pics.append('face' + f"{imageCounter:02d}" + '.jpg')
    imageCounter = imageCounter + 1
print(pics)

#-stimulus properties like size, orientation, location, duration 
stimSize = (400,400) # image stimulus size
# image stimulus location for presentation
horizMult = [-1, 1, 1, -1, -1, 1, 1, -1, -1, 1] # list of all possible horizontal positions for 10 trials
vertMult = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1] # list of all possible vertical positions for 10 trials
screenWidth = 1920 # my screen width in pixel
screenHeight = 1080 # my screen height in pixel
xCoord = [] # list of the image's x coordinates
yCoord = [] # list of the image's y coordinates
for i in horizMult: # get all possible horizontal positions in each quadrant per screen width
    xCoord.append(i*(screenWidth/4)) 
for i in vertMult: # get all possible vertical positions in each quadrant per screen height
    yCoord.append(i*(screenHeight/4))
imageCoords = list(zip(xCoord, yCoord)) # make a list of all X,Y coordinates for image presentation
stimDur = 1 # stimulus duration

#-start message text 
startMessage = "Welcome to the experiment, press any key to begin"

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
ims_in_dir = sorted(os.listdir(image_dir))
for pic in pics:
    if pic in ims_in_dir: # if the pic is in the image directory
        print(pic + " was found!")
    else: raise Exception("The image does not exist!")

#-create counterbalanced list of all conditions 
faceStims = pics
print(faceStims)


#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is correct") 
correctResp = []

#-create an empty list for participant responses (e.g., "on this trial, response was a X") 
participantResp = []

#-create an empty list for response accuracy collection (e.g., "was participant correct?") 
respAccuracy = []

#-create an empty list for response time collection 
RT = []

#-create an empty list for recording the order of stimulus identities 
stimId_order = []

#-create an empty list for recording the order of stimulus properties 
stimProp_order = []

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=38.3, distance=60) 
mon.setSizePix([1920,1080])
mon.save()

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, size = [1920, 1080], color=["black"], units='pix', fullscr=True)

#-define experiment start text unsing psychopy functions
start_msg = "Welcome to the experiment! Press any key to begin."
start_text = visual.TextStim(win, text = start_msg)

#-define block (start)/end text using psychopy functions
block_msg = "Press any key to continue to the next block."
end_trial_msg = "End of trial"
block_text = visual.TextStim(win, text = block_msg)
end_trial_text = visual.TextStim(win, text = end_trial_msg)

#-define stimuli using psychopy functions
fix_text = visual.TextStim(win, text = '+')
my_image = visual.ImageStim(win, units = 'pix', size = stimSize)

#-create response time clock

#-make mouse pointer invisible

#=====================
#CLOCK TIMING INFO
#=====================
# block timer
block_timer = core.CountdownTimer()
# trial timer
trial_timer = core.CountdownTimer()
# timer for image presentation + using while loops
image_timer = core.CountdownTimer()
# timer to get duration of all presentation time
metaTimer = core.Clock() 

#=====================
#START EXPERIMENT
#=====================
#-present start message text
start_text.draw()
win.flip()

#-allow participant to begin experiment with button press
event.waitKeys()

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks
for block in range(nBlocks):
    print('Welcome to block ' + str(block + 1))
    #-present block start message
    block_text.draw()
    win.flip()
    event.waitKeys() # wait for participant to press a key to start block
    # reset block timer once participant begins the block
    block_timer.reset()
    blockStartTime = metaTimer.getTime()
    #-randomize order of trials here
    np.random.shuffle(faceStims)
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
    for trial in range(nTrials):    
        trial_timer.reset()
        trialStartTime = metaTimer.getTime()
        print('Trial ' + str(trial + 1))
        
        #-set stimuli and stimulus properties for the current trial
        my_image.image = os.path.join(image_dir,faceStims[trial])
        my_image.pos = imageCoords[trial] # go through imageCoords list for image position
        
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw fixation
        fix_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(stimDur) #-wait 1 second, then:
        
        # reset image presentation timer before the image appears
        image_timer.reset()
        image_timer.add(1) #add 1 second = trial is 1 second
        imgStartTime = metaTimer.getTime() # get start time of img presentation
        #-draw image using while loop and CountdownTimer function
        while image_timer.getTime() > 0: #1 second
            my_image.draw() #-draw image
            fix_text.draw() #draw fixation with image
            win.flip() #-flip window
            imgEndTime = metaTimer.getTime() # get end time of img presentation
        # compute duration of image presentation
        stimPresDur = imgEndTime - imgStartTime
        print("The duration of image presentation is {} seconds".format(stimPresDur))
        
        #-draw end trial text
        end_trial_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(stimDur) #-wait 1 second, then:
        
        #-collect subject response for that trial
        
        #-collect subject response time for that trial
        
        #-collect accuracy for that trial
        
        trialEndTime = metaTimer.getTime()
        trialDur = trialEndTime - trialStartTime
        print("The duration of the trial is {} seconds".format(trialDur))
    
    blockEndTime = metaTimer.getTime()
    blockDur = blockEndTime - blockStartTime 
    print("The duration of the block is {} seconds".format(blockDur))
    
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
win.close()
#-quit experiment
```

## Frame-based timing exercises
1. Adjust your experiment so that it follows frame-based timing rather than clock timing (comment out the clock-based timing code in case you want to use it again) using for loops and if statements.
```
#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions 
import numpy as np
#-import psychopy functions
from psychopy import core, gui, visual, event, monitors
#-import file save functions
import json
#-(import other functions as necessary: os...)
import os
from datetime import datetime

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
os.chdir('C:\Psychopy Exercises')
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
    raise Exception("Could not find the path to data_dir")
if not os.path.isdir(image_dir):
    raise Exception("Could not find the path to image_dir")

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 'gender':'', 'session': 1}
print(exp_info)
# participant info dialog box customization:
my_dlg = gui.DlgFromDict(dictionary = exp_info, title = "subject info", fixed = ['session'], order = ['session','subject_nr','age','gender','handedness'], show = False)
print("All variables have been created! Now ready to show the dialog box!")
my_dlg.show() # show dialog box after printing variables have been created

#get date and time
date = datetime.now()
print(date)
exp_info['date'] = str(date.hour) + '-' + str(date.day) + '-' + str(date.month) + '-' + str(date.year)
print(exp_info['date'])

#-create a unique filename for the data
filename =  str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'
print(filename)
sub_dir = os.path.join(main_dir,'sub_info',filename)

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks 
nTrials = 10
nBlocks = 2

#-stimulus names (and stimulus extensions, if images) 
imageCounter = 1
pics = [] #from level 1 zipping tutorial = second string of counterbalanced tuple = image name from inside directory to present
while imageCounter < 11:
    pics.append('face' + f"{imageCounter:02d}" + '.jpg')
    imageCounter = imageCounter + 1
print(pics)

#-stimulus properties like size, orientation, location, duration 
stimSize = (400,400) # image stimulus size
# image stimulus location for presentation
horizMult = [-1, 1, 1, -1, -1, 1, 1, -1, -1, 1] # list of all possible horizontal positions for 10 trials
vertMult = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1] # list of all possible vertical positions for 10 trials
screenWidth = 1920 # my screen width in pixel
screenHeight = 1080 # my screen height in pixel
xCoord = [] # list of the image's x coordinates
yCoord = [] # list of the image's y coordinates
for i in horizMult: # get all possible horizontal positions in each quadrant per screen width
    xCoord.append(i*(screenWidth/4)) 
for i in vertMult: # get all possible vertical positions in each quadrant per screen height
    yCoord.append(i*(screenHeight/4))
imageCoords = list(zip(xCoord, yCoord)) # make a list of all X,Y coordinates for image presentation
stimDur = 1 # stimulus duration

#-start message text 
startMessage = "Welcome to the experiment, press any key to begin"

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
ims_in_dir = sorted(os.listdir(image_dir))
for pic in pics:
    if pic in ims_in_dir: # if the pic is in the image directory
        print(pic + " was found!")
    else: raise Exception("The image does not exist!")

#-create counterbalanced list of all conditions 
faceStims = pics
print(faceStims)


#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is correct") 
correctResp = []

#-create an empty list for participant responses (e.g., "on this trial, response was a X") 
participantResp = []

#-create an empty list for response accuracy collection (e.g., "was participant correct?") 
respAccuracy = []

#-create an empty list for response time collection 
RT = []

#-create an empty list for recording the order of stimulus identities 
stimId_order = []

#-create an empty list for recording the order of stimulus properties 
stimProp_order = []

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=38.3, distance=60) 
mon.setSizePix([1920,1080])
mon.save()

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, size = [1920, 1080], color=["black"], units='pix', fullscr=True)

#-define experiment start text unsing psychopy functions
start_msg = "Welcome to the experiment! Press any key to begin."
start_text = visual.TextStim(win, text = start_msg)

#-define block (start)/end text using psychopy functions
block_msg = "Press any key to continue to the next block."
end_trial_msg = "End of trial"
block_text = visual.TextStim(win, text = block_msg)
end_trial_text = visual.TextStim(win, text = end_trial_msg)

#-define stimuli using psychopy functions
fix_text = visual.TextStim(win, text = "+")
my_image = visual.ImageStim(win, units = 'pix', size = stimSize)

#-create response time clock

#-make mouse pointer invisible

#=====================
#CLOCK TIMING
#=====================
# block timer
#block_timer = core.CountdownTimer()
# trial timer
#trial_timer = core.CountdownTimer()
# timer for image presentation + using while loops
#image_timer = core.CountdownTimer()
# timer to get duration of all presentation time
#metaTimer = core.Clock() 

#=====================
#FRAME TIMING
#=====================
#-set refresh rate
refresh=1.0/60.0 #single frame duration in seconds

#-set durations
fix_dur = stimDur # 1 second duration for all stimuli
image_dur = stimDur # 1 second duration for all stimuli
text_dur = stimDur # 1 second duration for all stimuli

#-set frame counts
fix_frames = int(fix_dur / refresh) #whole number
image_frames = int(image_dur / refresh) #whole number
text_frames = int(text_dur / refresh) #whole number
#-the total number of frames to be presented on a trial
total_frames = int(fix_frames + image_frames + text_frames)

#=====================
#START EXPERIMENT
#=====================
#-present start message text
start_text.draw()
win.flip()

#-allow participant to begin experiment with button press
event.waitKeys()

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks
for block in range(nBlocks):
    print('Welcome to block ' + str(block + 1))
    #-present block start message
    block_text.draw()
    win.flip()
    event.waitKeys() # wait for participant to press a key to start block
    # reset block timer once participant begins the block
    #block_timer.reset()
    #blockStartTime = metaTimer.getTime()
    #-randomize order of trials here
    np.random.shuffle(faceStims)
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
    for trial in range(nTrials):    
        #trial_timer.reset()
        #trialStartTime = metaTimer.getTime()
        print('Trial ' + str(trial + 1))
        
        #-set stimuli and stimulus properties for the current trial
        my_image.image = os.path.join(image_dir,faceStims[trial])
        my_image.pos = imageCoords[trial] # go through imageCoords list for image position
        
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        for frameN in range(total_frames):
            # fixation
            if 0 <= frameN <= fix_frames:
                #-draw fixation
                fix_text.draw()
                #-flip window
                win.flip()
                #-wait time (stimulus duration)
                #core.wait(stimDur) #-wait 1 second, then:
                if frameN == fix_frames: #last frame for the fixation
                    print("End fix frame =", frameN) #print frame number
            
            # image
            if fix_frames < frameN <= (fix_frames + image_frames):
        # reset image presentation timer before the image appears
        #image_timer.reset()
        #image_timer.add(1) #add 1 second = trial is 1 second
        #imgStartTime = metaTimer.getTime() # get start time of img presentation
        #-draw image using while loop and CountdownTimer function
        #while image_timer.getTime() > 0: #1 second
                my_image.draw() #-draw image
                fix_text.draw() #draw fixation with image
                win.flip() #-flip window
                if frameN == (fix_frames + image_frames): #last frame for the image
                    print("End image frame =", frameN) #print frame number 
        #    imgEndTime = metaTimer.getTime() # get end time of img presentation
        # compute duration of image presentation
        #stimPresDur = imgEndTime - imgStartTime
        #print("The duration of image presentation is {} seconds".format(stimPresDur))
            
            # end trial
            if (fix_frames + image_frames) < frameN < total_frames: 
                #-draw end trial text
                end_trial_text.draw()
                #-flip window
                win.flip()
                #-wait time (stimulus duration)
                #core.wait(stimDur) #-wait 1 second, then:
                if frameN == (total_frames - 1): #last frame for the text
                    print("End text frame =", frameN) #print frame number    
        
        #-collect subject response for that trial
        
        #-collect subject response time for that trial
        
        #-collect accuracy for that trial
        
        #trialEndTime = metaTimer.getTime()
        #trialDur = trialEndTime - trialStartTime
        #print("The duration of the trial is {} seconds".format(trialDur))
    
    #blockEndTime = metaTimer.getTime()
    #blockDur = blockEndTime - blockStartTime 
    #print("The duration of the block is {} seconds".format(blockDur))
    
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
win.close()
#-quit experiment
```
2. Add a "dropped frame" detector to your script to find out whether your experiment is dropping frames. How many total frames are dropped in the experiment? If 20 or fewer frames are dropped in the whole experiment (1 frame per trial), keep frame-based timing in your experiment. Otherwise, switch back to the CountdownTimer.
```

```
