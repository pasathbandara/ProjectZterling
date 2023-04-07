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

# os.getcwd()
# os.chdir(join(dirname(__file__), "python"))
# import scipy

# import sys


# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.metrics import classification_report
# from sklearn.model_selection import train_test_split
# from sklearn.pipeline import Pipeline

# import sklearn

def validate_news(url, news):
    # import sys
    # scipy_path = "/absosdslute/path/to/scipy"
    # sys.path.append(scipy_path)
    # print (sys.path)
    # import scipy
    # print ("Current working dir : %s" % os.getcwd())
    # os.chdir("C:/Users/MSI/AppData/Local/Programs/Python/Python310/Lib/site-packages")
    # print ("Current working dir : %s" % os.getcwd())

    # import scipy
    # scipy_dir = os.path.dirname(scipy.__file__)
    # current_dir = os.getcwd()
    #
    # if current_dir == scipy_dir:
    #     print("You are in the SciPy source tree.")
    # else:
    #     print("You are not in the SciPy source tree.")


    # # https://stackoverflow.com/questions/11069309/python-import-scipy-leads-to-traceback-referencing-a-deleted-file
    # import sys
    # print (sys.path)


    # https://stackoverflow.com/questions/11069309/python-import-scipy-leads-to-traceback-referencing-a-deleted-file

    directory_to_remove = "/data/data/com.example.sdgptest2/files/chaquopy/AssetFinder/app"
    directory_to_remove2 = "/data/data/com.example.sdgptest2/files/chaquopy/AssetFinder/requirements"
    directory_to_remove3 = "/data/data/com.example.sdgptest2/files/chaquopy/AssetFinder/stdlib-x86"
    directory_to_remove4 = "/data/user/0/com.example.sdgptest2/files/chaquopy/stdlib-common.imy"
    directory_to_remove5 = "/data/user/0/com.example.sdgptest2/files/chaquopy/bootstrap.imy"
    directory_to_remove6 = "/data/user/0/com.example.sdgptest2/files/chaquopy/bootstrap-native/x86"
    # sys.path.remove(directory_to_remove)
    # sys.path.remove(directory_to_remove2)
    # sys.path.remove(directory_to_remove3)
    # sys.path.remove(directory_to_remove4)
    # sys.path.remove(directory_to_remove5)
    # sys.path.remove(directory_to_remove6)

    directory_to_add = "/data/data/com.example.sdgptest2/files/chaquopy/AssetFinder"
    # sys.path.append(directory_to_add)

    # if directory_to_remove in sys.path:
    #     print("removed               : ")
    #     sys.path.remove(directory_to_remove)

    # print(sys.path)

    # path_str = ';'.join(sys.path)
    # sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

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

    # print(dirname(__file__))

    file_path = join(dirname(__file__), "detector_pipeline.dill")
    if(os.path.getsize(file_path) > 0):
        with open(file_path, 'rb') as detector_file:
            # Move one directory back
            # cd ..
            # #
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

def helloworld(a):
    return "HELLLLLLLLLLLOOOOOOOOOOOO        " + a        

# url = "https://www.hindustantimes.com/cricket/virat-kohli-ends-century-drought-smashes-maiden-t20i-ton-in-india-vs-afghanistan-asia-cup-super-4-match-101662649555677.html"
# news = '''Virat Kohli reached his first international century since November 2019, as he reached the three-figure mark against Afghanistan in Asia Cup 2022. Team India's star batter Virat Kohli ended the wait for an international century, reaching the three-figure mark against Afghanistan in the Asia Cup Super 4 match in Dubai. Kohli reached his hundred in 53 balls, continuing on his impressive run of form since his return to Team India in the continental tournament. Before the century knock, Kohli had scored two fifties in the Asia Cup as well (59* against Hong Kong and 60 against Pakistan). Kohli's last century in international cricket came in November 2019 against Bangladesh; last month, the batter had endured a thousand days without a ton. The century against Afghanistan was Kohli's 71st international hundred, as he equalled Australia's batting great Ricky Ponting. Only Sachin Tendulkar (100 international centuries) stays ahead of the former India captain now.
# In the game against Afghanistan, Kohli opened the innings alongside stand-in skipper KL Rahul as Rohit Sharma was given rest in the game. This was the first time Kohli came as an opener in T20Is since March 2021, when he had forged a brilliant 94-run stand with Rohit; it was an even better outing for the former Indian captain this time, as he forged a 119-run stand with Rahul, who also scored a much-needed half-century (62 off 40 deliveries). Kohli began aggressively in his knock, racing to his half-century in 32 deliveries. Following the quick dismissals of Rahul and Suryakumar Yadav (6), the 33-year-old batter readjusted his game alongside Rishabh Pant, resorting to singles and doubles through the middle-overs before upping the ante against Afghanistan pacers. He eventually reached his century in the 19th over of the game with a six against Fareed Ahmed – this was his maiden T20I hundred.
# Kohli eventually remained unbeaten on 122 runs off 61 deliveries, smashing 12 fours and six sixes en route to his century knock.'''
# result, reliability_rating = validate_news(url, news)