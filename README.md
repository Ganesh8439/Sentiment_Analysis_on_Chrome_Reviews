# Sentiment_Analysis_on_Chrome_Reviews
# Summary
The dataset consists of google chrome reviews with rating, we have to find out the reviews in which the review is positive and the rating is less.We also have to deploy the app where the user will upload the dataset and it should give the reviews where the content does not match the rating in a CSV file.
# Methods
## Coding
* The required libraries are imported, here we **textblob** library for sentiment analysis
* We define a function **clean** that will clean any text passed to it, It removes all special characters and converts all letters into lower case, performing stemming on words which are not in the manually entered stopwords
* After reading the dataset we apply a for loop which will clean each review in the column text and check for the sematics using **textblob** and certain score is given for each text, If the score is greater than zero it means the review is positive, if the score is less than zero it means the review is negative and if the score is equal to zero then it means neutral
* Now we take only positive reviews and less rating(1 or 2 star) and store it in a dataframe
## Deployment
* Deployment is done using streamlit
* To run the app use the code `streamlit run main.py` in cmd prompt
* Make sure the libraries from the requirements.txt has been installed using `pip install -r requirements.txt`
* The deployement url is <http://192.168.29.220:8501>
![picture alt](http://via.placeholder.com/200x150 "Title is optional")
