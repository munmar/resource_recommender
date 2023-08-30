import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# # Download the NLTK resources (only needed once) -> Replaced by nltk.txt for Heroku
# nltk.download('omw-1.4')
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')


def preprocess_text(text):
  '''
    Preprocesses the input text.

    This function performs the following steps on the input text:
    - Converts the text to lowercase
    - Removes special characters and punctuation using regular expressions
    - Tokenizes the text into individual words
    - Removes stopwords using NLTK's predefined list
    - Lemmatizes the words to their base form using WordNet lemmatizer
    - Joins the preprocessed words back into a sentence
    
    Args:
      text (str): Input text to be preprocessed.

    Returns:
      str: Preprocessed text.
  '''
  text = text.lower()
  
  text = re.sub(r'[^\w\s]', '', text)
  
  words = word_tokenize(text)
  
  stop_words = set(stopwords.words('english'))
  words = [word for word in words if word not in stop_words]
  
  lemmatizer = WordNetLemmatizer()
  words = [lemmatizer.lemmatize(word) for word in words]
  
  processed_text = ' '.join(words)
  
  return processed_text