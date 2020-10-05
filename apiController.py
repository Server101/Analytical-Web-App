import json
import requests
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import main_functions
from pprint import pprint
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import time
import apiController
import matplotlib.pyplot as plt



 #Save all top words and numbers to a file

    #chartData_dict = wordsMenu.__dict__

#main_functions.save_to_file(fdist3.most_common(10), "JSON_Files/chartData.json")
#myChart_data = main_functions.read_from_file("JSON_Files/chartData.json")

#final_words=[]
#final_num=[]
#res = [int(sub.split('.')[1]) for sub in myChart_data]
#print(res)

#for w in myChart_data:
#        if w == str:
#            final_words.append(str)
#        else:
#            final_num.append(str)

#pprint(chartData_dict)
#print(final_words)
#print("==============================")
#print(final_num)
#print(type(myChart_data))
#st.write(pd.DataFrame(myChart_data))

#chart_data = pd.DataFrame(myData, columns =["A","B"])
#chart_data
#t.line_chart(chart_data)
    #main_functions.save_to_file(andriusB_dict, "andrius.json")

    # myChart = main_functions.read_from_file("JSON_Files/chartData.json")
    # print(myChart)

#pd.DataFrame = plt.subplots(figsize=(10,6))
#pd.set(title = "Frequency of Top Story Words", xlabel = "Words", ylabel = "Count")
#myData = fdist3.most_common(10)
#pprint(myData)
#print(type(myData))

#fig, ax = plt.subplots(figsize=(10,6))
#ax.plot(wordLabel, wordsNum, marker = 'o', color = 'cyan')
#barChart = ax.set(title = "Frequency of Top Story Words", xlabel = "Words", ylabel = "Count")
#plt.setp(ax.get_xticklabels(), rotation = 45)
#plt.show()
#st.pyplot()
#st.write(myData)
#Creating Array COntroller
#arr = np.array(myChart_data)
    #print(type(arr))
    #pprint(arr)
    #secondArray = np.array_split(arr,)
    #print(secondArray)



#chart_data = pd.DataFrame(fdist3.most_common(10), columns = ["A","B"])
#pd.DataFrame = plt.subplots(figsize=(10,6))
#chart_data
#st.line_chart(chart_data)
#st.pyplot()
#st.write(pd.DataFrame(myData))
    # to plot the data use line chart
    #st.line_chart(str1)


