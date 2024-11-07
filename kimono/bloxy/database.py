
# Bloxy Blog Schema Design...

schema = [
    {
        "author": "Jhon Doe",
        "title": "This is a basic title",
        "description": "This is a basic description",
        "url": "http://localhost:8000/bloxy/url...",
        "urlToImage": "http://localhost:8000/bloxy/urlToImage",
        "publishedAt": "2024-06-26 10:46:21",
        "publishedDate": "2024-06-26",
        "content": "This is a content",
        "tag": "tag",
        "viewsCount": 1,
        "readCount": "5 min"
    }
]

commentsSchema = [
    {
        "postId": 1478509612,
        "author": "Jhon Doe",
        "authorAvatarUrl": "",
        "comment": "This is my first comment",
        "commentAt": "2024-06-26 10:46:21"
    }
]

max_read_count_entry = max(schema, key=lambda x: x['viewsCount'])

print(max_read_count_entry)
