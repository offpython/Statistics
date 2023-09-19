# Time Likelihood 처리하기

import pandas as pd

severities = ['Material Damage', 'Minor injuries', 'Major injuries', 'Fatal']
times = ['Morning', 'Noon', 'Afternoon', 'Night']

data = [[17, 20, 13, 3],
        [27, 35, 13, 1],
        [10, 14, 16, 1],
        [24, 56, 37, 6]]

time_freq_df = pd.DataFrame(columns=severities, index=times, data=data)
time_freq_sums = time_freq_df.sum(axis=0) # axis=0 -> 열별로 합 구하기

time_likelihoods = time_freq_df / time_freq_sums
print(time_likelihoods)

# likelihood table 저장하기
time_likelihoods.to_csv('time_likelihoods.csv')