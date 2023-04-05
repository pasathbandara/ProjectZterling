# import joblib
import string
from nltk.corpus import stopwords
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import pandas as pd
import os
import csv
import dill
from os.path import dirname, join


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
import sklearn

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

    file_path = join(dirname(__file__), "detector_pipeline.dill")
    if(os.path.getsize(file_path) > 0):
        with open(file_path, 'rb') as detector_file:
            detector_pipeline = dill.load(detector_file)
            result = detector_pipeline.predict([[full_content]])[0]
            # print(result)
            rating = detector_pipeline.predict_proba([[full_content]])[0][1]
            # print(rating)     ## Prints two values 1.Probability of the news being Fake, 2. Probability of the news being True, P(F)+P(T)=1
            ## Prints the Probability of the news being True which can be used for the rating
            reliability_rating = rating*5

            # Getting Data to save in the database
            identifier = domainName + " " + news_title
            data = {
                "title":[news_title],
                "text":[news],
                "domain":[domainName],
                "Validity":result,
                "Identifier":[identifier],
                "Rating/5":reliability_rating
            }
            df = pd.DataFrame(data)

            if(os.path.isfile(join(dirname(__file__), "All_DB.csv"))):
                df_existing = pd.read_csv(join(dirname(__file__), "All_DB.csv"))
                alreadyExists = (identifier == df_existing["Identifier"]).any()
            else:
                alreadyExists = False

            # write/append data frame to CSV files
            if(not alreadyExists):    # Check for duplicates
                df.to_csv(join(dirname(__file__), "All_DB.csv"), mode="a", index=False, header=not os.path.isfile("Database/All_DB.csv"))

                if(result == "True"):
                    df.to_csv(join(dirname(__file__), "True_DB.csv"), mode="a", index=False, header=not os.path.isfile("Database/True_DB.csv"))
                elif(result == "Fake"):
                    df.to_csv(join(dirname(__file__), "Fake_DB.csv"), mode="a", index=False, header=not os.path.isfile("Database/Fake_DB.csv"))

            return result, reliability_rating


    # write/append data frame to CSV files
    # if(not alreadyExists):    # Check for duplicates
    #     df.to_csv("Frontend/SuperMainMain/app/src/main/python/Database/All_DB.csv", mode="a", index=False, header=not os.path.isfile("python/Database/All_DB.csv"))
    #
    #     if(result[0] == "True"):
    #         df.to_csv("Frontend/SuperMainMain/app/src/main/python/Database/True_DB.csv", mode="a", index=False, header=not os.path.isfile("python/Database/True_DB.csv"))
    #     elif(result[0] == "Fake"):
    #         df.to_csv("Frontend/SuperMainMain/app/src/main/python/Database/Fake_DB.csv", mode="a", index=False, header=not os.path.isfile("python/Database/Fake_DB.csv"))
    #
    # return result[0], reliability_rating

def retrieve_all_news():
    all_news_list = retrieve_news(join(dirname(__file__), "All_DB.csv"))
    return all_news_list

def retrieve_true_news():
    true_news_list = retrieve_news(join(dirname(__file__), "True_DB.csv"))
    return true_news_list

def retrieve_fake_news():
    fake_news_list = retrieve_news(join(dirname(__file__), "Fake_DB.csv"))
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
