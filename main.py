import json
import requests
import nltk
import response as response
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import main_functions
from pprint import pprint
from wordcloud import WordCloud
import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List


# Developer Name: Ricardo Brown
# Class: COP 4813 Professor Reis
# Project 1
# Due 10/03/2020

#These are database, only download 1 time
#nltk.download("punkt")
#nltk.download("stopwords")


#Streamlit Apllication UI
st.title("COP 4813 Web Application Programming")
st.header("Project 1")
st.subheader("Part A - The Stories API")

st.write("This app uses the Top Stories API to Display the most common words used in the top "
        "current articles based on a specific topic selected by the user. The data is displayed "
        "as a line chart and as a wordcloud image.")

st.subheader("I - Topic Selection")
#Accepting user name input saving as string
userName = st.text_input("Please enter your name")
if userName != "":
    st.write("Hi {}! Welcome to the program.".format(userName))

selectTopic = st.selectbox("Select a topic of your interest",
                       ["arts", "automobiles", "books","fashion", "food", "health",
                        "home", "insider", "magazine","movies", "nyregion", "obituaries","opinion",
                        "politics", "realestate", "Science", "sports", "sundayreview", "technology",
                        "theater", "t-magazine", "travel", "upshot", "us", "world"])

st.sidebar.header("Welcome to Ricardo Brown Application")



api_key_dict = main_functions.read_from_file("JSON_Files/api_key.json")
api_key = api_key_dict["my_key"]

url = "https://api.nytimes.com/svc/topstories/v2/" + selectTopic + ".json?api-key=" + api_key
response = requests.get(url).json()
main_functions.save_to_file(response, "JSON_Files/response.json")
my_articles = main_functions.read_from_file("JSON_Files/response.json")


str1 = ""
for i in my_articles["results"]:
    str1 = str1 + i["abstract"]

sentences = sent_tokenize(str1)
words = word_tokenize(str1)
#Get the frequency of words in the text
fdist = FreqDist(words)
#Getting rid of the puntation marks for the word cloud
words_no_punc = []
for w in words:
    if w.isalpha():
        words_no_punc.append(w.lower())
fdist2 = FreqDist(words_no_punc)
#Stopwiords were not intrested in
stopwords = stopwords.words("english")
clean_words=[]
for w in words_no_punc:
    if w not in stopwords:
        clean_words.append(w)
#Began printing most common used words here after taking out the garbage
fdist3 = FreqDist(clean_words)


#Creating the frequent distibution CHART
#===============================
st.subheader("II - Frequency Distribution")
selectFrequency = st.checkbox("Click here to generate frequency distribution")
if selectTopic != "":
    if selectFrequency:
        main_functions.save_to_file(fdist3.most_common(10), "JSON_Files/chartData.json")
        myChart_data = main_functions.read_from_file("JSON_Files/chartData.json")
        myData = fdist3.most_common(10)
        chart_dat = pd.DataFrame(myData, myData, columns = ["Words","Count"])
        st.line_chart(chart_dat)
        chart_dat


data_parameters = {
    1:["new", 9]
}
selected_parameters = [data_parameters.get(key) for key in [1]]
def selectDataFrame(myChart_data:str, selected_parameters: List[str]):
    entire_ds = pd.read_json(myChart_data)
    selected_parameters.insert(0, "latitude")





    #Plotting the graph here
    #fig, ax = plt.subplots(figsize=(10,6))
    #ax.plot(wordLabel, wordsNum, marker = 'o', color = 'cyan')
    #barChart = ax.set(title = "Frequency of Top Story Words", xlabel = "Words", ylabel = "Count")
    #plt.setp(ax.get_xticklabels(), rotation = 45)
    #st.pyplot()
#else:
 #   st.write("")


#Creating Wordcloud for the user
#===============================
st.subheader("III - Wordcloud")
choice = 1
selectCloud = st.checkbox("Click here to generate frequency distribution", key = choice)
if selectCloud:
        wordcloud = WordCloud().generate(str1)
        # WordCloud Capilization
        plt.figure(figsize=(12, 12))
        plt.imshow(wordcloud)
        plt.axis("off")
        st.image(wordcloud.to_array())
else:
    st.write("")



#===PART B MOST POPULAR ARTICLES===
st.header("Part B - Most Popular Articles")
st.subheader("Select if you want to see the most shared, emailed, or viewed articles.")
choice2 = 1

selectPopular= st.selectbox("Select your prefered set of articles",
                               ["","shared", "emailed", "viewed",], key = choice2)
choice3 = 1
selectDays = st.selectbox("Select the period of time (last 30 days)",
                                 ["", "1", "7", "30", ], key=choice3)

# Second Text Wordcloud Paremeters

if selectDays:

    wordcloud = WordCloud().generate(str1)
    # WordCloud Capilization
    plt.figure(figsize=(12, 12))
    plt.imshow(wordcloud)
    plt.axis("off")
    st.image(wordcloud.to_array())



