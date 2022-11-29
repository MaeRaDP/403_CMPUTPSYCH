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
correctResp = [[0]*nTrials]*nBlocks

#-create an empty list for participant responses (e.g., "on this trial, response was a X") 
subjResp = [[0]*nTrials]*nBlocks

#-create an empty list for response accuracy collection (e.g., "was participant correct?") 
respAccuracy = [[0]*nTrials]*nBlocks

#-create an empty list for response time collection 
respTime = [[0]*nTrials]*nBlocks

#-create an empty list for recording the order of stimulus identities 
stimId = [[0]*nTrials]*nBlocks

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

#-instruction text using psychopy functions (Press A if image on left and L if image on right)
instruction_msg = "You will be presented with different images on the screen. Press A if the image is presented on the left side of the screen or L if the image is presented on the right side of the screen. Please press any key to begin."
instruction_text = visual.TextStim(win, text = instruction_msg)

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
    
    #-present instruction message
    instruction_text.draw()
    win.flip()
    event.waitKeys() # wait for participant to press a key
    
    #-randomize order of trials here
    np.random.shuffle(faceStims)
    print(faceStims)
    
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
                keys = event.getKeys(keyList = ['a', 'l', 'escape']) # collect keypresses after flip of image
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
correctResp = [[0]*nTrials]*nBlocks

#-create an empty list for participant responses (e.g., "on this trial, response was a X") 
subjResp = [[0]*nTrials]*nBlocks

#-create an empty list for response accuracy collection (e.g., "was participant correct?") 
respAccuracy = [[0]*nTrials]*nBlocks

#-create an empty list for response time collection 
respTime = [[0]*nTrials]*nBlocks

#-create an empty list for recording the order of stimulus identities 
stimId = [[0]*nTrials]*nBlocks

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

#-instruction text using psychopy functions (Press A if image on left and L if image on right)
instruction_msg = "You will be presented with different images on the screen. Press A if the image is presented on the left side of the screen or L if the image is presented on the right side of the screen. Please press any key to begin."
instruction_text = visual.TextStim(win, text = instruction_msg)

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
    
    #-present instruction message
    instruction_text.draw()
    win.flip()
    event.waitKeys() # wait for participant to press a key
    
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
                keys = event.getKeys(keyList = ['a', 'l', 'escape']) # collect keypresses after flip of image
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
correctResp = [[0]*nTrials]*nBlocks

#-create an empty list for participant responses (e.g., "on this trial, response was a X") 
subjResp = [[0]*nTrials]*nBlocks

#-create an empty list for response accuracy collection (e.g., "was participant correct?") 
respAccuracy = [[0]*nTrials]*nBlocks

#-create an empty list for response time collection 
respTime = [[0]*nTrials]*nBlocks

#-create an empty list for recording the order of stimulus identities 
stimId = [[0]*nTrials]*nBlocks

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

#-instruction text using psychopy functions (Press A if image on left and L if image on right)
instruction_msg = "You will be presented with different images on the screen. Press A if the image is presented on the left side of the screen or L if the image is presented on the right side of the screen. Please press any key to begin."
instruction_text = visual.TextStim(win, text = instruction_msg)

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

    #-present instruction message
    instruction_text.draw()
    win.flip()
    event.waitKeys() # wait for participant to press a key
    
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
                keys = event.getKeys(keyList = ['a', 'l', 'escape']) # collect keypresses after flip of image
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
**NOTE: I used the tutorial example for these exercises**
1. Instead of collecting key name, subject RT, subject accuracy, and correct responses in lists, create a dictionary containing those variables. 
Then, during response collection, append the data to the dictionary instead of filling lists.

- **For this one, I'm not sure if I'm doing the dictionary thing properly, I kept the lists and converted into dictionary**

```
# import modules/functions
from psychopy import core, event, visual, monitors
import numpy as np

#monitor specs
mon = monitors.Monitor('myMonitor', width=38.3, distance=60) 
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

#blocks, trials, stims, and clocks
nBlocks=2
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill lists for responses
prob = [[0]*nTrials]*nBlocks
corr_resp = [[0]*nTrials]*nBlocks
sub_resp = [[0]*nTrials]*nBlocks
sub_acc = [[0]*nTrials]*nBlocks
resp_time = [[0]*nTrials]*nBlocks

# dictionary stuff
keys = ["Problem", "Correct Response", "Subject Response", "Subject Accuracy", "Response Time"]
values = [prob, corr_resp, sub_resp, sub_acc, resp_time]
subjectData = dict(zip(keys, values))

#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))

for block in range(nBlocks):
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed
                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2 #arbitrary number for inaccurate response 
                                    #(should be something other than 0 to distinguish 
                                    #from non-responses)
                    
        #print results
        print('problem=', prob[block][trial], 'correct response=', 
              corr_resp[block][trial], 'subject response=',sub_resp[block][trial], 
              'subject accuracy=',sub_acc[block][trial])
print(subjectData)
win.close()
```


2. Keep in mind that you can pre-define dictionaries or lists for the whole experiment (in which case you have to use [block][trial] indexing to collect responses) or you can do it block-by-block (in which case you can use [trial] indexing). 
Create your lists (or dictionary, if you prefer) within the block loop and switch to [trial] indexing.

- **Not sure how to properly do the trial indexing**
```
# import modules/functions
from psychopy import core, event, visual, monitors
import numpy as np

#monitor specs
mon = monitors.Monitor('myMonitor', width=38.3, distance=60) 
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

#blocks, trials, stims, and clocks
nBlocks=2
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))

for block in range(nBlocks):
    # dictionary of each var:
    sub_resp = dict()
    sub_acc = dict()
    prob = dict()
    corr_resp = dict()
    resp_time = dict()
    
    #dictionary of all var per block:
    keys = ["Problem", "Correct Response", "Subject Response", "Subject Accuracy", "Response Time"]
    values = [prob, corr_resp, sub_resp, sub_acc, resp_time]
    subjectData = dict(zip(keys, values))
    
    sub_resp[block] = [0]*nTrials
    sub_acc[block] = [0]*nTrials
    prob[block] = [0]*nTrials
    corr_resp[block] = [0]*nTrials
    resp_time[block] = [0]*nTrials

    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed
                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2 #arbitrary number for inaccurate response 
                                    #(should be something other than 0 to distinguish 
                                    #from non-responses)
                    
        #print results
        print('problem=', prob[block][trial], 'correct response=', 
              corr_resp[block][trial], 'subject response=',sub_resp[block][trial], 
              'subject accuracy=',sub_acc[block][trial])
    print(subjectData)
win.close()
```



## Save csv exercises
1. Using csv.DictWriter (use your favorite search engine to find the help page), save your dictionary (that you created above) as a .csv file.
- **I edited the dictionary here how it would be written into the csv file following Dr. Mathewson's example, but it doesn't match the dictionary I created above.**
- **For the version with the dictionary I created above, see [CSV_ExerciseV2.png](https://pages.github.com/) and the output csv file: [V2subject1_math_Nov282022](https://pages.github.com/)**
```
# import modules/functions
from psychopy import core, event, visual, monitors
import numpy as np
import csv
import os
import json as json

#monitor specs
mon = monitors.Monitor('myMonitor', width=38.3, distance=60) 
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

#directory info
filename = 'subject1_math_Nov282022.csv' #file with csv extension
main_dir = os.getcwd()
data_dir = os.path.join(main_dir,'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
filepath_address = os.path.join(data_dir, filename)
print(filepath_address)

#blocks, trials, stims, and clocks
nBlocks=2
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill lists for responses
prob = [[0]*nTrials]*nBlocks
corr_resp = [[0]*nTrials]*nBlocks
sub_resp = [[0]*nTrials]*nBlocks
sub_acc = [[0]*nTrials]*nBlocks
resp_time = [[0]*nTrials]*nBlocks
blocks = [[0, 0, 0, 0], [1, 1, 1, 1]] 
trials = [[0, 1, 2, 3], [0, 1, 2, 3]] 

#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))
    
for block in range(nBlocks):
    subjectData = []
    for a,b,c,d,e,f,g in zip(blocks[block], trials[block], prob[block], corr_resp[block], sub_resp[block], sub_acc[block], resp_time[block]):
            subjectData.append({'Block':a, 'Trial':b, 'Problem':c,'CorrectResponse':d,'SubjectResponse':e,'SubjectAccuracy':f, 'ResponseTime':g})
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed
                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2 #arbitrary number for inaccurate response 
                                    #(should be something other than 0 to distinguish 
                                    #from non-responses)
                    
        #print results
        print('problem=', prob[block][trial], 'correct response=', 
              corr_resp[block][trial], 'subject response=',sub_resp[block][trial], 
              'subject accuracy=',sub_acc[block][trial])
print(subjectData)

with open(filepath_address, 'w', newline='') as csvfile:
    fieldnames = ['Block', 'Trial', 'Problem', 'CorrectResponse', 'SubjectResponse', 'SubjectAccuracy', 'ResponseTime']
    data_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    data_writer.writeheader()
    for block in range(nBlocks):
        for iTrial in range(nTrials):
            data_writer.writerow(subjectData[iTrial])
win.close()
```



## Save JSON exercises
1. Add JSON filesaving to your experiment script.
```
# import modules/functions
from psychopy import core, event, visual, monitors
import numpy as np
import csv
import os
import json as json

#monitor specs
mon = monitors.Monitor('myMonitor', width=38.3, distance=60) 
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

#directory info
filename = 'JSON_subject1_math_Nov282022' #file
main_dir = os.getcwd()
data_dir = os.path.join(main_dir,'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
filepath_address = os.path.join(data_dir, filename)
print(filepath_address)

#blocks, trials, stims, and clocks
nBlocks=2
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill lists for responses
prob = [[0]*nTrials]*nBlocks
corr_resp = [[0]*nTrials]*nBlocks
sub_resp = [[0]*nTrials]*nBlocks
sub_acc = [[0]*nTrials]*nBlocks
resp_time = [[0]*nTrials]*nBlocks
blocks = [[0, 0, 0, 0], [1, 1, 1, 1]] 
trials = [[0, 1, 2, 3], [0, 1, 2, 3]] 

#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))
    
for block in range(nBlocks):
    subjectData = []
    for a,b,c,d,e,f,g in zip(blocks[block], trials[block], prob[block], corr_resp[block], sub_resp[block], sub_acc[block], resp_time[block]):
            subjectData.append({'Block':a, 'Trial':b, 'Problem':c,'CorrectResponse':d,'SubjectResponse':e,'SubjectAccuracy':f, 'ResponseTime':g})
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed
                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2 #arbitrary number for inaccurate response 
                                    #(should be something other than 0 to distinguish 
                                    #from non-responses)
                    
        #print results
        print('problem=', prob[block][trial], 'correct response=', 
              corr_resp[block][trial], 'subject response=',sub_resp[block][trial], 
              'subject accuracy=',sub_acc[block][trial])
              
    with open(filename+ '_block%i.txt'%block, 'w') as outfile:
        json.dump(subjectData, outfile)
        
win.close()
```



## Read JSON exercises
1. Create a short "read and analysis" script that loads a saved JSON file, performs rudimentary analyses on the data, and prints the means.
```
import pandas as pd
import json as json
import os

#directory info
filename = 'JSON_subject1_math_Nov282022' #file
main_dir = os.getcwd()
data_dir = os.path.join(main_dir,'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
filepath_address = os.path.join(data_dir, filename)

#load the imported data as a variable (df)
df = pd.read_json(filename+'_block1.txt')
print(df)

print("Pearson r:")
print(pd.DataFrame.corr(df,method='pearson'))
print("Spearman rho:")
print(pd.DataFrame.corr(df,method='spearman'))

print("Mean Subject Accuracy")
print(sum(df['SubjectAccuracy'])/len(df['SubjectAccuracy']))

print("Mean Response Time")
print(sum(df['ResponseTime'])/len(df['ResponseTime']))
```



2. Change your "read and analysis" script so that RTs for inaccurate responses are removed from analysis.
```
import pandas as pd
import json as json
import os

#directory info
filename = 'JSON_subject1_math_Nov282022' #file
main_dir = os.getcwd()
data_dir = os.path.join(main_dir,'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
filepath_address = os.path.join(data_dir, filename)

#load the imported data as a variable (df)
df = pd.read_json(filename+'_block1.txt')
print(df)

acc_trials = df.loc[df['SubjectAccuracy'] == 1] #show only trials on which subject was correct
print(acc_trials)

print("Mean Subject Accuracy")
print(len(acc_trials)/len(df['SubjectAccuracy']))

print("Mean Response Time")
print(sum(acc_trials['ResponseTime'])/len(acc_trials['ResponseTime']))
```



3. Change your "read and analysis" script so that any trials without a response (0 value) are removed from analysis.
```
import pandas as pd
import json as json
import os

#directory info
filename = 'JSON_subject1_math_Nov282022' #file
main_dir = os.getcwd()
data_dir = os.path.join(main_dir,'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
filepath_address = os.path.join(data_dir, filename)

#load the imported data as a variable (df)
df = pd.read_json(filename+'_block1.txt')
print(df)

sub_trials = df.loc[df['SubjectResponse'] != 0] #show only trials on which subject answered
print(sub_trials)

print("Mean Subject Accuracy")
print(sum(sub_trials['SubjectAccuracy'])/len(df['SubjectAccuracy']))

print("Mean Response Time")
print(sum(sub_trials['ResponseTime'])/len(sub_trials['ResponseTime']))
```
