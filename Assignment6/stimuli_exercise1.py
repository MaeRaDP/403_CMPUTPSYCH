from psychopy import gui, core, visual, monitors, event
from datetime import datetime
import numpy as np
import os

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================

#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=38.3, distance=60) 
mon.setSizePix([1920,1080])
mon.save()

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, size = [1920, 1080], color=["black"], units='pix', fullscr=True)

# stim exercise 1
os.chdir('C:\Psycopy Images') #stuff you only have to define once at the top of your script
main_dir = os.getcwd() #stuff you only have to define once at the top of your script
image_dir = os.path.join(main_dir,'images') #stuff you only have to define once at the top of your script

# number of trials
nTrials = 10 

# face images stimuli
faceStims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg', 'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']

# stimuli properties
my_image = visual.ImageStim(win, units = 'pix', size = (400,400))

# randomize to show different face images
np.random.shuffle(faceStims)

for trial in range(nTrials):
    my_image.image = os.path.join(image_dir,faceStims[trial])
    my_image.draw()
    win.flip()
    event.waitKeys()
win.close()
