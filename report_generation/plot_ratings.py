import pandas as pd
import datetime
from datetime import date, timedelta
import matplotlib.pyplot as plt
import matplotlib
import os

def plot_ratings(from_date, to_date, scrapped_data_path, Reports_Dir):
    from_date_obj = datetime.datetime.strptime(from_date, '%d_%b_%Y')
    to_date_obj = datetime.datetime.strptime(to_date, '%d_%b_%Y')
    '''
    for single_date in (start_date + timedelta(n) for n in range(day_count)):
    for date in range(from_date_obj, to_date_obj):
        d = datetime.datetime.strptime(s, '%m/%d/%Y') + datetime.timedelta(days=1)
        print(d.strftime('%d_%b_%Y'))
    '''
    from_new = from_date_obj.strftime('%Y,%m,%d')
    to_new = to_date_obj.strftime('%Y,%m,%d')
    start_date = date(int(from_new[0:4]), int(from_new[5:7]), int(from_new[8:10]))
    end_date = date(int(to_new[0:4]), int(to_new[5:7]), int(to_new[8:10]))
    delta = timedelta(days=1)
    #fix,ax = plt.subplots()
    plt.xlabel("Dates", fontsize=8)
    plt.ylabel("Average rating out of 5", fontsize=8)
    matplotlib.rcParams.update({'font.size': 8})
    while start_date <= end_date:
        name = (start_date.strftime("%d_%b_%Y"))
        name_to_plot = (start_date.strftime("%d%m"))
        start_date += delta
        csv_name = name + '.csv'
        csv_name = os.path.join(scrapped_data_path,csv_name)
        if(os.path.isfile(csv_name)):
          df = pd.read_csv(csv_name, sep=';')
          avg = df['rating'].mean()
        else:
          avg = 0
        plt.plot(name_to_plot,avg, marker = '*')
    prefix = start_date.strftime("%d_%b_%Y")+'_'+end_date.strftime("%d_%b_%Y")
    #plt.show()
    print("Rating analysis is plotted at : {}".format(Reports_Dir))
    plt.savefig(Reports_Dir+'/{}_rating_analysis.png'.format(prefix))
    return
