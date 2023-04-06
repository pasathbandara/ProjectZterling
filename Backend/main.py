# _______________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________
#Joblib Version

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

    detector_pipeline = joblib.load("Backend/detector_pipeline.joblib")
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
        if(os.path.isfile("Backend/Database/All_DB.csv")):
            df_existing = pd.read_csv("Backend/Database/All_DB.csv")
            alreadyExists = (identifier == df_existing["Identifier"]).any()
        else:
            alreadyExists = False
    except:
        alreadyExists = False

    

    # write/append data frame to CSV files
    if(not alreadyExists):    # Check for duplicates
        df.to_csv("Backend/Database/All_DB.csv", mode="a", index=False, header=not os.path.isfile("Backend/Database/All_DB.csv"))

        if(result[0] == "True"):
            df.to_csv("Backend/Database/True_DB.csv", mode="a", index=False, header=not os.path.isfile("Backend/Database/True_DB.csv"))
        elif(result[0] == "Fake"):
            df.to_csv("Backend/Database/Fake_DB.csv", mode="a", index=False, header=not os.path.isfile("Backend/Database/Fake_DB.csv"))

    return result[0], reliability_rating

def retrieve_all_news():
    all_news_list = retrieve_news("Backend/Database/All_DB.csv")
    return all_news_list

def retrieve_true_news():
    true_news_list = retrieve_news("Backend/Database/True_DB.csv")
    return true_news_list

def retrieve_fake_news():
    fake_news_list = retrieve_news("Backend/Database/Fake_DB.csv")
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

url = "https://www.hindustantimes.com/cricket/virat-kohli-ends-century-drought-smashes-maiden-t20i-ton-in-india-vs-afghanistan-asia-cup-super-4-match-101662649555677.html"
news = '''Virat Kohli reached his first international century since November 2019, as he reached the three-figure mark against Afghanistan in Asia Cup 2022. Team India's star batter Virat Kohli ended the wait for an international century, reaching the three-figure mark against Afghanistan in the Asia Cup Super 4 match in Dubai. Kohli reached his hundred in 53 balls, continuing on his impressive run of form since his return to Team India in the continental tournament. Before the century knock, Kohli had scored two fifties in the Asia Cup as well (59* against Hong Kong and 60 against Pakistan). Kohli's last century in international cricket came in November 2019 against Bangladesh; last month, the batter had endured a thousand days without a ton. The century against Afghanistan was Kohli's 71st international hundred, as he equalled Australia's batting great Ricky Ponting. Only Sachin Tendulkar (100 international centuries) stays ahead of the former India captain now.
In the game against Afghanistan, Kohli opened the innings alongside stand-in skipper KL Rahul as Rohit Sharma was given rest in the game. This was the first time Kohli came as an opener in T20Is since March 2021, when he had forged a brilliant 94-run stand with Rohit; it was an even better outing for the former Indian captain this time, as he forged a 119-run stand with Rahul, who also scored a much-needed half-century (62 off 40 deliveries). Kohli began aggressively in his knock, racing to his half-century in 32 deliveries. Following the quick dismissals of Rahul and Suryakumar Yadav (6), the 33-year-old batter readjusted his game alongside Rishabh Pant, resorting to singles and doubles through the middle-overs before upping the ante against Afghanistan pacers. He eventually reached his century in the 19th over of the game with a six against Fareed Ahmed – this was his maiden T20I hundred.
Kohli eventually remained unbeaten on 122 runs off 61 deliveries, smashing 12 fours and six sixes en route to his century knock.'''
result, reliability_rating = validate_news(url, news)

print(result, reliability_rating)

fakeurl = ""
# news is the input given in the frontend for the relevant textArea which is the news content
fakenews = '''Republicans have had seven years to come up with a viable replacement for Obamacare but they failed miserably. After taking a victory lap for gifting the wealthy with a tax break on Wednesday, Donald Trump looked at the cameras and said,  We have essentially repealed Obamacare and we will come up with something that will be much better. Obamacare has been repealed in this bill,  he added. Well, like most things Trump says, that s just not true. But, if the former reality show star could have done that in order to eradicate former President Obama s signature legislation, he would have and without offering an alternative.Senate Majority Leader Mitch McConnell told NPR that  This has not been a very bipartisan year. I hope in the new year, we re going to pivot here and become more cooperative. An Obamacare repeal in 2018 is DOA. Well, we obviously were unable to completely repeal and replace with a 52-48 Senate,  the Kentucky Republican said.  We ll have to take a look at what that looks like with a 51-49 Senate. But I think we ll probably move on to other issues. NPR reports:McConnell hopes to focus instead on stabilizing the insurance marketplaces to keep premiums from skyrocketing in the early months of 2018, a promise he made to moderate Republican Sen. Susan Collins of Maine to get her support for the tax bill.On top of that McConnell broke with House Speaker Paul Ryan, R-Wis., on the approach to paring back spending on programs like Medicaid and food stamps. McConnell told NPR he is  not interested  in using Senate budget rules to allow Republicans to cut entitlements without consultation with Democrats. I think entitlement changes, to be sustained, almost always have to be bipartisan,  McConnell said.  The House may have a different agenda. If our Democratic friends in the Senate want to join us to tackle any kind of entitlement reform. I d be happy to take a look at it. This is coming from Mitch McConnell. He knows Donald Trump is destroying the GOP. It doesn t matter, Sen. McConnell. We still recall him saying that his  number one priority is making sure president Obama s a one-term president. Well, we re hoping that Trump doesn t last a full term. Funny how that works.Photo by Chip Somodevilla/Getty Images'''

fakeresult , fakereliability_rating = validate_news(fakeurl, fakenews)

print(fakeresult)
print(fakereliability_rating) 




# _______________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________

#DILL Version

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
import dill

from os.path import dirname, join
    
def validate_news(url, news):
    

    def process_text(s):
        #Check Punctuation
        nopunc =[char for char in s if char not in string.punctuation]

        # Join the characters  without punctuation
        nopunc =''.join(nopunc)

        #Converting Strings to Lowercase and Removing stopwords
        clean_string = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
        return clean_string 

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

    # sctor_pipeline = join(dirname(__file__), "detector_pipeline.joblib")
    # detector_pipeline = joblib.load(sctor_pipeline)

    sctor_pipeline = join(dirname(__file__), "detector_pipeline.dill")
    if(os.path.getsize(sctor_pipeline) > 0):
        with open(sctor_pipeline, 'rb') as detector_file:         
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

            if(os.path.isfile("Backend/Database/All_DB.csv")):
                df_existing = pd.read_csv("Backend/Database/All_DB.csv")
                df_existing = pd.read_csv("Backend/Database/All_DB.csv")
                alreadyExists = (identifier == df_existing["Identifier"]).any()
            else:
                alreadyExists = False

            # write/append data frame to CSV files
            if(not alreadyExists):    # Check for duplicates
                df.to_csv("Backend/Database/All_DB.csv", mode="a", index=False, header=not os.path.isfile("Backend/Database/All_DB.csv"))

                if(result == "True"):
                    df.to_csv("Backend/Database/True_DB.csv", mode="a", index=False, header=not os.path.isfile("Backend/Database/True_DB.csv"))
                elif(result == "Fake"):
                    df.to_csv("Backend/Database/Fake_DB.csv", mode="a", index=False, header=not os.path.isfile("Backend/Database//Fake_DB.csv"))

            return result, reliability_rating

def retrieve_all_news():
    all_news_list = retrieve_news("Backend/Database/All_DB.csv")
    return all_news_list

def retrieve_true_news():
    true_news_list = retrieve_news("Backend/Database/True_DB.csv")
    return true_news_list

def retrieve_fake_news():
    fake_news_list = retrieve_news("Backend/Database/Fake_DB.csv")
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

# This is a true news 

url = "https://www.hindustantimes.com/cricket/virat-kohli-ends-century-drought-smashes-maiden-t20i-ton-in-india-vs-afghanistan-asia-cup-super-4-match-101662649555677.html"
# news is the input given in the frontend for the relevant textArea which is the news content
news = '''Virat Kohli reached his first international century since November 2019, as he reached the three-figure mark against Afghanistan in Asia Cup 2022. Team India's star batter Virat Kohli ended the wait for an international century, reaching the three-figure mark against Afghanistan in the Asia Cup Super 4 match in Dubai. Kohli reached his hundred in 53 balls, continuing on his impressive run of form since his return to Team India in the continental tournament. Before the century knock, Kohli had scored two fifties in the Asia Cup as well (59* against Hong Kong and 60 against Pakistan). Kohli's last century in international cricket came in November 2019 against Bangladesh; last month, the batter had endured a thousand days without a ton. The century against Afghanistan was Kohli's 71st international hundred, as he equalled Australia's batting great Ricky Ponting. Only Sachin Tendulkar (100 international centuries) stays ahead of the former India captain now.

In the game against Afghanistan, Kohli opened the innings alongside stand-in skipper KL Rahul as Rohit Sharma was given rest in the game. This was the first time Kohli came as an opener in T20Is since March 2021, when he had forged a brilliant 94-run stand with Rohit; it was an even better outing for the former Indian captain this time, as he forged a 119-run stand with Rahul, who also scored a much-needed half-century (62 off 40 deliveries). Kohli began aggressively in his knock, racing to his half-century in 32 deliveries. Following the quick dismissals of Rahul and Suryakumar Yadav (6), the 33-year-old batter readjusted his game alongside Rishabh Pant, resorting to singles and doubles through the middle-overs before upping the ante against Afghanistan pacers. He eventually reached his century in the 19th over of the game with a six against Fareed Ahmed – this was his maiden T20I hundred.

Kohli eventually remained unbeaten on 122 runs off 61 deliveries, smashing 12 fours and six sixes en route to his century knock.'''

result ,reliability_rating = validate_news(url, news)

print(result)
print(reliability_rating)    





# This is a fake news 

fakeurl = ""
# news is the input given in the frontend for the relevant textArea which is the news content
fakenews = '''Republicans have had seven years to come up with a viable replacement for Obamacare but they failed miserably. After taking a victory lap for gifting the wealthy with a tax break on Wednesday, Donald Trump looked at the cameras and said,  We have essentially repealed Obamacare and we will come up with something that will be much better. Obamacare has been repealed in this bill,  he added. Well, like most things Trump says, that s just not true. But, if the former reality show star could have done that in order to eradicate former President Obama s signature legislation, he would have and without offering an alternative.Senate Majority Leader Mitch McConnell told NPR that  This has not been a very bipartisan year. I hope in the new year, we re going to pivot here and become more cooperative. An Obamacare repeal in 2018 is DOA. Well, we obviously were unable to completely repeal and replace with a 52-48 Senate,  the Kentucky Republican said.  We ll have to take a look at what that looks like with a 51-49 Senate. But I think we ll probably move on to other issues. NPR reports:McConnell hopes to focus instead on stabilizing the insurance marketplaces to keep premiums from skyrocketing in the early months of 2018, a promise he made to moderate Republican Sen. Susan Collins of Maine to get her support for the tax bill.On top of that McConnell broke with House Speaker Paul Ryan, R-Wis., on the approach to paring back spending on programs like Medicaid and food stamps. McConnell told NPR he is  not interested  in using Senate budget rules to allow Republicans to cut entitlements without consultation with Democrats. I think entitlement changes, to be sustained, almost always have to be bipartisan,  McConnell said.  The House may have a different agenda. If our Democratic friends in the Senate want to join us to tackle any kind of entitlement reform. I d be happy to take a look at it. This is coming from Mitch McConnell. He knows Donald Trump is destroying the GOP. It doesn t matter, Sen. McConnell. We still recall him saying that his  number one priority is making sure president Obama s a one-term president. Well, we re hoping that Trump doesn t last a full term. Funny how that works.Photo by Chip Somodevilla/Getty Images'''

fakeresult , fakereliability_rating = validate_news(fakeurl, fakenews)

print(fakeresult)
print(fakereliability_rating) 