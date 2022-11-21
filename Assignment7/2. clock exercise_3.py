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