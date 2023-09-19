import pandas as pd

def cal_save_likelihoods(index, data, save_name):
    play = ['Yes', 'No']
    freq_df = pd.DataFrame(columns=play, index=index, data=data)
    freq_sums = freq_df.sum(axis=0)
    likelihoods = freq_df / freq_sums
    likelihoods.to_csv(save_name)
    return likelihoods
