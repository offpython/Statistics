def update_bayesian_table(prior, total_likelihood, data):   # lecture_230913= row값 의미
    bayesian = prior.copy()
    bayesian.columns = ['prior']
    bayesian['likelihood'] = total_likelihood.loc[data]

    bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
    norm_const = bayesian['joint'].sum()
    bayesian['posterior'] = bayesian['joint'] / norm_const
    return bayesian
