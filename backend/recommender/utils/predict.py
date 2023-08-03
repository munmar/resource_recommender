import pandas as pd
import os
import joblib
from .preprocessing import *
# from .recommendation import train_recommendation_model, get_top_n_recommendations
from .data import get_local_data
from django.conf import settings

def recommend(new_user_input):
  base_dir = settings.BASE_DIR

  tfidf_vectorizer_path = os.path.join(base_dir, 'recommender', 'utils', 'models', 'tfidf_vectorizer.joblib')
  tfidf_matrix_path = os.path.join(base_dir, 'recommender', 'utils', 'models', 'tfidf_matrix.joblib')
  processed_resources_data = get_local_data('processed_resources_data.csv')


  loaded_tfidf_vectorizer = joblib.load(tfidf_vectorizer_path)
  loaded_tfidf_matrix = joblib.load(tfidf_matrix_path)

  # new_user_input = "I want to become a data scientist"
  preprocessed_input = preprocess_text(new_user_input)

  # Transform the preprocessed input using the pre-trained TF-IDF vectorizer
  new_input_tfidf = loaded_tfidf_vectorizer.transform([preprocessed_input])

  # Compute the similarity scores between the new input and course descriptions
  new_input_similarity_scores = new_input_tfidf.dot(loaded_tfidf_matrix.T)

  # Define the number of top similar courses to recommend
  top_n_recommendations = 5

  # Find the indices of the top N most similar courses for the new input
  top_indices = new_input_similarity_scores.toarray().argsort()[0][-top_n_recommendations:][::-1]

  # Get the course information for the top N similar courses and add any relevant details
  new_input_recommendations = processed_resources_data.iloc[top_indices].copy()
  new_input_recommendations['user_input'] = new_user_input

  # Reset the index of the recommendations DataFrame
  new_input_recommendations.reset_index(drop=True, inplace=True)

  # print(new_input_recommendations)
  return new_input_recommendations