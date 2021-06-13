import pandas as pd
import os
from CNN_RNN_EN.predict import *
import nltk
import nltk.data
from keyword_extractor import *
from amazon_review_scraper.reviews import *
from process_review import *
import glob
from report_generation.WordCloud import *
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

sentiment_model_dir = './SentimentAnalysisModel/'
review_csv_path = './scraped_review.csv'
csv_for_sentiment = './sentiment_review.csv'
urls_filepath = './urls.txt'
selector_file = './selectors.yml'
scrapped_data_path = "./scrapped_reviews/"
Reports_Dir = "./reports/"
num_pages = 5
sortby = 'recent' #helpful
review_field = 'content'
max_num_splits = 4
fields_to_write = ["Sentiment_1", "Sentiment_2", "Sentiment_3", "Sentiment_4"]
fields_to_process = ["Split_1","Split_2","Split_3","Split_4"]
keyword_fields = ["Keywords_1","Keywords_2","Keywords_3","Keywords_4"]
scraper = True
sentiment_check = True
keyword_extract = True
context_extract = True
#From_Date = ''
#To_Date = ''

def process_sentiment(model_dir, input_csv, field_to_process, field_to_write):

    # Process sentiments for all the feedbacks in the given csv file
    predict_unseen_data(model_dir, input_csv,field_to_process, field_to_write)
    return

def main():
    # Fetch review by scraping
    #
    #reviews.scrape(url)
    if(scraper):
      print("Fetching the reviews...Please wait and relax :)")
      reviews(urls_filepath, num_pages, sortby,selector_file, review_csv_path)

    split_scrapped_review_by_date(review_csv_path, scrapped_data_path)
    sentiment_columns = []
    sentiment_columns.extend(fields_to_process)
    sentiment_columns.extend(fields_to_write)
    sentiment_columns.extend(keyword_fields)
    for date_split_file in glob.glob(scrapped_data_path+'/*.csv'):
      review_data = pd.read_csv(date_split_file, sep=';')
      columns = sorted(review_data.columns, reverse=True)
      # Split sentences and write it to csv
      sentiment_data = []
      count = 0
      for index, row in review_data.iterrows():
          count += 1
          full_review_content = row[review_field]
          review_split_sentences = []
          # Split the feedback in to contexts
          if(context_extract):
            try : 
              print("Fetching context from the review ID: {}".format(count))
              review_split_sentences = tokenizer.tokenize(full_review_content)
            except:
              review_split_sentences = ["xyz"] * max_num_splits
          else:
              review_split_sentences = ["xyz"] * max_num_splits
          pad_length = max_num_splits - len(review_split_sentences)
          if(pad_length > 0):
              pad_list = ["xyz"] * pad_length
              review_split_sentences.extend(pad_list)
          #for val in range(max_num_splits):
          #    sentiment_data[fields_to_process[val]] = review_split_sentences[val]
          row_to_write = review_split_sentences[:max_num_splits]
          row_to_write.extend(["xyz"] * max_num_splits)
          # Extract keywords from each context
          for review_split in review_split_sentences[:max_num_splits]:
            if(review_split != '' and keyword_extract):
              keywords = extract_keyword(review_split)
              row_to_write.append(keywords)
            else:
              row_to_write.append([""])
          sentiment_data.append(row_to_write)
      print("{} reviews processed".format(count))
      sentiment_dataframe = pd.DataFrame(sentiment_data, columns=sentiment_columns)
      data_to_process = pd.concat([review_data, sentiment_dataframe], axis=1)
      data_to_process.to_csv(date_split_file, index=False, sep=";")
      # Process sentiments
      if(sentiment_check):
        for val in range(max_num_splits):
            process_sentiment(sentiment_model_dir, date_split_file, fields_to_process[val], fields_to_write[val])
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  nltk.download('punkt')
  main()


