#!/usr/bin/env python
# coding: utf-8

# # Sentiment Analysis 

# In[13]:


from bs4 import BeautifulSoup


# In[14]:


import requests


# In[15]:


import json


# In[552]:


url = ""


# In[553]:


painting_page = requests.get(url)


# In[554]:


page_html = painting_page.text


# In[30]:


webfile = open("html.txt","r")


# In[31]:


a = str(webfile.readlines())


# In[32]:


a


# In[555]:


print(page_html)


# In[33]:


soup = BeautifulSoup(a, "html.parser")


# In[34]:


credit_div = soup.find_all("p")


# In[35]:


credit_div


# In[36]:


t = []
for a_credit in credit_div:
    t.append(a_credit.text)


# In[37]:


a  = [i.split('.', 1)[0] for i in t]


# In[38]:


a


# In[544]:


SentenceCol = pd.DataFrame(a)


# In[545]:


SentenceCol.columns = ['sentence']


# In[546]:


SentenceCol


# In[547]:


def sentiment_calc(text):
    try:
        return TextBlob(text).sentiment
    except:
        return None
SentenceCol['sentiment'] = SentenceCol['sentence'].apply(sentiment_calc)


# In[548]:


update = SentenceCol


# In[549]:


update[['polarity', 'subjectivity']] = pd.DataFrame(update['sentiment'].tolist(), index=update.index)


# In[550]:


update


# In[551]:


update.to_csv('KUWAIT_WIKI_SENT.csv', index = False)


# # Word Frequency Counts For Historic Timelines

# In[40]:








w = str(a)


# In[41]:


import re

mystr = w
wordList = re.sub("[^\w]", " ",  mystr).split()


# In[42]:


s = [w.lower() for w in wordList]


# In[43]:


s


# In[44]:


from nltk.corpus import stopwords
# ...
filtered_words = [word for word in s if word not in stopwords.words('english')]


# In[45]:


from collections import Counter
counts = Counter(filtered_words)
print(counts)


# In[219]:


import nltk # be sure to have stopwords installed for this using nltk.download_shell()
import pandas as pd 
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# install Vader and make sure you download the lexicon as well
sid = SentimentIntensityAnalyzer()
# this step will return an error if you have not installed the lexicon
summary = {"positive":0,"neutral":0,"negative":0}
for x in s: 
    ss = sid.polarity_scores(x)
    if ss["compound"] == 0.0: 
        summary["neutral"] +=1
    elif ss["compound"] > 0.0:
        summary["positive"] +=1
    else:
        summary["negative"] +=1
print(summary)


# In[253]:


pip install pycorenlp


# In[171]:


import statistics


# In[194]:


def analyze(text): 
    tokenized = nltk.sent_tokenize(text)
    sid = SentimentIntensityAnalyzer()
    scores = []
    compound = []
    for token in tokenized: 
        scores.append(sid.polarity_scores(token))
        for token in tokenized: 
        scores.append(sid.polarity_scores(token))
        print(token)
        print(sid.polarity_scores(token))
    for score in scores: 
        compound.append(score["compound"])
    return scores


# In[214]:


v = []


# In[216]:


v.append(analyze(j))


# In[217]:


v


# In[47]:


a = pd.DataFrame(counts.items())


# In[48]:


a.columns = ['Word','Frequency']


# In[49]:


a.sort_values(by = ['Frequency'], ascending = False)


# In[50]:


a.to_csv("Timeline_WC.csv", index = False)


# In[229]:


a['Word'] = a['Word'].astype(str)


# In[230]:


a


# In[ ]:




