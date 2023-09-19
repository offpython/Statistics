# prior 처리하기

import pandas as pd

severities = ['Material Damage', 'Minor injuries', 'Major injuries', 'Fatal']

severity_freq_df = pd.Series(name='severity',
                             index=severities,
                             data=[78, 125, 79, 11])
total_freqs = severity_freq_df.sum() # 293\
prior_probs = severity_freq_df / total_freqs

# csv로 저장
save_file_name = 'prior_probs.csv'
prior_probs.to_csv(save_file_name)

