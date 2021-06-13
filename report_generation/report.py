from WordCloud import *
from plot_ratings import *
gen_word_cloud_flag = True
plot_ratings_flag = True
From_Date = '01_Apr_2021'
To_Date = '01_May_2021'
scrapped_data_path =  "./scrapped_reviews/"
Reports_Dir =  "./reports/"
max_num_splits = 4
import sys
From_Date = sys.argv[1]
To_Date = sys.argv[2]
print("Generating Report :")
print(From_Date,To_Date)
# Report generation
# Word Cloud Generation
if(plot_ratings_flag):
  plot_ratings(From_Date, To_Date, scrapped_data_path, Reports_Dir)

if(gen_word_cloud_flag):
  gen_wordcloud(From_Date,To_Date, scrapped_data_path,max_num_splits, Reports_Dir)

