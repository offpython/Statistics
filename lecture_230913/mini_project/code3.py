from code2 import cal_save_likelihoods
outlooks = ['Overcast', 'Rain', 'Sunny']
outlook_data = [[4,0],
                [3,2],
                [2,3]]
outlook_save_name = 'outlook_likelihoods.csv'
cal_save_likelihoods(outlooks, outlook_data, outlook_save_name)
