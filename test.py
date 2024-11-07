from transutil.http.client import ClientSession
import uuid

url = "https://newsapi.org/v2/everything?q=tesla&from=2024-05-26&sortBy=publishedAt&apiKey=a5d8f17cd2094653885aba72c9b982d9"

request = ClientSession()

from datetime import datetime

# Given date in YYYY-MM-DD format
date_str = "2024-06-26"

# Convert to datetime object
date_obj = datetime.strptime(date_str, "%Y-%m-%d")

# Format to desired format
formatted_date = date_obj.strftime("%B %d, %Y")

import math

def calculate_reading_time(content):
    words_per_minute = 200 

    words = content.split()
    num_words = len(words)

    reading_time_minutes = num_words / words_per_minute

    reading_time_seconds = reading_time_minutes * 60

    hours = math.floor(reading_time_seconds / 3600)
    reading_time_seconds %= 3600
    minutes = math.floor(reading_time_seconds / 60)
    seconds = math.ceil(reading_time_seconds % 60)

    parts = []
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours > 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
    if seconds > 0 or (hours == 0 and minutes == 0): 
        parts.append(f"{seconds} second{'s' if seconds > 1 else ''}")

    reading_time = ", ".join(parts)
    return reading_time

import datetime

data = [
    {
        "postId": 6659437385,
        "author": "Pawan Kumar",
        "authorAvatar": "None",
        "title": "This is a test blog post",
        "description": "This is a test blog post,\r\n\r\nIt's form ii\r\n\r\nlol!",
        "urlToImage": "http://localhost:29518/media/img/f00d2fb9-0981-4de4-8437-45c53da5e9a0.jpg",
        "url": "http://localhost:29518/bloxy/single?postId=6659437385&postQueue=null&filter=null&sort=null",
        "publishedAt": "2024-07-20 16:05:38",
        "publishedDate": "July 20, 2024",
        "tag": "null",
        "category": "technology",
        "viewsCount": 5,
        "readCount": "3 seconds",
        "_id": "669b92fad959c71f36df8b1d"
    },
    {
        "postId": 6659437385,
        "author": "Pawan Kumar",
        "authorAvatar": "None",
        "title": "This is a test blog post",
        "description": "This is a test blog post,\r\n\r\nIt's form ii\r\n\r\nlol!",
        "urlToImage": "http://localhost:29518/media/img/f00d2fb9-0981-4de4-8437-45c53da5e9a0.jpg",
        "url": "http://localhost:29518/bloxy/single?postId=6659437385&postQueue=null&filter=null&sort=null",
        "publishedAt": "2024-07-20 16:05:38",
        "publishedDate": "July 19, 2024",
        "tag": "null",
        "category": "technology",
        "viewsCount": 5,
        "readCount": "3 seconds",
        "_id": "669b92fad959c71f36df8b1d"
    }
]

today = datetime.datetime.now().strftime("%B %d, %Y")
todays_data = [post for post in data if post["publishedDate"] == today]
sorted_data = sorted(todays_data, key=lambda x: x["publishedDate"])

