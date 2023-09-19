# import pandas as pd
#
# df = pd.DataFrame(index=['row 1', 'row 2'],
#                   columns=['col 1', 'col 2'],
#                   data=[[1, 2,],
#                         [3, 4,]])
#
# # df에 []를 이용하여 뽑으면 column이 뽑힘
# print(df, '\n')
# # row를 뽑는 방법
# print(df['col 1'], '\n')
# # 원소를 뽑는 방법(row name과 column name을 이용해서)
# print(df.loc['row 1', 'col 2'])


# 저장된 csv를 이용해 Bayesian Table 구하기
import pandas as pd

prior = pd.read_csv('prior_probs.csv', index_col=0)
total_likelihood = pd.read_csv('total_likelihoods.csv', index_col=0) # 전체 likelihood

bayesian = prior.copy()
bayesian.rename(columns={'severity' : 'prior'}, inplace=True)

bayesian['likelihood'] = total_likelihood.loc['Mon'] # <- 여기 row값만 바꿔주면 됨
bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
norm_const = bayesian['joint'].sum()
bayesian['posterior'] = bayesian['joint'] / norm_const
print(bayesian, '\n')