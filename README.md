# reviewAnalysis.software


## Architecture
![Image](https://github.com/sharathpandurajbaliga/reviewAnalysis.software/blob/main/Images/workflow.jpeg)

## Usage (Run the following commands step by step):
1. python ./main.py 
2. python ./report_generation/report.py

## Folder Stucture

![Image](https://github.com/sharathpandurajbaliga/reviewAnalysis.software/blob/main/Images/Folders.jpeg)


## Process Overview:
### 1. main.py:
   On running main.py, following things are executed:
#### a. Fetch the reviews
   Scraping reviews for a product from Amazon.com is been implemented and it is readily usable. Please use **reviewAnalysis.software/urls.txt** to mention the review path
      An example Review path is already mentioned. If you want to use your own path for the product, please do the following to get the URL
      
      - Search your product on Amazon.com
      
![Image](https://github.com/sharathpandurajbaliga/reviewAnalysis.software/blob/main/Images/1.PNG)

      - Click on 'Ratings'
      
![Images](https://github.com/sharathpandurajbaliga/reviewAnalysis.software/blob/main/Images/2.PNG)

      - Scroll to the bottom and click on 'See All Reviews' as shown in the screenshot below  --------> 
      
![Images](https://github.com/sharathpandurajbaliga/reviewAnalysis.software/blob/main/Images/3.PNG)

      - Kindly copy the Url and paste it into **reviewAnalysis.software/urls.txt**
      
![Images](https://github.com/sharathpandurajbaliga/reviewAnalysis.software/blob/main/Images/4.PNG)



#### b. Split each review statement into smaller contexts
   NLTK tokenizer is used to split into smaller contexts
#### c. Classify each context into Bug or Feature Request or Other type
   A CNN and RNN based Deep Learning Model is been trained and implemented to classify the contexts into **Bug/Feature/Other**
     The implementation of this can be seen in 
     ***reviewAnalysis.software/CNN_RNN_EN folder***
     The trained model is placed at 
     ***reviewAnalysis.software/SentimentAnalysisModel Folder***
#### d. Pick the important keywords from each context to understand the same
   A Keyword Extractor model (Keybert) is been used to grab the keywords from the given context sentence. The Github link for resource: https://github.com/MaartenGr/KeyBERT
   and it can be also installed as a package using 
     ***pip install keybert***
#### e. Write the output into .csv file
   Once the above steps from a,b,c,d are finished, datewise .csv files containing output form all above the steps are saved at 
     ***reviewAnalysis.software/scrapped_reviews***
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
       
### 2. report_generation/report.py (Please run this after the 1st step is finised i.e main.py)
  The following reports are generated for the processed reviews by step 1. If you like to generate report for custom dates, it is possible to run for custom dates by running 

***./report_generation/report.py 'from_date' 'to_date'***

eg : ./report_generation/report.py '01_Apr_2021' '10_May_2021'

  The reports could be seen in ***reviewAnalysis.software/reports*** folder
#### a. Word Cloud :
   1. A word cloud that suggests the keywords for the customer problems/ bug report is generated for the available review. 
   2. At the end of the process, a wordcloud is generated as ***WordCloud.png*** file at ***reviewAnalysis.software/reports*** folder
   
  
![Image](https://github.com/sharathpandurajbaliga/reviewAnalysis.software/blob/main/Images/wordcloud.jpeg)



#### b. Rating Analysis Plot :
   1. Mean rating for each day of the product is plotted, such that the business owner knows how people are liking/disliking his product on a period of time.
   2. At the end of the process, a plot with variations in the rating each day is ploted as ***RatingAnalysis.png*** file at ***reviewAnalysis.software/reports*** folder 
   
     
     
    
    

