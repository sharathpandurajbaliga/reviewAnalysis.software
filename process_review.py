import pandas as pd
import os
def split_scrapped_review_by_date(scrapped_file, split_dir):
  data = pd.read_csv(scrapped_file, sep=';')
  #groupByDate = data.groupby('date')
  #print(groupByDate.groups.keys())
  if(not os.path.isdir(split_dir)):
    os.mkdir(split_dir)
  for name, group in data.groupby('date'):
    group.to_csv(split_dir + '/{}.csv'.format(name.replace(" ","_")), index=False,sep=';')
  '''
  for date_val in groupByDate.groups.keys():
    group_df = groupByDate.get_group(date_val)
    date_val = date_val.replace(" ","_")
    date_val = date_val + '.csv'
    csv_path = os.path.join(split_dir,date_val)
    print("created :{}".format(csv_path))
    if(os.path.isfile(csv_path)):
      group_df.to_csv(csv_path, sep=';') 
  '''
  return









