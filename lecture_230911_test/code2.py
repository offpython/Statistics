# 저장된 csv 읽어오기

import pandas as pd

prior_probs = pd.read_csv('prior_probs.csv', index_col=0)
# index_col = 0 => 표를 불러올 때 첫 번째 column이 index column
print(prior_probs)