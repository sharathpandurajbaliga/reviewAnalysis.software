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
fields_to_process = ["Split_1", "Split_2","Split_3","Split_4"]
def process_sentiment(model_dir, input_csv):

    # Process sentiments for all the feedbacks in the given csv file
    predict_unseen_data(model_dir, input_csv)
    return


def main():
    # Fetch review by scrapping
    data = pd.read_csv(review_csv_path, sep=';')

    # Split sentences and write it to csv
    for row in data.iterrows():
        full_review_content = row[review_field]
        review_split_sentences = tokenizer.tokenize(full_review_content)
        pad_length = max_num_splits - len(review_split_sentences)
        if(pad_length > 0):
            pad_list = [""] * pad_length

        for val in range(max_num_splits):
            row[fields_to_process[val]] = review_split_sentences[val]

    columns = sorted(data.columns, reverse=True)
    data.to_csv(review_csv_path, index=False, columns=columns, sep=';')

    # Process sentiments
    for val in range(max_num_splits):
        process_sentiment(sentiment_model_dir, review_csv_path, fields_to_process[val], fields_to_write[val])

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   main()


