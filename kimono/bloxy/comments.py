from aquilify.shortcuts import render
from aquilify.wrappers import Request

from . import (
    utils,
    config,
    schema
)

from datetime import datetime

class BloxyCommentsManager:
    
    async def main( self, request: Request ):
        
        if not request.method == "POST":
            return { "error": "Method Not Allowed!" }
        
        data = await request.json()
        userCommentSchema = schema.UserComments(data)
        
        if not ( await config.commentsCollection.insert_one(
            { "id": "$auto", "author": userCommentSchema.author, "postId": userCommentSchema.postId, "comment": userCommentSchema.userComment,
            "authorAvatarUrl": userCommentSchema.authorAvatarUrl, "commentAt": datetime.now().strftime("%B %d, %Y %H:%M")  }
        ) ).success:
            return { "error": "Internal server error! while interacting with database." }, 401
        
        return {"success": "User Comment Inserted successfully."}
    
    
commentsManager: BloxyCommentsManager = BloxyCommentsManager()