from code4 import cal_save_likelihoods

vehicle = ['Sedan', 'Jeep', 'Pick Up', 'Minibus', 'Bus', 'Truck']
vehicle_data = [[18, 16, 4, 0],
                [3, 2, 1, 0],
                [4, 14, 6, 0],
                [18, 34, 13, 2],
                [9, 4, 11, 1],
                [26, 55, 44, 8]]

sex = ['Man', 'Woman']
sex_data = [[73, 121, 78, 11],
            [5, 4, 1, 0]]

road = ['Straight flat', 'Straight descend',
        'Straight ascend', 'Curve flat',
        'Curve descend', 'Curve ascend']
road_data = [[30, 54, 32, 5],
             [17, 40, 24, 3],
             [9, 10, 9, 1],
             [6, 10, 2, 0],
             [11, 7, 9, 2],
             [5, 4, 3, 0]]

surface = ['Dry', 'Wet', 'Sandy']
surface_data = [[61, 99, 66, 10],
                [17, 25, 13, 1],
                [0, 1, 0, 0]]

vehicle_save_name = 'vehicle_likelihoods.csv'
sex_save_name = 'sex_likelihoods.csv'
road_save_name = 'road_likelihoods.csv'
surface_save_name = 'surface_likelihoods.csv'

cal_save_likelihoods(vehicle, vehicle_data,
                     vehicle_save_name)
cal_save_likelihoods(sex, sex_data,
                     sex_save_name)
cal_save_likelihoods(road, road_data,
                     road_save_name)
cal_save_likelihoods(surface, surface_data,
                     surface_save_name)