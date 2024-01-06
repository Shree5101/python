#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd


# In[12]:


df=pd.read_csv(r'C:\programme innomatics\movie_data\ratings.csv')
df


# In[5]:


import pandas as pd



# Count the number of unique userId
unique_user_ids = df['userId'].nunique()

print("Number of unique userId:", unique_user_ids)


# In[14]:


df1=pd.read_csv(r'C:\programme innomatics\movie_data\movies.csv')
df1


# In[15]:


df2=pd.read_csv(r'C:\programme innomatics\movie_data\tags.csv')
df2


# In[22]:



matrix_movie_id = 2571 # Replace with the actual movieId

# Filter tags for the movie "Matrix, The (1999)"
matrix_tags = df2[(df2['movieId'] == matrix_movie_id) & 
                      (df2['tag'].isin(['alternate universe', 'karate', 'philosophy', 'post apocalyptic']))]

# Display the selected tags
selected_tags = matrix_tags['tag'].unique()

print("Correct tags submitted by users to 'Matrix, The (1999)':")
print(selected_tags)


# In[40]:



# Assuming 'Terminator 2: Judgment Day (1991)' has a specific title
movie_title = 'Terminator 2: Judgment Day (1991)'

# Find the movieId for the specified title
movie_entry = df1[df1['title'] == movie_title]
movie_id = movie_entry['movieId'].values[0] if not movie_entry.empty else None

# Check if the movieId is found
if movie_id is not None:
    # Filter ratings for the specified movieId
    movie_ratings = df[df['movieId'] == movie_id]

    # Calculate the average user rating
    average_rating = movie_ratings['movieId'].mean()
    print(f"Average user rating for '{movie_title}': {average_rating:.2f}")
else:
    print(f"Movie '{movie_title}' not found in the dataset.")


# In[42]:


import pandas as pd
import matplotlib.pyplot as plt

# Assuming df is your ratings dataset and 'Fight Club (1999)' has a specific title

movie_title = 'Fight Club (1999)'

# Find the movieId for the specified title
movie_entry = df1[df1['title'].str.contains(movie_title, case=False, regex=False)]
movie_id = movie_entry['movieId'].values[0] if not movie_entry.empty else None

# Check if the movieId is found
if movie_id is not None:
    # Filter ratings for the specified movieId
    movie_ratings = df[df['movieId'] == movie_id]

    # Plot the histogram of user ratings
    plt.hist(movie_ratings['movieId'], bins=10, edgecolor='black')
    plt.title(f'Distribution of User Ratings for "{movie_title}"')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.show()
else:
    print(f"Movie '{movie_title}' not found in the dataset.")


# In[65]:


import pandas as pd



# Step 1: Group user ratings based on movieId and apply aggregation operations
grouped_ratings = df.groupby('movieId').agg({'rating': ['count', 'mean']}).reset_index()

# Step 2: Inner join on dataframe created from movies.csv and the grouped df from step 1
merged_df = pd.merge(df1, grouped_ratings, on='movieId', how='inner')

filtered_moviesdf4 = merged_df[merged_df[('rating', 'count')] > 50]

# Display the resulting dataframe
print(filtered_moviesdf4)


# In[64]:


# Assuming filtered_movies is the dataframe you provided
filtered_moviesdf4 = merged_df[merged_df[('rating', 'count')] > 50]

# Display the resulting dataframe
print(filtered_moviesdf4)


# In[ ]:





# In[21]:


import requests
import numpy as np
from bs4 import BeautifulSoup

def scrapper(imdbId):
    id = str(int(imdbId))
    n_zeroes = 7 - len(id)
    new_id = "0"*n_zeroes + id
    URL = f"https://www.imdb.com/title/tt{new_id}/"
    request_header = {
        'Content-Type': 'text/html; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    response = requests.get(URL, headers=request_header)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Update the tag and attribute based on the actual structure of the IMDb page
    imdb_rating = soup.find('div', attrs={'rating-button__aggregate-rating__score':'sc-5931bdee-2 hUPAas'})

    return imdb_rating.text.strip() if imdb_rating else np.nan

# Example usage
imdb_id = "114709"  # Replace with the actual IMDb ID
rating = scrapper(imdb_id)
print(f"IMDb Rating: {rating}")


# In[9]:


import requests
import numpy as np
from bs4 import BeautifulSoup

def scrapper(imdbId):
    id = str(int(imdbId))
    n_zeroes = 7 - len(id)
    new_id = "0" * n_zeroes + id
    URL = f"https://www.imdb.com/title/tt{new_id}/"
    request_header = {
        'Content-Type': 'text/html; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    response = requests.get(URL, headers=request_header)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Update the tag and class based on the actual structure of the IMDb page
    imdb_rating = soup.find('span', attres={'data-testid':'class_'})

    return imdb_rating.text.strip() if imdb_rating else np.nan

# Example usage
imdb_id = "114709"  # Replace with the actual IMDb ID
rating = scrapper(imdb_id)
print(f"IMDb Rating: {rating}")


# In[16]:


df3=pd.read_csv(r'C:\programme innomatics\movie_data\links.csv')
df3


# In[17]:


import pandas as pd

# Assuming df_ratings is the dataset with userId, movieId, ratings
# Assuming df_imdb is the dataset with movieId, imdbId, tmdbId

# Merge the two datasets on the 'movieId' column
merged_df = pd.merge(df, df3, on='movieId')

# Find the movie with the highest IMDB rating
highest_rated_movie = merged_df.loc[merged_df['rating'].idxmax()]

# Get the movieId of the highest-rated movie
highest_rated_movie_id = highest_rated_movie['movieId']

print(f"The movieId of the movie with the highest IMDB rating is: {highest_rated_movie_id}")


# In[18]:


import pandas as pd

# Assuming df_ratings is the dataset with userId, movieId, ratings
# Assuming df_imdb is the dataset with movieId, imdbId, tmdbId
# Assuming df_movies is the dataset with movieId, title, genres

# Merge the datasets on the 'movieId' column
merged_df = pd.merge(df, df3, on='movieId')
merged_df = pd.merge(merged_df, df1, on='movieId')

# Filter for Sci-Fi movies
scifi_movies = merged_df[merged_df['genres'].str.contains('Sci-Fi')]

# Find the Sci-Fi movie with the highest IMDB rating
highest_rated_scifi_movie = scifi_movies.loc[scifi_movies['rating'].idxmax()]

# Get the movieId of the highest-rated Sci-Fi movie
highest_rated_scifi_movie_id = highest_rated_scifi_movie['movieId']

print(f"The movieId of the Sci-Fi movie with the highest IMDB rating is: {highest_rated_scifi_movie_id}")

