import pandas as pd

# empty DataFrame 만들기
bayesian = pd.DataFrame(index=['B', 'not B'])
print(bayesian, '\n')

# prior probability 정보 넣기
bayesian['prior'] = [0.1, 0.9]
print(bayesian, '\n')

# likelihood 정보 넣기
bayesian['likelihood'] = [0.9, 0.3]
print(bayesian, '\n')

# joint probability 계산하기
## NOTE : column 출력할 때도 df[column]
bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
print(bayesian, '\n')

# posterior 계산하기
norm_const = bayesian['joint'].sum()
bayesian['posterior'] = bayesian['joint'] / norm_const
print(bayesian, '\n')

# Question.1) 쇼핑백을 많이 들고 있었을 때의 Bayesian table 구현하기
import pandas as pd

bayesian1 = pd.DataFrame(index=['B', 'not B'])

bayesian1['prior'] = [0.1, 0.9]
bayesian1['likelihood'] = [0.7, 0.4]
bayesian1['joint'] = bayesian1['prior'] * bayesian1['likelihood']
norm_const1 = bayesian1['joint'].sum()
bayesian1['posterior'] = bayesian1['joint'] / norm_const1

print(bayesian1, '\n')

# Question.2) 쇼핑백을 많이 들고 있지 않았을 때의 Bayesian table 구현하기
bayesian2 = pd.DataFrame(index=['B', 'not B'])

bayesian2['prior'] = [0.1, 0.9]
bayesian2['likelihood'] = [0.3, 0.6]
bayesian2['joint'] = bayesian2['prior'] * bayesian2['likelihood']
norm_const2 = bayesian2['joint'].sum()
bayesian2['posterior'] = bayesian2['joint'] / norm_const2

print(bayesian2)

