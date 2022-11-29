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