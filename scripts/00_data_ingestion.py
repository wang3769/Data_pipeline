import requests

# Replace this with your actual API key
API_KEY = '1e5d2c3ffeb645cf86d1200c110c0a6f'
#wangtianqi2012@hotmail
#1234567AB

# Define the endpoint and parameters
url = 'https://newsapi.org/v2/top-headlines'
params = {
    'country': 'us',
    'category': 'business',  # options: business, entertainment, general, health, science, sports, technology
    'pageSize': 100,  # number of articles
    'apiKey': API_KEY
}

# Make the request
response = requests.get(url, params=params)

# Check if request was successful
if response.status_code == 200:
    data = response.json() # JSON is a standard for APIs, light and language agnostic
    articles = data.get('articles', []) # get returns default values of a dictionary in this case it specify a []

    # Print article details
    # for i, article in enumerate(articles, 1):
    #     print(f"\nArticle {i}")
    #     print(f"Title: {article['title']}")
    #     print(f"Description: {article['description']}")
    #     print(f"URL: {article['url']}")
    #     print(f"date: {article['publishedAt']}")
else:
    print("Error:", response.status_code, response.text)
    
import os
import sqlite3
import pandas as pd

#folder_path = '../data/raw/'
folder_path = "/opt/airflow/data/"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

os.chdir(folder_path)

#print("Current directory:", os.getcwd())

# Sample: convert articles list to a dataframe first
df = pd.DataFrame(articles)

# Flatten 'source' column (which is a dict)
df['source'] = df['source'].apply(lambda s: s['name'] if isinstance(s, dict) else s)

# Connect to SQLite file (creates if not exist)
conn = sqlite3.connect('news_data.db')

# Save to table called "articles"
df.to_sql('articles', conn, if_exists='append', index=False)

conn.close()