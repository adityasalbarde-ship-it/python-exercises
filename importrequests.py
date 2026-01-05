import requests
import json

# Ask user for the type of news
query = input("What type of news are you interested in? ")

# API URL (replace YOUR_API_KEY with your actual NewsAPI key)
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-01-28&sortBy=publishedAt&apiKey=dbe57b028aeb41e285a226a94865f7a7"

# Send GET request
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Check if articles exist
if data.get("articles"):
    print(f"\nTop news about '{query}':\n")
    for article in data["articles"][:5]:  # show top 5 articles
        print(f"📰 Title: {article['title']}")
        print(f"🧑 Author: {article.get('author', 'N/A')}")
        print(f"📝 Description: {article['description']}")
        print(f"🔗 URL: {article['url']}\n")
else:
    print("No news found for that topic.")