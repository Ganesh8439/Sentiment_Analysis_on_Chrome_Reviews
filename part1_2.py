# Importing required libraries

import pandas as pd
import streamlit as st
from nltk.stem.porter import PorterStemmer
import re
from textblob import TextBlob

ps=PorterStemmer()

# After intial results found that the word 'many' can make some reviews as positive
stopwords=['many']

# Function to clean a given text
# It removes other characters except a-z, converts text into lower case and removes the given stopwords

def clean(text):
    text = re.sub('[^a-zA-Z]', " ", text)
    text = text.lower()
    text = text.split()
    text = [ps.stem(word) for word in text if word not in stopwords]
    text = ' '.join(text)
    return text

# App creation using streamlit
st.title("Sentiment Analysis on Chrome Reviews")
st.header("Upload review data to find positive reviews with low rating")
st.markdown("1.Ensure column's name of review should be **Text**")
st.markdown("2.Ensure column's name of rating should be **Star**")

#Data read
data = st.file_uploader("Choose a File",type = ['csv'])

#After reading data calculating the results
if data is not None:
    df = pd.read_csv(data)
    st.write('## Wait for Results')




    s=df[['Text','Star']]
    
    
    
    # For loop to clean and analyse the sentiment of each review
    corpus=[]
    for i in s['Text']:
        i=clean(str(i))
        score = TextBlob(str(i)).sentiment[0]
        if (score > 0):
            corpus.append('Positive')
        elif (score < 0):
            corpus.append('Negative')
        else:
            corpus.append('Neutral')
    
    
    #Adding a new column for the sentiment
    s["sentiment"]=corpus
    
    #Taking only positive reviews
    s=s[s['sentiment']=='Positive']
    
    #Removing good ratings
    s=s[s.Star!=5]
    s=s[s.Star!=4]
    s=s[s.Star!=3]
    
    result=s[['Text','Star']]
    #Generating CSV to download
    if st.button("Click to generate CSV file") :
       st.download_button(label="Download as CSV",data=result.to_csv().encode("utf-8"),file_name='data.csv',mime='text/csv',)