from keybert import KeyBERT
'''
    Function : extract_keyword
    IN : feedback_text -- a sentence from the feedback. (May be from each aspect)
         keyword_thresh -- the number of keywords needed in the output 
    OUT : descriptor_keywords -- List of keywords that best describes the aspect            
'''


def extract_keyword(feedback_text, keyword_thresh=3):
    kw_model = KeyBERT('distilbert-base-nli-mean-tokens')
    keyword_list = kw_model.extract_keywords(feedback_text, keyphrase_ngram_range=(1, 1), stop_words=None)
    descriptor_keywords = []
    for keyword in keyword_list[:keyword_thresh]:
        descriptor_keywords.append(keyword[0])
    return descriptor_keywords






