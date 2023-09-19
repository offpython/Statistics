import itertools

def get_all_evidences():
    times = ['Morning', 'Noon', 'Afternoon', 'Night']
    days = ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']
    vehicles = ['Sedan', 'Jeep', 'Pick Up', 'Minibus', 'Bus', 'Truck']
    sexes = ['Man', 'Woman']
    roads = ['Straight flat', 'Straight descend', 'Straight ascend',
             'Curve flat', 'Curve descend', 'Curve ascend']
    surfaces = ['Dry', 'Wet', 'Sandy']

    evidences = list(itertools.product(days, times, vehicles, sexes, roads, surfaces))

    return evidences


def from_likelihood_to_posterior(bayesian, total_likelihood, single_data):
    bayesian['likelihood'] = total_likelihood.loc[single_data]
    bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
    norm_const = bayesian['joint'].sum()
    bayesian['posterior'] = bayesian['joint'] / norm_const
    return bayesian

def update_bayesian_table(prior, total_likelihood, data, verbose=False): # verbose : 구체적 설명
    bayesian = prior.copy()
    bayesian.rename(columns={'severity': 'prior'},inplace=True)
    bayesian = from_likelihood_to_posterior(bayesian, total_likelihood, data[0])

    if verbose:
        print(f'======== Data : {data[0]} ========')
        print(bayesian, '\n')

    for single_data in data[1:]:
        bayesian['prior'] = bayesian['posterior']
        bayesian = from_likelihood_to_posterior(bayesian, total_likelihood, single_data)

        if verbose:
            print(f'======== Data : {single_data} ========')
            print(bayesian, '\n')

    return bayesian