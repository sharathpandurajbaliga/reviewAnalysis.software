# reviewAnalysis.software
## Usage (Run the following commands step by step):
1. python main.py 
2. python ./report_generation/report.py
3. ![Image_traffic](https://github.com/ShaminiKoravuna/Traffic_Signs_Recognition/blob/main/output/1.jpg)

## Process Overview:
### 1. main.py:
   On running main.py, following things are executed:
   
#### a. Fetch the reviews
      Scraping reviews for a product from Amazon.com is been implemented and it is readily usable. Please use **reviewAnalysis.software/urls.txt** to mention the review path
      An example Review path is already mentioned. If you want to use your own path for the product, please do the following to get the URL
      - Search your product on Amazon.com
      ![Image_traffic](https://github.com/ShaminiKoravuna/Traffic_Signs_Recognition/blob/main/output/1.jpg)
      - Click on 'Ratings'
      - Scroll to the bottom and click on 'See All Reviews' as shown in the screenshot below  --------> 
      Kindly copy the Url and paste it into **reviewAnalysis.software/urls.txt**
#### b. Split each review statement into smaller contexts
     NLTK tokenizer is used to split into smaller contexts
#### c. Classify each context into Bug or Feature Request or Other type
     A CNN and RNN based Deep Learning Model is been trained and implemented to classify the contexts into **Bug/Feature/Other**
     The implementation of this can be seen in **reviewAnalysis.software/CNN_RNN_EN folder**
     The trained model is placed at **reviewAnalysis.software/SentimentAnalysisModel Folder**
#### d. Pick the important keywords from each context to understand the same
     A Keyword Extractor model (Keybert) is been used to grab the keywords from the given context sentence. The Github link for resource:
     https://github.com/MaartenGr/KeyBERT
     and it can be also installed as a package using **pip install keybert**
#### e. Write the output into .csv file
     Once the above steps from a,b,c,d are finished, datewise .csv files containing output form all above the steps are saved at **reviewAnalysis.software/scrapped_reviews**
     CSV file Definition:
      Name : dd_month_yyyy.csv eg: 01_Jan_2021.csv
      Contents:
          1. Title : Suggests the review title from Amazon Reviews
          2. Content : Holds the complete review content
          3. Date : Date of Publish
          4. Variant : Product type
          5. Verified : If reviewer is Verified Purchaser
          6. Images : url to the Images if any
          7. Author : Name of reviewer
          8. Rating : Value between 1-5
          9. Product : Name of Product
          10. url : URL to the review page
          11. Split_n : Contexts
          12. Sentiment_n : Classification 
          13. Keywords_n : Essential keyword indicators
       
          
    
    

## Folder Stucture

reviewAnalysis.softwar
