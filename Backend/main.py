import joblib
import string 
from nltk.corpus import stopwords

#Collecting User Text
user_input = input(str("Please enter the news content you want to verify: "))
print("You entered:  " + str(user_input))


def process_text(s):

    #Check Punctuation
    nopunc =[char for char in s if char not in string.punctuation]

    # Join the characters  without punctuation
    nopunc =''.join(nopunc)

    #Converting Strings to Lowercase and Removing stopwords
    clean_string = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    return clean_string


detector_pipeline = joblib.load("detector_pipeline.joblib")
result = detector_pipeline.predict([['''''']])

print(result)
    