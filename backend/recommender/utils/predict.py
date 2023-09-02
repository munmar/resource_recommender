import pandas as pd
import os
import joblib
from .preprocessing import *
from .data import get_local_data
from django.conf import settings
import sys
from sklearn.metrics.pairwise import cosine_similarity

def recommend_by_class(new_user_input, top_n_per_class=3, top_n_recommendations = 15):
  '''
    Generates class-specific recommendations based on user input.

    This function takes user input, preprocesses it, and computes the similarity scores
    between the input and course descriptions using a pre-trained TF-IDF vectorizer and matrix.
    It then filters and selects the top N most similar courses for each class and concatenates
    the recommendations from all classes to provide final recommendations.

    Args:
      new_user_input (str): User input describing their preferences.
      top_n_per_class (int, optional): Number of top recommendations to select per class. Defaults to 3.
      top_n_recommendations (int, optional): Total number of final recommendations. Defaults to 15.

    Returns:
      pandas.DataFrame: DataFrame containing class-specific course recommendations.
  '''
  base_dir = settings.BASE_DIR

  tfidf_vectorizer_path = os.path.join(base_dir, 'recommender', 'utils', 'models', 'tfidf_vectorizer.joblib')
  tfidf_matrix_path = os.path.join(base_dir, 'recommender', 'utils', 'models', 'tfidf_matrix.joblib')
  processed_resources_data = get_local_data('processed_resources_data.csv')


  loaded_tfidf_vectorizer = joblib.load(tfidf_vectorizer_path)
  loaded_tfidf_matrix = joblib.load(tfidf_matrix_path)

  preprocessed_input = preprocess_text(new_user_input)

  # transform input with pre-trained TF-IDF vectorizer
  new_input_tfidf = loaded_tfidf_vectorizer.transform([preprocessed_input])

  # compute the similarity scores between the new input and course descriptions
  new_cosine_similarity_scores = cosine_similarity(new_input_tfidf, loaded_tfidf_matrix)

  # get indices of top N most similar courses for new input
  top_indices = new_cosine_similarity_scores.toarray().argsort()[0][-top_n_recommendations:][::-1]

  # get course information for the top N similar courses
  new_input_recommendations = processed_resources_data.iloc[top_indices].copy()
  new_input_recommendations.reset_index(drop=True, inplace=True)

  # filter top N recommendations per class
  recommendations_per_class = {}
  for class_name in new_input_recommendations['class'].unique():
      class_recommendations = new_input_recommendations[new_input_recommendations['class'] == class_name]
      top_n_class_recommendations = class_recommendations.head(top_n_per_class)
      recommendations_per_class[class_name] = top_n_class_recommendations

  # concatenate recommendations from all classes
  final_recommendations = pd.concat(recommendations_per_class.values())
  final_recommendations.reset_index(drop=True, inplace=True)
  return final_recommendations