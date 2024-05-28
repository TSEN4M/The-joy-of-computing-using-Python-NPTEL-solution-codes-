import pandas as pd      #provides data structure like data frames
import nltk         #natural language tool kit
from nltk.sentiment.vader import SentimentIntensityAnalyzer     #valence aware dictionary and sentiment reasoner

nltk.downloader.download('vader_lexicon')    # download lexicon, lexicon acts as a dictionary

file='C:/Users/death/Downloads/python/data_file.xlsx'
xl=pd.ExcelFile(file)    #read from excel file using pandas
dfs=xl.parse(xl.sheet_names[0])    #parsing the excel sheet to data frame
dfs =list(dfs['messages'])    #removes the blank rows from the data_frame
print(dfs)
sid=SentimentIntensityAnalyzer()
str1="Tsewang"

for data in dfs:
     print(type(dfs))
     print(type(data))
     a=data.find(str1)
     print(a)
     if a==-1:
          ss=sid.polarity_scores(data)
          print(data)
          for k in ss:
               print(k,ss[k])