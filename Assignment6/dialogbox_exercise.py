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