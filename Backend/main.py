import joblib
import string 
from nltk.corpus import stopwords

def process_text(s):

    #check puctuation
    nopunc =[char for char in s if char not in string.punctuation]

    # join the characters  without punctuation
    nopunc =''.join(nopunc)

    