import pandas as pd

from utils import get_all_evidences
from utils import update_bayesian_table

prior = pd.read_csv('prior_probs.csv', index_col=0)
total_likelihood = pd.read_csv('total_likelihoods.csv', index_col=0)

hypotheses = ['Material Damage', 'Minor injuries', 'Major injuries', 'Fatal']
data_types = ['Day', 'Time', 'Vehicle', 'Sex', 'Road', 'Surface']

columns = data_types + hypotheses
total_posterior = pd.DataFrame(columns=columns)

evidences = get_all_evidences()

for row_idx, evidence in enumerate(evidences):
    bayesian = update_bayesian_table(prior, total_likelihood, evidence)
    posterior = bayesian['posterior'].tolist()

    row_data = list(evidence) + posterior
    total_posterior.loc[row_idx] = row_data

total_posterior.to_csv('total_posterior.csv')
print(total_posterior)