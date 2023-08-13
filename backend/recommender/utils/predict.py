import pandas as pd
import os
import joblib
from .preprocessing import *
from .data import get_local_data
from django.conf import settings
import sys

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

def recommend_by_class(new_user_input):
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
  top_n_recommendations = 10

  # Find the indices of the top N most similar courses for the new input
  top_indices = new_input_similarity_scores.toarray().argsort()[0][-top_n_recommendations:][::-1]

  # Get the course information for the top N similar courses and add any relevant details
  new_input_recommendations = processed_resources_data.iloc[top_indices].copy()
  new_input_recommendations['user_input'] = new_user_input

  # Reset the index of the recommendations DataFrame
  new_input_recommendations.reset_index(drop=True, inplace=True)

  # Group recommendations by 'class' and select top 3 from each group
  top_n_recommendations_per_class = (
      new_input_recommendations.groupby('class').head(3)
  )

  # Reset the index of the recommendations DataFrame
  top_n_recommendations_per_class.reset_index(drop=True, inplace=True)

  return top_n_recommendations_per_class

def recommend_by_class_more(new_user_input, top_n_per_class=3):
  try:
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
    top_n_recommendations = 15

    # Find the indices of the top N most similar courses for the new input
    top_indices = new_input_similarity_scores.toarray().argsort()[0][-top_n_recommendations:][::-1]

    # Get the course information for the top N similar courses
    new_input_recommendations = processed_resources_data.iloc[top_indices].copy()

    # Reset the index of the recommendations DataFrame
    new_input_recommendations.reset_index(drop=True, inplace=True)

    # Filter recommendations by class and select top N from each class
    recommendations_per_class = {}
    for class_name in new_input_recommendations['class'].unique():
        class_recommendations = new_input_recommendations[new_input_recommendations['class'] == class_name]
        top_n_class_recommendations = class_recommendations.head(top_n_per_class)
        recommendations_per_class[class_name] = top_n_class_recommendations

    # Concatenate recommendations from all classes
    final_recommendations = pd.concat(recommendations_per_class.values())

    # Reset the index of the final recommendations DataFrame
    final_recommendations.reset_index(drop=True, inplace=True)
  except Exception as e:
    print(str(e))
    sys.stdout.flush()
    raise e



  return final_recommendations