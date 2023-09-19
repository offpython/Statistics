import pandas as pd

prior = pd.read_csv('prior_probs.csv', index_col=0)
total_likelihood = pd.read_csv('total_likelihoods.csv',
                               index_col=0)

# 첫 번째 정보를 사용한 경우 -> 월요일
bayesian = prior.copy()
bayesian.rename(columns={'severity': 'prior'},
                inplace=True)
bayesian['likelihood'] = total_likelihood.loc['Mon']
bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
norm_const = bayesian['joint'].sum()
bayesian['posterior'] = bayesian['joint'] / norm_const
print(bayesian, '\n')

# 두 번째 정보를 사용한 경우 -> Morning
bayesian['prior'] = bayesian['posterior']  # posterior -> prior
bayesian['likelihood'] = total_likelihood.loc['Morning']
bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
norm_const = bayesian['joint'].sum()
bayesian['posterior'] = bayesian['joint'] / norm_const
print(bayesian, '\n')

# 세 번째 정보를 사용한 경우 -> Jeep
bayesian['prior'] = bayesian['posterior']  # posterior -> prior
bayesian['likelihood'] = total_likelihood.loc['Minibus']
bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
norm_const = bayesian['joint'].sum()
bayesian['posterior'] = bayesian['joint'] / norm_const
print(bayesian, '\n')