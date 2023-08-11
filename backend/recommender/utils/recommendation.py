import pandas as pd
import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from .data import get_local_data
from .extract import *
from .preprocessing import *

def train_recommendation_model():
  # Load job data and course data
  job_data = get_local_data('jobs_data.csv')
  resources_data = get_local_data('resources_data.csv')

  # preprocessing the raw data
  job_data['processed_description'] = job_data['description'].apply(preprocess_text)
  resources_data['processed_description'] = resources_data['description'].apply(preprocess_text)
  
  # skill extraction
  job_data_filtered = job_data[job_data['processed_description'].apply(contains_skill)]

  job_data_filtered['skills'] = job_data_filtered['processed_description'].apply(extract_technical_skills)

  # initialise a TF-IDF vectorizer
  tfidf_vectorizer = TfidfVectorizer()

  # fit transform the course descriptions with the TF-IDF vectorizer
  tfidf_matrix = tfidf_vectorizer.fit_transform(resources_data['processed_description'])

  # Convert the skills from job_data into a space-separated string for matching
  job_data_filtered['skills_str'] = job_data_filtered['skills'].apply(lambda skills: ' '.join(skills))

  # Transform the job skills into a TF-IDF matrix
  job_skills_tfidf = tfidf_vectorizer.transform(job_data_filtered['skills_str'])

  # Compute the similarity scores between the job skills and course descriptions
  # The dot product between job_skills_tfidf and tfidf_matrix gives the similarity scores
  similarity_scores = job_skills_tfidf.dot(tfidf_matrix.T)
  
  joblib.dump(similarity_scores, 'models/similarity_scores.joblib')
  joblib.dump(tfidf_vectorizer, 'models/tfidf_vectorizer.joblib')
  joblib.dump(tfidf_matrix, 'models/tfidf_matrix.joblib')
  resources_data.to_csv('../../data/processed_resources_data.csv')
  job_data_filtered.to_csv('../../data/processed_jobs_data.csv')


# print(os.path.join(LOCAL_DATA_PATH, 'jobs_data.csv'))

if __name__ == '__main__':
  train_recommendation_model()