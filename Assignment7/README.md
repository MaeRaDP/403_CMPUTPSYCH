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
    xCoord.append(i*(screenSize[0]/4)) 
# get all possible vertical positions in each quadrant per screen height
for i in vertMult:
    yCoord.append(i*(screenSize[1]/4))
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
        countdown_timer.add(1) #add w second = trial is .5 second
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
```

```

## Frame-based timing exercises
1. Adjust your experiment so that it follows frame-based timing rather than clock timing (comment out the clock-based timing code in case you want to use it again) using for loops and if statements.
```

```
2. Add a "dropped frame" detector to your script to find out whether your experiment is dropping frames. How many total frames are dropped in the experiment? If 20 or fewer frames are dropped in the whole experiment (1 frame per trial), keep frame-based timing in your experiment. Otherwise, switch back to the CountdownTimer.
```

```
