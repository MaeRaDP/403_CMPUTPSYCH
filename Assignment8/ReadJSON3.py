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
