import itertools

def get_all_evidence():
    times = ['Morning', 'Noon', 'Afternoon', 'Night']
    days = ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']
    vehicles = ['Sedan', 'Jeep', 'Pick Up', 'Minibus', 'Bus', 'Truck']
    sexes = ['Man', 'Woman']
    roads = ['Straight flat', 'Straight descend', 'Straight ascend',
             'Curve flat', 'Curve descend', 'Curve ascend']
    surfaces = ['Dry', 'Wet', 'Sandy']

    evidences = list(itertools.product(days, times, vehicles, sexes, roads, surfaces))

    return evidences

evidences = get_all_evidence()
print(len(evidences))