import pandas as pd

dataset = pd.read_csv('PlayTennis.csv')
print(dataset, '\n')

yes = dataset[dataset['Play Tennis'] == 'Yes']
no = dataset[dataset['Play Tennis'] == 'No']
print(yes, '\n')
print(no, '\n')
