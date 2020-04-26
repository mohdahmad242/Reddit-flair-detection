import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from werkzeug.utils import secure_filename
import numpy as np
import pandas as pd

import pickle
import os
cwd = os.getcwd()
pretrained_model = pickle.load(open(cwd + '\\ml_model\\model.pkl','rb'))
tfidf = pickle.load(open(cwd + '\\ml_model\\ngrams_vectorizer.pkl','rb'))
flairs = ['AMA', 'AskIndia', 'Business/Finance', 'Coronavirus', 'Food', 'Non-Political', 'Photography', 'Policy/Economy', 'Politics', 'Scheduled', 'Science/Technology', 'Sports']

# Importing Library Reddit Library
import praw
# Initializing Reddit API
reddit = praw.Reddit(client_id='KhELuATyIFR1aQ',
                     client_secret='gHm5vxbsctlwSE8yqtpLKAdFR7E',
                     user_agent='ahmadkhan242',
                        username='ahmadkhan242', 
                     password='9990800652')


REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    if type(text) == np.nan:
        return np.nan
    text = str(text)
    text = text.lower()
    text = REPLACE_BY_SPACE_RE.sub(' ', text)
    text = BAD_SYMBOLS_RE.sub('', text)
    text = ' '.join(word for word in text.split() if word not in STOPWORDS)
    return text

def data_prep(res_url):
    posts = reddit.submission(url = str(res_url))
    res_data = {}
    res_data["title"] = str(posts.title)
    res_data["title_u"] = str(posts.title)
    res_data["selftext"] = str(posts.selftext)
    
    count = 0
    posts.comments.replace_more(limit=50)
    combined_comments = " "
    for comment in posts.comments:
        combined_comments += " " + comment.body
    res_data["combined_comments"] = str(combined_comments)
    res_data['title'] = clean_text(str(res_data['title']))
    res_data['selftext'] = clean_text(str(res_data['selftext']))
    res_data['combined_comments'] = clean_text(str(res_data['combined_comments']))
    return res_data

def pred(pred_url):
    features = data_prep(pred_url)
    final_features = str(features['title']) + str(features['selftext']) + str(features['combined_comments'])
    data = pd.DataFrame({"content":[final_features]})
    final_feature = tfidf.fit_transform(data.content).toarray()
    res = flairs[int(pretrained_model.predict(final_feature))]
    return {"result" :res, "title": str(features['title_u'])}

