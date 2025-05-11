from transutil import syncbit

class UserRegistrationSchema(syncbit.Schema):
    
    name = syncbit.fields.String( strict = True )
    email = syncbit.fields.String( strict = True )
    password = syncbit.fields.String( strict = True )
    
    def __str__(self) -> str:
        return self.name
    
class UserLoginSchema(syncbit.Schema):
    
    email = syncbit.fields.String( strict = True )
    password = syncbit.fields.String( strict = True )
    
    def __str__(self) -> str:
        return self.email
    
class UserComments(syncbit.Schema):
    
    author = syncbit.fields.String( strict = True )
    postId = syncbit.fields.Integer( strict = True )
    userComment = syncbit.fields.String( strict = True )
    authorAvatarUrl = syncbit.fields.String( strict = True )
    
    def __str__(self) -> str:
        return self.userComment
    
class UserNewsLetter(syncbit.Schema):
    
    email = syncbit.fields.String( strict = True )
    
    def __str__(self) -> str:
        return self.email
    
class UserBlogWriting(syncbit.Schema):
    
    title = syncbit.fields.String( strict = True )
    category = syncbit.fields.String( strict = True )
    content = syncbit.fields.String( strict = True )
    tags = syncbit.fields.String( strict = True )
    author = syncbit.fields.String( strict = True )
    
    def __str__(self) -> str:
        return self.author
    
class UserBlogReview(syncbit.Schema):

    name = syncbit.fields.String( strict = True )
    email = syncbit.fields.String( strict = True )
    frequency = syncbit.fields.String( strict = True )
    blogQuality = syncbit.fields.String( strict = True )
    favoriteBlogs = syncbit.fields.String( strict = True )
    writingEase = syncbit.fields.String( strict = True )
    newsSatisfaction = syncbit.fields.String( strict = True )
    overallExperience = syncbit.fields.String( strict = True )
    websiteReview = syncbit.fields.String( strict = True )
    bugsErrors = syncbit.fields.String( strict = True )
    improvements = syncbit.fields.String( strict = True )
    additionalFeedback = syncbit.fields.String( strict = True )

    def __str__(self) -> str:
        return self.name