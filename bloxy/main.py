from aquilify.shortcuts import render, redirect
from aquilify.wrappers import Request
from aquilify import responses

from . import (
    utils,
    config,
    schema
)

import os
import random
import uuid
import aiofiles

from datetime import datetime

UPLOAD_DIR = "media/img"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

class Bloxy:
    
    async def main(self, request: Request):
        
        if "_id" in request.session:
            user_data = await config.authcollection.find_one({ "_id": request.session["_id"] })
            context = user_data.data if user_data.success else {}
        else:
            context = {}
            
        popQuery = await config.postscollection.fetch_all()
        sortedData = sorted(popQuery.data, key=lambda x: utils.parse_date(x['publishedDate']), reverse=True)
        dataEntries = sortedData[:30] if len(sortedData) > 10 else sortedData
        
        popularPost = max(popQuery.data, key=lambda x: x['viewsCount']) if popQuery.success else None

        today = datetime.now().strftime("%B %d, %Y")
        todays_data = [post for post in popQuery.data if post["publishedDate"] == today]
        sorted_by_date = sorted(todays_data, key=lambda x: x["publishedDate"])
        sorted_by_views = sorted(sorted_by_date, key=lambda x: x["viewsCount"], reverse=True)
        popularPosts = sorted_by_views[:10]
            
        return await render(request, "index.html", {
            
            "user": context, "popularPost": popularPost, "bloxyPosts": dataEntries, "popularPosts": popularPosts
            
            })
        
    async def single( self, request: Request ):
        
        if "_id" in request.session:
            user_data = await config.authcollection.find_one({ "_id": request.session["_id"] })
            context = user_data.data if user_data.success else {}
        else:
            context = {}
        
        postId = request.args.get("postId")
        postQueue = request.args.get("postQueue")
        postCollection = await config.postscollection.fetch_all()
        
        query = await config.postscollection.find_one(
            { "postId": int(postId) }
        )
        
        commentsQuery = await config.commentsCollection.find().filter(
            { "postId": int(postId) }
        ).execute()
        
        viewsUpdateCountQuery = await config.postscollection.update_one(
            { "postId": int(postId) },
            { "$set": { "viewsCount": int(query.data.get("viewsCount") + 1) } }
        )

        today = datetime.now().strftime("%B %d, %Y")
        todaysData = [post for post in postCollection.data if post['publishedDate'] == today]
        filteredData = [post for post in todaysData if post["postId"] != int(postId)]
        otherPosts = sorted(filteredData, key=lambda x: x["publishedDate"])
        
        if not ( query.success, commentsQuery.success, viewsUpdateCountQuery.success ):
            return { "error": "Invalid Post or Invalid Url!" }
        
        return await render( request, "single.html", { "user": context, "bloxyPost": query.data, "comments": commentsQuery.data, "totalComments": len(commentsQuery.data), "postId": int(postId), "otherPosts": otherPosts[:10] } )
        
    async def register( self, request: Request):
        
        if "_id" in request.session:
            return await redirect( "/bloxy/dashboard", 302 )
        
        return await render( request, "register.html" )
    
    async def login( self, request: Request):
        
        if "_id" in request.session:
            return await redirect( "/bloxy/dashboard", 302 )
        
        return await render( request, "login.html" )
    
    async def search(self, request: Request):
        
        query = request.args.get('query', '')
        postCollection = await config.postscollection.fetch_all()
        
        results = [post for post in postCollection.data if query.lower() in post['title'].lower()]
        return responses.JsonResponse({"results": results})
    
    async def newsLetter( self, request: Request ):
        
        req = await request.json()
        newsLetterSchema = schema.UserNewsLetter( req )
        
        if ( await config.newsLetterCollection.find_one(
            { "email": newsLetterSchema.email }
        ) ).success:
            return { "message": f"Account {newsLetterSchema.email} already registered for our NewsLetter." }, 403
        
        query = await config.newsLetterCollection.insert_one(
            { "id": "$auto", "email": newsLetterSchema.email, "datetime": "$datetime" }
        )
        
        if not query.success:
            return { "message": "Internal server error! while delting database." }, 401
        
        return { "message": "User News Letter Suscribe successfully." }, 200
    
    async def writer( self, request: Request ):

        if not "_id" in request.session:
            return await redirect( "/bloxy/login", 302 )
        
        if "_id" in request.session:
            user_data = await config.authcollection.find_one({ "_id": request.session["_id"] })
            context = user_data.data if user_data.success else {}
        else:
            context = {}
        
        return await render( request, "writer.html", context = { "user": context } )

    async def create_blog_post( self, request: Request ):

        if not "_id" in request.session:
            return await redirect( "/bloxy/login", 302 )
        
        userQuery = await config.authcollection.find_one(
            { "_id": request.session['_id'] }
        )

        if not userQuery.success:
            return await redirect( "/bloxy/login", 302 )
        
        formData = await request.form()
        
        ( title, category, content, tags, author, image ) = (
            formData.get("title"), formData.get("category"),
            formData.get("content"), formData.get("tags"), 
            formData.get("author"),  formData.get("image")
        )
        
        if not all([title, category, content, author]):
            return responses.JsonResponse({"message": "Missing required fields."}, status=400)
        
        imageFilename = None
        if image:
            imageId = str(uuid.uuid4())
            _, image_extension = os.path.splitext(image.filename)
            imageFilename = os.path.join(UPLOAD_DIR, f"{imageId}{image_extension}")
            async with aiofiles.open(imageFilename, "wb") as buffer:
                await buffer.write(await image.read())
                
        postID = random.randint(1000000000, 9999999999)
        
        post_data = {
            "postId": postID,
            "author": author,
            "authorAvatar": userQuery.data["avatar"],
            "title": title,
            "description": str(content),
            "urlToImage": f"{request.url.scheme}://{request.host}/{imageFilename}" if imageFilename else None,
            "url": f"{request.url.scheme}://{request.host}/bloxy/single?postId={postID}&postQueue=null&filter=null&sort=null",
            "publishedAt": "$datetime",
            "publishedDate": datetime.now().strftime("%B %d, %Y"),
            "tags": tags.split(" "),
            "category": category,
            "viewsCount": 0,
            "readCount": str(utils.calculate_reading_time(str(content)))
        }
        
        dbQuery = await config.postscollection.insert_one(post_data)
        
        if not dbQuery.success:
            return responses.JsonResponse(
                { "message": "Internal server error! while inetercting with database."},
                500
            )

        return responses.JsonResponse({"message": "Blog posted successfully!"}, status=200)
    
    
bloxy: Bloxy = Bloxy() 