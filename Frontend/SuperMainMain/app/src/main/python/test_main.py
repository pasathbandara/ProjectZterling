import unittest
import main
import string
import nltk
from nltk.corpus import stopwords

def process_text(s):
    #Check Punctuation
    nltk.download('stopwords')
    nopunc =[char for char in s if char not in string.punctuation]

    # Join the characters  without punctuation
    nopunc =''.join(nopunc)

    #Converting Strings to Lowercase and Removing stopwords
    clean_string = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    return clean_string 

class TestMain(unittest.TestCase):

    def test_validate_news_true(self):
        # Testing for true news
        url = "https://www.hindustantimes.com/cricket/virat-kohli-ends-century-drought-smashes-maiden-t20i-ton-in-india-vs-afghanistan-asia-cup-super-4-match-101662649555677.html"
        news = '''Virat Kohli reached his first international century since November 2019, as he reached the three-figure mark against Afghanistan in Asia Cup 2022. Team India's star batter Virat Kohli ended the wait for an international century, reaching the three-figure mark against Afghanistan in the Asia Cup Super 4 match in Dubai. Kohli reached his hundred in 53 balls, continuing on his impressive run of form since his return to Team India in the continental tournament. Before the century knock, Kohli had scored two fifties in the Asia Cup as well (59* against Hong Kong and 60 against Pakistan). Kohli's last century in international cricket came in November 2019 against Bangladesh; last month, the batter had endured a thousand days without a ton. The century against Afghanistan was Kohli's 71st international hundred, as he equalled Australia's batting great Ricky Ponting. Only Sachin Tendulkar (100 international centuries) stays ahead of the former India captain now.
        In the game against Afghanistan, Kohli opened the innings alongside stand-in skipper KL Rahul as Rohit Sharma was given rest in the game. This was the first time Kohli came as an opener in T20Is since March 2021, when he had forged a brilliant 94-run stand with Rohit; it was an even better outing for the former Indian captain this time, as he forged a 119-run stand with Rahul, who also scored a much-needed half-century (62 off 40 deliveries). Kohli began aggressively in his knock, racing to his half-century in 32 deliveries. Following the quick dismissals of Rahul and Suryakumar Yadav (6), the 33-year-old batter readjusted his game alongside Rishabh Pant, resorting to singles and doubles through the middle-overs before upping the ante against Afghanistan pacers. He eventually reached his century in the 19th over of the game with a six against Fareed Ahmed – this was his maiden T20I hundred.
        Kohli eventually remained unbeaten on 122 runs off 61 deliveries, smashing 12 fours and six sixes en route to his century knock.'''
        result = main.validate_news(url, news)
        assert result[0].lower() == "true"

    def test_validate_news_fake(self):
        # Testing for fake news
        url = ""
        news = '''Donald Trump just couldn t wish all Americans a Happy New Year and leave it at that. Instead, he had to give a shout out to his enemies, haters and  the very dishonest fake news media.  The former reality show star had just one job to do and he couldn t do it. As our Country rapidly grows stronger and smarter, I want to wish all of my friends, supporters, enemies, haters, and even the very dishonest Fake News Media, a Happy and Healthy New Year,  President Angry Pants tweeted.  2018 will be a great year for America! As our Country rapidly grows stronger and smarter, I want to wish all of my friends, supporters, enemies, haters, and even the very dishonest Fake News Media, a Happy and Healthy New Year. 2018 will be a great year for America!  Donald J. Trump (@realDonaldTrump) December 31, 2017Trump s tweet went down about as welll as you d expect.What kind of president sends a New Year s greeting like this despicable, petty, infantile gibberish? Only Trump! His lack of decency won t even allow him to rise above the gutter long enough to wish the American citizens a happy new year!  Bishop Talbert Swan (@TalbertSwan) December 31, 2017no one likes you  Calvin (@calvinstowell) December 31, 2017Your impeachment would make 2018 a great year for America, but I ll also accept regaining control of Congress.  Miranda Yaver (@mirandayaver) December 31, 2017Do you hear yourself talk? When you have to include that many people that hate you you have to wonder? Why do the they all hate me?  Alan Sandoval (@AlanSandoval13) December 31, 2017Who uses the word Haters in a New Years wish??  Marlene (@marlene399) December 31, 2017You can t just say happy new year?  Koren pollitt (@Korencarpenter) December 31, 2017Here s Trump s New Year s Eve tweet from 2016.Happy New Year to all, including to my many enemies and those who have fought me and lost so badly they just don t know what to do. Love!  Donald J. Trump (@realDonaldTrump) December 31, 2016This is nothing new for Trump. He s been doing this for years.Trump has directed messages to his  enemies  and  haters  for New Year s, Easter, Thanksgiving, and the anniversary of 9/11. pic.twitter.com/4FPAe2KypA  Daniel Dale (@ddale8) December 31, 2017Trump s holiday tweets are clearly not presidential.How long did he work at Hallmark before becoming President?  Steven Goodine (@SGoodine) December 31, 2017He s always been like this . . . the only difference is that in the last few years, his filter has been breaking down.  Roy Schulze (@thbthttt) December 31, 2017Who, apart from a teenager uses the term haters?  Wendy (@WendyWhistles) December 31, 2017he s a fucking 5 year old  Who Knows (@rainyday80) December 31, 2017So, to all the people who voted for this a hole thinking he would change once he got into power, you were wrong! 70-year-old men don t change and now he s a year older.Photo by Andrew Burton/Getty Images.'''
        result = main.validate_news(url, news)
        assert result[0].lower() == "fake"

    # def test_retrieve(self):

    ## ------------------------------------- TO TEST THE RETRIEVE FUNCTION -------------------------------------

    # news_list = retrieve_all_news()
    # print(news_list)
            

if __name__ == '__main__':
    unittest.main()