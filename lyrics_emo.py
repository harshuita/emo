"""from transformers import pipeline
import pandas as pd
import string"""
import nltk
nltk.download('stopwords')
nltk.download('punkt')
"""from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
df=pd.read_csv('lyrics_10k.csv')
def clean_text(text, max_length=578):
    cleaned_text = ' '.join(text.split())
    cleaned_text = cleaned_text.lower()
    cleaned_text = cleaned_text.translate(str.maketrans("", "", string.punctuation))
    cleaned_text = ''.join([i for i in cleaned_text if not i.isdigit()])
    cleaned_text = ''.join([i for i in cleaned_text if i.isalpha() or i.isspace()])
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(cleaned_text)
    cleaned_text = ' '.join([word for word in word_tokens if word.lower() not in stop_words])
    
    padded_text = cleaned_text.ljust(max_length)
    
    return padded_text
cleaned_lyrics = df.apply(clean_text)"""