import pandas as pd
#
# import pandas as pd
#
# day_likelihood = pd.read_csv('day_likelihoods.csv', index_col=0)
# sex_likelihood = pd.read_csv('sex_likelihoods.csv', index_col=0)
# print(day_likelihood, '\n')
# print(sex_likelihood, '\n')
#
# total_likelihood = pd.concat([day_likelihood, sex_likelihood])
# print(total_likelihood)

import pandas as pd

file_names = ['day_likelihoods.csv', 'sex_likelihoods.csv',
              'surface_likelihoods.csv', 'time_likelihoods.csv',
              'vehicle_likelihoods.csv', 'road_likelihoods.csv']
likelihoods = []

for file_name in file_names:
    df = pd.read_csv(file_name, index_col=0)
    likelihoods.append(df)

total_likelihood = pd.concat(likelihoods)
total_likelihood.to_csv('total_likelihoods.csv')
print(total_likelihood)