# Likelihood 계산해주는 함수 만들기

import pandas as pd

def cal_save_likelihoods(index, data, save_name):
    severities = ['Material Damage', 'Minor injuries', 'Major injuries', 'Fatal']

    freq_df = pd.DataFrame(columns=severities, index=index, data=data)
    freq_sums = freq_df.sum(axis=0)
    likelihoods = freq_df / freq_sums

    likelihoods.to_csv(save_name)
    return likelihoods