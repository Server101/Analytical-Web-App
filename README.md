# Analytical-Web-App
This app uses the Top Stories API from the New York Times to Display the most common words used in the top current articles based on a specific topic selected by the user. The data is displayed as a line chart and as a wordcloud image hosting on streamlit.
To run the application in Python enviornment type command in terminal: streamlit run main.py

Total packages used:
import json,
import requests,
import nltk,
import response as response,
from nltk import sent_tokenize,
from nltk import word_tokenize,
from nltk.probability import FreqDist,
from nltk.corpus import stopwords,
import main_functions,
from pprint import pprint,
from wordcloud import WordCloud,
import streamlit as st,
import pandas as pd,
import numpy as np,
import time,
import matplotlib.pyplot as plt,
import re,
import ax,
from PIL import Image,
import datetime.

