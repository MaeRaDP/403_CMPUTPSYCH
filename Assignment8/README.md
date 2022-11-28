# PSYCH 403 - Assignment 8 exercises: MPacificar

## PsychoPy keypress exercises
1. event.getKeys is prone to collect as many responses as you can make in a trial, but often times you only want to collect one response for a trial. 
Come up with a solution so that only a single response is recorded from event.getKeys 
(e.g., ignoring all responses after the first response). Hint: one solution is used somewhere else in level6.

- **Answer: I used a counter as suggested in Level 6 tutorial for frame-based timing:**
```
#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions 
import numpy as np
#-import psychopy functions
from psychopy import core, gui, visual, event, monitors, logging
#-import file save functions
import json
import csv
#-(import other functions as necessary: os...)
import os
from datetime import datetime
import pandas as pd

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
#correctResp = []
correctResp = [[-1]*nTrials]*nBlocks

#-create an empty list for participant responses (e.g., "on this trial, response was a X") 
#participantResp = []
subjResp = [[-1]*nTrials]*nBlocks

#-create an empty list for response accuracy collection (e.g., "was participant correct?") 
#respAccuracy = []
respAccuracy = [[-1]*nTrials]*nBlocks

#-create an empty list for response time collection 
#RT = []
respTime = [[-1]*nTrials]*nBlocks

#-create an empty list for recording the order of stimulus identities 
stimId_order = []

#-create an empty list for recording the order of stimulus properties 
stimProp_order = []

#-empty list for block
blocks = [[0, 0, 0, 0], [1, 1, 1, 1]]

#-empty list for trial
trials = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

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
rt_clock = core.Clock()

#-make mouse pointer invisible
event.Mouse(visible=False)

#=====================
#FRAME TIMING INFO
#=====================
#-set refresh rate
refresh = 1.0/60.0 #single frame duration in seconds

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

#-dropped frame detector
win.recordFrameIntervals = True #record frames
win.refreshThreshold = refresh + 0.004 # refresh rate plus 4 ms tolerance
logging.console.setLevel(logging.WARNING) # log module to report error warnings to output window

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
    #-randomize order of trials here
    np.random.shuffle(faceStims)
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
    for trial in range(nTrials):    
        print('Trial ' + str(trial + 1))
        
        #-reset response time clock here (I moved it here to reset per trial)
        rt_clock.reset() 
        
        # reset keys for every trial
        event.clearEvents(eventType='keyboard')
        
        #-set stimuli and stimulus properties for the current trial
        my_image.image = os.path.join(image_dir,faceStims[trial])
        my_image.pos = imageCoords[trial] # go through imageCoords list for image position
        
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================
        count = -1 # counting key presses
        
        for frameN in range(total_frames):
            # fixation
            if 0 <= frameN <= fix_frames:
                #-draw fixation
                fix_text.draw()
                #-flip window
                win.flip()
                #-wait time (stimulus duration)
                if frameN == fix_frames: #last frame for the fixation
                    print("End fix frame =", frameN) #print frame number
            
            # image
            if fix_frames < frameN <= (fix_frames + image_frames): 
                my_image.draw() #-draw imagec
                fix_text.draw() #draw fixation with image
                win.flip() #-flip window
                keys = event.getKeys() # collect keypresses after flip of image
                if keys:
                    count = count + 1 # count number of times a key is pressed
                    if 'escape' in keys: # if someone wants to escape the experiment
                        win.close()
                    elif count == 0: # if first time key is pressed
                        respTime = rt_clock.getTime() # collect response time
                        subjResp = keys
                        print(subjResp, respTime)
                if frameN == (fix_frames + image_frames): #last frame for the image
                    print("End image frame =", frameN) #print frame number 

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
        print('Overall, %i frames were dropped.' %win.nDroppedFrames) # print total number of dropped frames every trial
    
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
win.close()
#-quit experiment
core.quit()
```


2. Statement placement in your script is very important when collecting responses and refreshing keypresses. 
What happens if you put event.ClearEvents within the trial loop instead of outside the trial loop? 
- **Answer: In my script to collect the keys properly, the event.ClearEvents function is within the trial loop. When I placed it outside the trial loop but within the for loop for nBlocks, the keys being collected isn't just the response for when the trial started, but it keeps adding irrelevant key presses prior to the time I want the keys to be collected.**
```
#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions 
import numpy as np
#-import psychopy functions
from psychopy import core, gui, visual, event, monitors, logging
#-import file save functions
import json
import csv
#-(import other functions as necessary: os...)
import os
from datetime import datetime
import pandas as pd

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
#correctResp = []
correctResp = [[-1]*nTrials]*nBlocks

#-create an empty list for participant responses (e.g., "on this trial, response was a X") 
#participantResp = []
subjResp = [[-1]*nTrials]*nBlocks

#-create an empty list for response accuracy collection (e.g., "was participant correct?") 
#respAccuracy = []
respAccuracy = [[-1]*nTrials]*nBlocks

#-create an empty list for response time collection 
#RT = []
respTime = [[-1]*nTrials]*nBlocks

#-create an empty list for recording the order of stimulus identities 
stimId_order = []

#-create an empty list for recording the order of stimulus properties 
stimProp_order = []

#-empty list for block
blocks = [[0, 0, 0, 0], [1, 1, 1, 1]]

#-empty list for trial
trials = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

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
rt_clock = core.Clock()

#-make mouse pointer invisible
event.Mouse(visible=False)

#=====================
#FRAME TIMING INFO
#=====================
#-set refresh rate
refresh = 1.0/60.0 #single frame duration in seconds

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

#-dropped frame detector
win.recordFrameIntervals = True #record frames
win.refreshThreshold = refresh + 0.004 # refresh rate plus 4 ms tolerance
logging.console.setLevel(logging.WARNING) # log module to report error warnings to output window

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
    #-randomize order of trials here
    np.random.shuffle(faceStims)
    
    # clear events outside of trial instead of inside trial
    event.clearEvents(eventType='keyboard')
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
    for trial in range(nTrials):    
        print('Trial ' + str(trial + 1))
        
        #-reset response time clock here (I moved it here to reset per trial)
        rt_clock.reset() 
        
        # reset keys for every trial
        #event.clearEvents(eventType='keyboard')
        
        #-set stimuli and stimulus properties for the current trial
        my_image.image = os.path.join(image_dir,faceStims[trial])
        my_image.pos = imageCoords[trial] # go through imageCoords list for image position
        
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================
        count = -1 # counting key presses
        
        for frameN in range(total_frames):
            # fixation
            if 0 <= frameN <= fix_frames:
                #-draw fixation
                fix_text.draw()
                #-flip window
                win.flip()
                #-wait time (stimulus duration)
                if frameN == fix_frames: #last frame for the fixation
                    print("End fix frame =", frameN) #print frame number
            
            # image
            if fix_frames < frameN <= (fix_frames + image_frames):
                my_image.draw() #-draw imagec
                fix_text.draw() #draw fixation with image
                win.flip() #-flip window
                keys = event.getKeys() # collect keypresses after flip of image
                if keys:
                    count = count + 1 # count number of times a key is pressed
                    if 'escape' in keys: # if someone wants to escape the experiment
                        win.close()
                    elif count == 0: # if first time key is pressed
                        respTime = rt_clock.getTime() # collect response time
                        subjResp = keys
                        print(subjResp, respTime)
                if frameN == (fix_frames + image_frames): #last frame for the image
                    print("End image frame =", frameN) #print frame number 

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
        print('Overall, %i frames were dropped.' %win.nDroppedFrames) # print total number of dropped frames every trial
    
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
win.close()
#-quit experiment
core.quit()
```

What happens if you unindent the "if keys:" line?
- **Answer: When I unindented the if keys line, the experiment stops due to an error indicating that there is a NameError: name 'keys' is not defined. This is because the keys variable before the if keys is indented. When the if keys is unindented, the keys variable is not recognized because it's in a different block of code.**
```
#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions 
import numpy as np
#-import psychopy functions
from psychopy import core, gui, visual, event, monitors, logging
#-import file save functions
import json
import csv
#-(import other functions as necessary: os...)
import os
from datetime import datetime
import pandas as pd

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
#correctResp = []
correctResp = [[-1]*nTrials]*nBlocks

#-create an empty list for participant responses (e.g., "on this trial, response was a X") 
#participantResp = []
subjResp = [[-1]*nTrials]*nBlocks

#-create an empty list for response accuracy collection (e.g., "was participant correct?") 
#respAccuracy = []
respAccuracy = [[-1]*nTrials]*nBlocks

#-create an empty list for response time collection 
#RT = []
respTime = [[-1]*nTrials]*nBlocks

#-create an empty list for recording the order of stimulus identities 
stimId_order = []

#-create an empty list for recording the order of stimulus properties 
stimProp_order = []

#-empty list for block
blocks = [[0, 0, 0, 0], [1, 1, 1, 1]]

#-empty list for trial
trials = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

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
rt_clock = core.Clock()

#-make mouse pointer invisible
event.Mouse(visible=False)

#=====================
#FRAME TIMING INFO
#=====================
#-set refresh rate
refresh = 1.0/60.0 #single frame duration in seconds

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

#-dropped frame detector
win.recordFrameIntervals = True #record frames
win.refreshThreshold = refresh + 0.004 # refresh rate plus 4 ms tolerance
logging.console.setLevel(logging.WARNING) # log module to report error warnings to output window

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
    #-randomize order of trials here
    np.random.shuffle(faceStims)
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
    for trial in range(nTrials):    
        print('Trial ' + str(trial + 1))
        
        #-reset response time clock here (I moved it here to reset per trial)
        rt_clock.reset() 
        
        # reset keys for every trial
        event.clearEvents(eventType='keyboard')
        
        #-set stimuli and stimulus properties for the current trial
        my_image.image = os.path.join(image_dir,faceStims[trial])
        my_image.pos = imageCoords[trial] # go through imageCoords list for image position
        
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================
        count = -1 # counting key presses
        
        for frameN in range(total_frames):
            # fixation
            if 0 <= frameN <= fix_frames:
                #-draw fixation
                fix_text.draw()
                #-flip window
                win.flip()
                #-wait time (stimulus duration)
                if frameN == fix_frames: #last frame for the fixation
                    print("End fix frame =", frameN) #print frame number
            
            # image
            if fix_frames < frameN <= (fix_frames + image_frames): 
                my_image.draw() #-draw imagec
                fix_text.draw() #draw fixation with image
                win.flip() #-flip window
                keys = event.getKeys() # collect keypresses after flip of image
                if frameN == (fix_frames + image_frames): #last frame for the image
                    print("End image frame =", frameN) #print frame number 
            if keys:
                    count = count + 1 # count number of times a key is pressed
                    if 'escape' in keys: # if someone wants to escape the experiment
                        win.close()
                    elif count == 0: # if first time key is pressed
                        respTime = rt_clock.getTime() # collect response time
                        subjResp = keys
                        print(subjResp, respTime)
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
        print('Overall, %i frames were dropped.' %win.nDroppedFrames) # print total number of dropped frames every trial
    
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
win.close()
#-quit experiment
core.quit()
```

## Recording data exercises
1. Instead of collecting key name, subject RT, subject accuracy, and correct responses in lists, create a dictionary containing those variables. 
Then, during response collection, append the data to the dictionary instead of filling lists.
```

```


2. Keep in mind that you can pre-define dictionaries or lists for the whole experiment (in which case you have to use [block][trial] indexing to collect responses) or you can do it block-by-block (in which case you can use [trial] indexing). 
Create your lists (or dictionary, if you prefer) within the block loop and switch to [trial] indexing.
```

```



## Save csv exercises
1. Using csv.DictWriter (use your favorite search engine to find the help page), save your dictionary (that you created above) as a .csv file.
```

```



## Save JSON exercises
1. Add JSON filesaving to your experiment script.
```

```



## Read JSON exercises
1. Create a short "read and analysis" script that loads a saved JSON file, performs rudimentary analyses on the data, and prints the means.
```

```



2. Change your "read and analysis" script so that RTs for inaccurate responses are removed from analysis.
```

```



3. Change your "read and analysis" script so that any trials without a response (0 value) are removed from analysis.
```

```
