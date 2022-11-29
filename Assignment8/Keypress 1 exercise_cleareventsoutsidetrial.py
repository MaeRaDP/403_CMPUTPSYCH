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