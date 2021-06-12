import pandas as pd
from CNN_RNN_EN.predict import *
import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

sentiment_model_dir = ''
review_csv_path = ''
review_csv = ''
review_field = ''
max_num_splits = 4
fields_to_write = ["Sentiment_1", "Sentiment_2", "Sentiment_3", "Sentiment_4"]
fields_to_process = ["Split_1","Split_2","Split_3","Split_4"]
def process_sentiment(model_dir, input_csv, field_to_process, field_to_write):

    # Process sentiments for all the feedbacks in the given csv file
    predict_unseen_data(model_dir, input_csv,field_to_process, field_to_write)
    return



def main():
    # Fetch review by scraping
    #


    review_data = pd.read_csv(review_csv_path, sep=';')
    columns = sorted(review_data.columns, reverse=True)
    sentiment_columns = []
    sentiment_columns.extend(fields_to_write)
    sentiment_columns.extend(fields_to_process)
    sentiment_data = pd.DataFrame(columns=sentiment_columns)

    # Split sentences and write it to csv
    for index, row in review_data.iterrows():
        full_review_content = row[review_field]
        review_split_sentences = tokenizer.tokenize(full_review_content)
        pad_length = max_num_splits - len(review_split_sentences)
        if(pad_length > 0):
            pad_list = [""] * pad_length
            review_split_sentences.extend(pad_list)
        #for val in range(max_num_splits):
        #    sentiment_data[fields_to_process[val]] = review_split_sentences[val]
        sentiment_data.append(review_split_sentences[:3], columns=sentiment_columns)

    data_to_process = pd.concat([review_data, sentiment_data], axis=1)
    data_to_process.to_csv(review_csv, index=False, sep=";")
    # Process sentiments
    for val in range(max_num_splits):
        process_sentiment(sentiment_model_dir, review_csv_path, fields_to_process[val], fields_to_write[val])

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   main()


