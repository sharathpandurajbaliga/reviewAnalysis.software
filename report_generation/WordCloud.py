# Python Code to Generate a WordCloud

# Importing the Libraries
from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
from datetime import datetime

def gen_wordcloud(from_date='', to_date = '', csv_file_folder = r'./scrapped_reviews/',max_splits = 4, output_folder = r'./reports/'):
    # Read 'Youtube05-Shakira.csv' file
    #Setting the comment and stop words
    comment_words = ''
    stop_words = set(STOPWORDS)
    for given_file in glob.glob(csv_file_folder+'/*.csv'):
        permit = True
        if(from_date != '' and to_date != ''):
          if(from_date > to_date):
            tmp = from_date 
            from_date = to_date
            to_date = from_date
          base_name = os.path.basename(given_file)
          base_name = base_name.split(".csv")[0]
          date_time_obj = datetime.strptime(base_name, '%d_%b_%Y')
          from_date_time_obj = datetime.strptime(from_date, '%d_%b_%Y')
          to_date_time_obj = datetime.strptime(to_date, '%d_%b_%Y')
          if (date_time_obj <= to_date_time_obj and date_time_obj >= from_date_time_obj):
            permit = True
            print("Using {} for word cloud".format(given_file))
          else:
            permit = False
        if(permit):
          data = pd.read_csv(given_file, sep=';', error_bad_lines=False, encoding ="utf-8")
          # Iterating through the .csv data file
          for val in range(1, max_splits+1):
              sentiment_field = "Sentiment_" + str(val)
              keyword_field = "Keywords_" + str(val)
              for sentiment, Keywords in zip(data[sentiment_field],data[keyword_field]):
                  sentiment = str(sentiment)
                  Keywords = str(Keywords)
                  if sentiment == 'bug':
                      keywords_split = Keywords.split()
                  else:
                      continue
                  
                  #for Keyword in range(len(keywords_split)):
                      #keywords_split[Keyword] = keywords_split[Keyword].lower()

                  comment_words += " ".join(keywords_split) + " "
    # Create the Word Cloud
    
    final_wordcloud = WordCloud(width = 800, height = 800,
                        background_color ='black',
                        stopwords = stop_words,
                        #min_word_length= 8,
                        max_words=60,
                        #collocation_threshold=40,
                        min_font_size = 10).generate(comment_words)

    # Plotting the WordCloud
    plt.figure(figsize=(10, 10), facecolor=None)
    plt.imshow(final_wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    if(not os.path.isdir(output_folder)):
        os.mkdir(output_folder)
    word_cloud_path = output_folder+'{}_word_cloud_for_bugs.png'.format(from_date+'_'+to_date)
    print("Generated WordCloud at : {}".format(word_cloud_path))
    plt.savefig(word_cloud_path, bbox_inches='tight')