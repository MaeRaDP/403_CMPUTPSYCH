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