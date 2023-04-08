import string
from flask import Flask, request, jsonify
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
import scipy

app = Flask(__name__)

@app.route('/validate_news', methods=['POST'])
def validate_news():
    data = request.get_json()
    url = data['url']
    news = data['news']
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

    # file_path = "/data/data/com.example.sdgptest2/files/chaquopy/AssetFinder/app/detector_pipeline.dill"
    file_path = join(dirname(__file__), "detector_pipeline.dill")
    if(os.path.getsize(file_path) > 0):
        with open(file_path, 'rb') as detector_file:
            detector_pipeline = dill.load(detector_file)
            result = detector_pipeline.predict([[full_content]])[0]
            rating = detector_pipeline.predict_proba([[full_content]])[0][1]
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

            if(os.path.isfile(join(dirname(__file__), "Database/All_DB.csv"))):
                df_existing = pd.read_csv(join(dirname(__file__), "Database/All_DB.csv"))
                alreadyExists = (identifier == df_existing["Identifier"]).any()
            else:
                alreadyExists = False

            # write/append data frame to CSV files

            # ALLOW REDUNDANCY
            df.to_csv(join(dirname(__file__), "Database/All_DB.csv"), mode="a", index=False, header=not os.path.isfile("Database/All_DB.csv"))

            if(result == "True"):
                df.to_csv(join(dirname(__file__), "Database/True_DB.csv"), mode="a", index=False, header=not os.path.isfile("Database/True_DB.csv"))
            elif(result == "Fake"):
                df.to_csv(join(dirname(__file__), "Database/Fake_DB.csv"), mode="a", index=False, header=not os.path.isfile("Database/Fake_DB.csv"))

            # # DONT ALLOW REDUNDANCY:
            # if(not alreadyExists):    # Check for duplicates
            #     df.to_csv(join(dirname(__file__), "Database/All_DB.csv"), mode="a", index=False, header=not os.path.isfile("Database/All_DB.csv"))

            #     if(result == "True"):
            #         df.to_csv(join(dirname(__file__), "Database/True_DB.csv"), mode="a", index=False, header=not os.path.isfile("Database/True_DB.csv"))
            #     elif(result == "Fake"):
            #         df.to_csv(join(dirname(__file__), "Database/Fake_DB.csv"), mode="a", index=False, header=not os.path.isfile("Database/Fake_DB.csv"))

            return jsonify({'result': result, 'reliability_rating': reliability_rating})
    else:
        return jsonify({'error': 'Model file not found'})

@app.route('/all_news', methods=['GET'])
def retrieve_all_news():
    all_news_list = retrieve_news(join(dirname(__file__), "Database/All_DB.csv"))
    news_dicts = []
    for news in all_news_list:
        news_dict = {
            "title": news[0],
            "text": news[1],
            "domain": news[2],
            "validity": news[3],
            "rating": news[5]
        }
        news_dicts.append(news_dict)
    return jsonify(news_dicts)

@app.route('/true_news', methods=['GET'])
def retrieve_true_news():
    true_news_list = retrieve_news(join(dirname(__file__), "Database/True_DB.csv"))
    news_dicts = []
    for news in true_news_list:
        news_dict = {
            "title": news[0],
            "text": news[1],
            "domain": news[2],
            "validity": news[3],
            "rating": news[5]
        }
        news_dicts.append(news_dict)
    return jsonify(news_dicts)

@app.route('/fake_news', methods=['GET'])
def retrieve_fake_news():
    fake_news_list = retrieve_news(join(dirname(__file__), "Database/Fake_DB.csv"))
    news_dicts = []
    for news in fake_news_list:
        news_dict = {
            "title": news[0],
            "text": news[1],
            "domain": news[2],
            "validity": news[3],
            "rating": news[5]
        }
        news_dicts.append(news_dict)
    return jsonify(news_dicts)

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

def helloworld(a):
    import sys
    # print("Here YOU GO: "+sys.path)
    return a + sys.path


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# url = "https://www.hindustantimes.com/cricket/virat-kohli-ends-century-drought-smashes-maiden-t20i-ton-in-india-vs-afghanistan-asia-cup-super-4-match-101662649555677.html"
# news = '''Virat Kohli reached his first international century since November 2019, as he reached the three-figure mark against Afghanistan in Asia Cup 2022. Team India's star batter Virat Kohli ended the wait for an international century, reaching the three-figure mark against Afghanistan in the Asia Cup Super 4 match in Dubai. Kohli reached his hundred in 53 balls, continuing on his impressive run of form since his return to Team India in the continental tournament. Before the century knock, Kohli had scored two fifties in the Asia Cup as well (59* against Hong Kong and 60 against Pakistan). Kohli's last century in international cricket came in November 2019 against Bangladesh; last month, the batter had endured a thousand days without a ton. The century against Afghanistan was Kohli's 71st international hundred, as he equalled Australia's batting great Ricky Ponting. Only Sachin Tendulkar (100 international centuries) stays ahead of the former India captain now.
# In the game against Afghanistan, Kohli opened the innings alongside stand-in skipper KL Rahul as Rohit Sharma was given rest in the game. This was the first time Kohli came as an opener in T20Is since March 2021, when he had forged a brilliant 94-run stand with Rohit; it was an even better outing for the former Indian captain this time, as he forged a 119-run stand with Rahul, who also scored a much-needed half-century (62 off 40 deliveries). Kohli began aggressively in his knock, racing to his half-century in 32 deliveries. Following the quick dismissals of Rahul and Suryakumar Yadav (6), the 33-year-old batter readjusted his game alongside Rishabh Pant, resorting to singles and doubles through the middle-overs before upping the ante against Afghanistan pacers. He eventually reached his century in the 19th over of the game with a six against Fareed Ahmed – this was his maiden T20I hundred.
# Kohli eventually remained unbeaten on 122 runs off 61 deliveries, smashing 12 fours and six sixes en route to his century knock.'''
# result, reliability_rating = validate_news(url, news)

