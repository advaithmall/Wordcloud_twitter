import snscrape.modules.twitter as sntwitter
import numpy as np
from IPython.display import display
import pandas as pd
import pprint
import re

def preprocess(text_string):
    #print("entered preprocess")
    #print(type(text_string), text_string)
    space_pattern = '\s+'
    url_regex = ('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|'
                 '[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    mention_regex = '@[\w\-]+'
    hashtag_regex = '#[\w\-]+'
    parsed_text = re.sub(space_pattern, ' ', text_string)
    parsed_text = re.sub(url_regex, ' ', parsed_text)
    parsed_text = re.sub(mention_regex, ' ', parsed_text)
    parsed_text = re.sub(hashtag_regex, ' ', parsed_text)
    #print(len(parsed_text))
    #print(parsed_text)
    return parsed_text

#Created a list to append all tweet attributes(data)
print("Please enter a valid twitter username: ")
user_name = input("")
attributes_container = []
text = ""
#Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{user_name}').get_items()):
    #print("i = -> ",i)
    if i > 1000:
        break
    #print(tweet.content)
    text += preprocess(tweet.content)
    #ttributes_container.append(
     #   [tweet.content])
    
#Creating a dataframe from the tweets list above
#tweets_df = pd.DataFrame(attributes_container, columns=[
  # "tweet"])
#display(tweets_df.to_string())
#tweets_df.to_csv('file5.csv')
#pprint.pprint(attributes_container)
print(text)
