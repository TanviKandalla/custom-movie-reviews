import pandas as pd
import requests

# Load the movies dataset
movies_df = pd.read_csv("Movies.csv", encoding='latin-1')

# Set the TMDB API endpoint and key
endpoint = "https://api.themoviedb.org/3/"
api_key = "YOUR_API_KEY"

# Define a function to extract movie features using the TMDB API
def extract_movie_features(movie_id):
    url = f"{endpoint}movie/{movie_id}?api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        features = {
            "budget": data["budget"],
            "revenue": data["revenue"],
            "popularity": data["popularity"],
            "runtime": data["runtime"],
            "vote_average": data["vote_average"],
            "vote_count": data["vote_count"], #can add upto any number of features needed for our dataset. if u sent we can add based on their data
        }
        return features
    else:
        return {}

# Extract features for each movie in the dataset
movie_features = []
for i, movie in movies_df.iterrows():
    features = extract_movie_features(movie_id=movie["Movie ID"])
    movie_features.append(features)

# Convert the features into a dataframe and merge with the movies dataset
features_df = pd.DataFrame(movie_features)
movies_df = pd.concat([movies_df, features_df], axis=1)

# Save the updated dataset to a CSV file
movies_df.to_csv("Movies_with_features.csv", index=False)
