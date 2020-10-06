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
import re
import ax
from PIL import Image
import datetime


#import seaborn as sns
#from typing import List
#from string import digits

#
# Developer Name: Ricardo Brown
# Class: COP 4813 Professor Reis
# Project 1
# Due 10/05/2020
#
#Image sources: https://www.vectorstock.com/royalty-free-vector/global-network-
#Image Source: https://questionpro.com/blog/rating-scale

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

today = st.date_input("Today is", datetime.datetime.now())

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

st.sidebar.header("Welcome to Ricardo's Web Application")

image0 = Image.open('u2aimg1.jpg')
image2 = Image.open('images/rate1.jpg')

optionsRate = ""
while optionsRate == "":
    st.sidebar.image(image2, use_column_width=True)
    optionsRate = st.sidebar.selectbox(" On a scale from suite man to suite man, how would you rate this project?",
                                ["", "6","5","4","3", "2", "1"])
    counter = 1
    counter = counter + 1
    if counter >= 1:
        break
if optionsRate == "1":
    image1 = Image.open('images/IMPROVED.745.jpg')
   # st.sidebar.write("Thank you! I learned alot in this project")
    st.sidebar.image(image1, use_column_width=True)
    st.success("Thank you! I learned alot in this project")
if optionsRate == "2":
    image2 = Image.open('images/red-white-fi1.png')
    st.success("Thank you! I learned alot in this project")
    st.sidebar.image(image2, use_column_width=True)
if optionsRate == "3":
    image3 = Image.open('images/6-2-confetti.png')

    st.sidebar.image(image3, use_column_width=True)
if optionsRate == "4":
    image4 = Image.open('images/-fireworks457.png')

    st.sidebar.image(image4, use_column_width=True)
if optionsRate == "5":
    image5 = Image.open('images/balloon_52.png')

    st.sidebar.image(image5, use_column_width=True)
if optionsRate == "6":
    image6 = Image.open('images/celebration.1.jpg')

    st.sidebar.image(image6, use_column_width=True)

if userName == "":
    st.write("Loading...")
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i+1)
        time.sleep(0.1)
    st.warning("Please type your name in messagebox above")



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

        #newData = np.array_str(chart_dat)
        #pprint(newData)
        #newData = newData.__dict__
        #print(type(newData))
        #pprint(newData)

        exampleWords = ["New", "Book", "History", "Novel", "Times", "President", "Players", "Car", "Pandemic", "Coronavirus"]
        exampleNumbers = [39 ,15 ,25 ,30 ,14 ,9 ,15 , 12 ,15 ,23]
        # Plotting the graph here,
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(exampleWords, exampleNumbers, marker='o', color='cyan')
        barChart = ax.set(title="The most popular words of all articles topics 2020", xlabel="Words", ylabel="Count")
        plt.setp(ax.get_xticklabels(), rotation=45)
        #plt.show()
        st.pyplot()

#stopwords = stopwords.words("english")
newWords=[]
myData = fdist3.most_common(10)
def save_to_file(data,file_name):
    with open(file_name, "w") as write_file:
        json.dump(data,write_file,indent=2, )
        print("You sucessfully saved to {}.".format(file_name))
#for w in myData:
#   if w not in myData:
#       s = s.replace(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
#       newWords.append(w)
#Began printing most common used words here after taking out the garbage
#fdist3 = FreqDist(clean_words)
#def remove(list):
#    remove_digits = str.maketrans('', '', digits)
#    list = [i.translate(remove_digits) for i in list]
#list = ['4geeks', '3for','4geeks']
#print(remove(list))
#print(list)

def remove(list):
    pattern = '[0-9]'
    list = [re.sub(pattern, '', i) for i in list]
    return list
list = ['4geeks', '3for','4geeks5']
print(remove(list))
data_parameters = {
    1:["new", 9]
}
Chart_data = main_functions.read_from_file("JSON_Files/chartData.json")

#selected_parameters = [data_parameters.get(key) for key in [1]]
#def selectDataFrame(Chart_data:str, selected_parameters: List[str]):
#    entire_ds = pd.read_json(Chart_data)
#    selected_parameters.insert(0, "latitude")

#    try:
#        partial_ds = entire_ds[selected_parameters]
#        print("You made data frame parameters sucess")
#        #partial_ds = partial_ds.rename(columns={"words":"wa", "Count":"ca"})
#        return partial_ds
#   except ValueError:
#        print("Some parameters")#
#st.write(selected_parameters)
#Removing numbers from myData Top Common strings
test_lits = [1, 3 ,4 ,6 ,7]
remove_list = [3, 6, 1, 2, 4, 5, 7,8 , 9, 0]
res = [w for w in myData if w not in remove_list]
#print(res)
#print(type(res))



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

#Error creating
#Where ID is equal to published_date, last 1, 7, 30 days of published.
#Streamlit codes generate numerous errors
    wordcloud = WordCloud().generate(str1)
    # WordCloud Capilization
    plt.figure(figsize=(12, 12))
    plt.imshow(wordcloud)
    plt.axis("off")
    st.image(wordcloud.to_array())



