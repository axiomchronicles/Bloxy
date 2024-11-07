from aquilify.wrappers import Request
from aquilify.responses import JsonResponse

from transutil import crypter

from datetime import datetime

from .. import (
    config,
    schema
)

from . import (
    exception
)

class BlogyLoginCls:
    
    async def main( self, request: Request ):
        
        try:
        
            if not request.method == "POST":
                raise exception.AuthenticationError( "404: Method Not Allowed (Warning!)", 405 )
            
            requestData = await request.json()
            userSchema = schema.UserLoginSchema(requestData)
            
            query = await config.authcollection.find_one( {"email": userSchema.email} )
            
            if not query.success:
                raise exception.AuthenticationError( "User email has not registered with us!", 403 )
            
            if not crypter.checkpw( query.data["password"], userSchema.password ):
                raise exception.AuthenticationError( "Invalid password! please try again.", 403 )
            
            que = await config.authcollection.update_one(
                { "_id": query.data["_id"] },
                { "$set": { "last_login": datetime.now().strftime("%d-%m-%Y %H:%M:%S") } }
            )
            
            if not que.success:
                raise exception.AuthenticationError( "500: Internal server error! Interact :: Database" )
            
            request.session["_id"] = query.data["_id"]
            request.session["Session"] = "Active"
            
            return JsonResponse( {"res": f"Authentication successfull... you may now login!"} )
            
        except exception.AuthenticationError as ae:
            return JsonResponse( content = {"res": ae.response}, status = ae.code, headers = ae.header )
        

blogyLogin: BlogyLoginCls = BlogyLoginCls()