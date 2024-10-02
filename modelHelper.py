import pandas as pd
pd.set_option('display.max_columns', None)
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

from sklearn.neighbors import NearestNeighbors

import warnings

class ModelHelper():
    def __init__(self):
        pass

    def make_recommendation(self, Title):
        # Load the dataset
        movies_df = pd.read_csv('cleaned_movies_data.csv')
        
        # Define feature columns for modeling
        feature_cols = ['Release_Date', 'Rating', 'No_of_Persons_Voted', 'Duration', 'Genres']
        
        # Preprocessing pipelines (as before)
        numeric_features = ['Rating', 'No_of_Persons_Voted']
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean')),
            ('scaler', StandardScaler())
        ])
        
        categorical_features = ['Genres']
        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent', missing_values=pd.NA)),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])
        
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)
            ]
        )

        # Prepare the features for modeling
        X = movies_df.loc[:, feature_cols]
        
        preprocessor.fit(X)
        X_preprocessed = preprocessor.transform(X)
        
        # Set k to a fixed number of neighbors (e.g., 5)
        k = 5
        model1 = NearestNeighbors(n_neighbors=k, metric='cosine')
        
        model1.fit(X_preprocessed)

        # Get features for the selected movie
        movie_features = movies_df.loc[movies_df.Title == Title, feature_cols]

        if movie_features.empty:
            return pd.DataFrame()  # Return an empty DataFrame if the title is not found

        movie_features_preprocessed = preprocessor.transform(movie_features)
        
        distances, indices = model1.kneighbors(movie_features_preprocessed)
        
        # Get the recommended movies
        recommended_movies = movies_df.iloc[indices[0]]
        recommended_movies["distances"] = distances[0]
        
        # Sort by distance and return the recommendations
        recommended_movies = recommended_movies.sort_values(by="distances")
        
        return recommended_movies

        preds = model.predict_proba(df)
        return(preds[0][1])
