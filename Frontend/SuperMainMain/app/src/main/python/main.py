import joblib
import string
from nltk.corpus import stopwords
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import pandas as pd
import os
import csv

def process_text(s):
    #Check Punctuation
    nopunc =[char for char in s if char not in string.punctuation]

    # Join the characters  without punctuation
    nopunc =''.join(nopunc)

    #Converting Strings to Lowercase and Removing stopwords
    clean_string = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    return clean_string

def validate_news(url, news):
    try:
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        html = requests.get(url, headers=headers)
        script = BeautifulSoup(html.content, "html.parser")
        parsed_uri = urllib.request.urlparse(url)
        domainName = '{uri.netloc}'.format(uri=parsed_uri)
        news_title = script.find("title").text
    except:
        news_title = ""
        domainName = ""

    full_content = news_title + " " + news

    # detector_pipeline = joblib.load("Backend/detector_pipeline.joblib")
    detector_pipeline = joblib.load("detector_pipeline.joblib")
    result = detector_pipeline.predict([[full_content]])
    rating = detector_pipeline.predict_proba([[full_content]])
    # print(result[0])
    # print(rating)     ## Prints two values 1.Probability of the news being Fake, 2. Probability of the news being True, P(F)+P(T)=1
    # print(rating[0][1])     ## Prints the Probability of the news being True which can be used for the rating
    reliability_rating = rating[0][1]*5
    # print(reliability_rating)

    # Code to update csv file for continous model training, but should write seperate .py or .ipynb file for update_model, So the dataset would be updated and available for commercial use

    # Getting Data to save in the database
    identifier = domainName + " " + news_title
    data = {
        "title":[news_title],
        "text":[news],
        "domain":[domainName],
        "Validity":[result[0]],
        "Identifier":[identifier],
        "Rating/5":[reliability_rating]
    }
    df = pd.DataFrame(data)

    try: 
        if(os.path.isfile("Frontend/SuperMainMain/app/src/main/python/Database/All_DB.csv")):
            df_existing = pd.read_csv("Frontend/SuperMainMain/app/src/main/python/Database/All_DB.csv")
            alreadyExists = (identifier == df_existing["Identifier"]).any()
        else:
            alreadyExists = False
    except:
        alreadyExists = False

    # write/append data frame to CSV files
    if(not alreadyExists):    # Check for duplicates
        df.to_csv("Frontend/SuperMainMain/app/src/main/python/Database/All_DB.csv", mode="a", index=False, header=not os.path.isfile("python/Database/All_DB.csv"))

        if(result[0] == "True"):
            df.to_csv("Frontend/SuperMainMain/app/src/main/python/Database/True_DB.csv", mode="a", index=False, header=not os.path.isfile("python/Database/True_DB.csv"))
        elif(result[0] == "Fake"):
            df.to_csv("Frontend/SuperMainMain/app/src/main/python/Database/Fake_DB.csv", mode="a", index=False, header=not os.path.isfile("python/Database/Fake_DB.csv"))

    return result[0], reliability_rating

def retrieve_all_news():
    all_news_list = retrieve_news("Frontend/SuperMainMain/app/src/main/python/Database/All_DB.csv")
    return all_news_list

def retrieve_true_news():
    true_news_list = retrieve_news("Frontend/SuperMainMain/app/src/main/python/Database/True_DB.csv")
    return true_news_list

def retrieve_fake_news():
    fake_news_list = retrieve_news("Frontend/SuperMainMain/app/src/main/python/Database/Fake_DB.csv")
    return fake_news_list

def retrieve_news(path):
    try:
        with open(path, "r") as file_obj:
            # Skip the heading using next function:
            heading = next(file_obj)
            # Create reader object
            reader_obj = csv.reader(file_obj)
            news_list = list(reader_obj)
            return news_list
    except FileNotFoundError:
        # return empty list if file doesnt exist (means that the database is empty)
        return[]

#Create Login page verification
