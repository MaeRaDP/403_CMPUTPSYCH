# PSYCH 403 - Assignment 6 exercises: MPacificar

## Dialog box exercises
**Use the PsychoPy help page on guis to customize your "exp_info" dialog box: psychopy.gui**
1. Edit the dictionary "exp_info" so you have a variable called "session", with "1" preset as the session number.
2. Edit the "gender" variable in "exp_info" so the subject can write in whatever they want into an empty box, instead of the drop-down list
```
# dictionary setup for the dialog box gui:
exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 'gender':'', 'session': 1}
print(exp_info)
```
**Using DlgFromDict:**
1. Customize my_dlg so that you have a title for your dialog box: "subject info".
```
my_dlg = gui.DlgFromDict(dictionary = exp_info, title = 'subject info')
```
2. Set the variable "session" as fixed. What happens?
```
my_dlg = gui.DlgFromDict(dictionary = exp_info, title = 'subject info', fixed = ['session'])
```
- **Answer: The session variable cannot be edited (non-editable) by the participant if it's set to fixed**

3. Set the order of the variables as session, subject_nr, age, gender, handedness.
```
my_dlg = gui.DlgFromDict(dictionary = exp_info, title = 'subject info', fixed = ['session'], order = ['session','subject_nr','age','gender','handedness'])
```
4. Once you have done all of the above, don't show "my_dlg" right away. Tell your experiment to print "All variables have been created! Now ready to show the dialog box!". Then, show the dialog box.
```
my_dlg = gui.DlgFromDict(dictionary = exp_info, title = 'subject info', fixed = ['session'], order = ['session','subject_nr','age','gender','handedness'], show = False)
print("All variables have been created! Now ready to show the dialog box!")
my_dlg.show()
```
Fill in the following pseudocode with the real code you have learned so far:
```
from psychopy import gui, core
from datetime import datetime
import os

#=====================
#COLLECT PARTICIPANT INFO
#=====================

#-create a dialogue box that will collect current participant number, age, gender, handedness
# dictionary setup for the dialog box gui:
# dictionary setup for the dialog box gui:
exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 'gender':'', 'session': 1}
print(exp_info)

# participant info dialog box customization:
my_dlg = gui.DlgFromDict(dictionary = exp_info, title = 'subject info', fixed = ['session'], order = ['session','subject_nr','age','gender','handedness'], show = False)
print("All variables have been created! Now ready to show the dialog box!")
my_dlg.show() # show dialog box after printing variables have been created

# get date and time
date = datetime.now()
print(date)
exp_info['date'] = str(date.hour) + '-' + str(date.day) + '-' + str(date.month) + '-' + str(date.year)
print(exp_info['date'])

#-create a unique filename for the data
filename =  str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'
print(filename)

main_dir = os.getcwd() 
sub_dir = os.path.join(main_dir,'sub_info',filename)
```

## Monitor and window exercises

Look at the psychopy help page on "window" to help solve the exercises:
1. How does changing "units" affect how you define your window size?
- **Answer: Changing units does not affect how you define the window size, because it applies to the units of the stimuli being drawin in the window**
3. How does changing colorSpace affect how you define the color of your window? Can you define colors by name?
- **Answer: PsychoPy uses three color spaces which are RGB, DKL, and LMS. Changing colorSpace changes how you define the colour of the window. RGB and DKL follows this format: [#,#,#], where # can range -1:1; HSV format is [#,#,#], where # can range 0:1. Colors can also be defined using hex values or by name as listed on the web/X11 color names (e.g., "pink").**

Fill in the following pseudocode with the real code you have learned so far:
```
from psychopy import visual, monitors

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================

#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=38.3, distance=60) 
mon.setSizePix([1920,1080])
mon.save()

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, size = [1920, 1080], color=["black"], units='pix', fullscr=True)
```

## Stimulus exercises
Check the psychopy help page on "ImageStim" to help you solve these exercises:
1. Write a short script that shows different face images from the image directory at 400x400 pixels in size. What does this do to the images? How can you keep the proper image dimensions and still change the size?
- **Answer: specifying the size changes how big the stimulus (image) is showm on the screen. To keep proper image dimensions and still change size, specify the unit according to the image's dimension format (i.e., use units = 'pix' for images with dimensions specified in pixels).**
```
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
```
3. Write a short script that makes one image appear at a time, each in a different quadrant of your screen (put the window in fullscreen mode). Think about how you can calculate window locations without using a trial-and-error method.
```
```
4. Create a fixation cross stimulus (hint:text stimulus).

Fill in the following pseudocode with the real code you have learned so far:
```
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions (images, fixation cross)

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks
    #-present block start message
    #-randomize order of trials here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
        #-set stimuli and stimulus properties for the current trial
        
        #=====================
        #START TRIAL
        #=====================  
        #-draw fixation
        #-flip window
        #-wait time (stimulus duration)
        
        #-draw image
        #-flip window
        #-wait time (stimulus duration)
        
        #-draw end trial text
        #-flip window
        #-wait time (stimulus duration)
        
#======================
# END OF EXPERIMENT
#======================        
#-close window
```
