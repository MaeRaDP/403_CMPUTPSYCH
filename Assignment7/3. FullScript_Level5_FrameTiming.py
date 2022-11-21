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
#CLOCK TIMING INFO
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