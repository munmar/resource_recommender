import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# # Download the NLTK resources (only needed once)
# nltk.download('omw-1.4')
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# Function for text preprocessing with lemmatization
def preprocess_text(text):
  # Convert text to lowercase
  text = text.lower()
  
  # Remove special characters and punctuation using regular expressions
  text = re.sub(r'[^\w\s]', '', text)
  
  # Tokenize the text into words
  words = word_tokenize(text)
  
  # Remove stopwords
  stop_words = set(stopwords.words('english'))
  words = [word for word in words if word not in stop_words]
  
  # Lemmatization of words
  lemmatizer = WordNetLemmatizer()
  words = [lemmatizer.lemmatize(word) for word in words]
  
  # Join the processed words back into a sentence
  processed_text = ' '.join(words)
  
  return processed_text