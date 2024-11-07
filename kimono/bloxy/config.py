from electrus.asynchronous import Electrus

client: Electrus = Electrus()
database = client["KIMONO"]

# Kimino Collection Server's

basecollection = database["BaseCOllection"]
authcollection = database["AuthCOllection"]
postscollection = database["PostsCollection"]
commentsCollection = database["CommentsCollection"]
newsLetterCollection = database["NewsLetterCollection"]
userReviewCollection = database["UserReviewCollection"]

# Operational Performance