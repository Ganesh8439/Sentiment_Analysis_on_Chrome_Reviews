import pandas as pd
import streamlit as st

st.title("Identifying Review's Rating")
st.header("Instructions")
st.markdown("1.Review column's name should be **Text**")
st.markdown("2.Rating column's name should be **Star**")
st.markdown("3.Rating range should be 0-5")

data = st.file_uploader("Choose a File",type = ['csv'])

if data is not None:
    df = pd.read_csv(data)
    st.write('## Data set')
    st.dataframe(df,3000,500)

# df=pd.read_csv(r"C:\Users\91880\Downloads\chrome_reviews.csv")


# df.info()


s=df[['Text','Star']]

# get_ipython().system('pip install textblob_fr')


from textblob import TextBlob


corpus=[]
for i in s['Text']:
    score = TextBlob(str(i)).sentiment[0]
    if (score > 0):
        corpus.append('Positive')
    elif (score < 0):
        corpus.append('Negative')
    else:
        corpus.append('Neutral')



s["sentiment"]=corpus

s=s[s['sentiment']=='Positive']

s=s[s.Star!=5]
s=s[s.Star!=4]

if st.button("Click for Results") :
        st.download_button(label="Download data as CSV",data=s.to_csv().encode("utf-8"),file_name='data.csv',mime='text/csv',)