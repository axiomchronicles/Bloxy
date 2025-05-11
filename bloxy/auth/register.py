from aquilify.wrappers import Request
from aquilify.responses import JsonResponse

from transutil import crypter

from .. import (
    config,
    schema
)

from . import (
    utils,
    exception
)

class BlogyRegistrationCls:
    
    async def main( self, request: Request ):
        
        try:
        
            if not request.method == "POST":
                raise exception.AuthenticationError( "404: Method Not Allowed (Warning!)", 405 )
            
            requestData = await request.json()
            userSchema = schema.UserRegistrationSchema(requestData)
            
            if not utils.is_valid_email( userSchema.email ):
                raise exception.AuthenticationError( "Invalid Email: %s! please enter a valid email." %(userSchema.email), 403 )
            
            checkPw, errorMsg = utils.is_valid_password( userSchema.password )
            
            if not checkPw:
                raise exception.AuthenticationError( str(errorMsg), 403 )
            
            if ( await config.authcollection.find_one( {"email": userSchema.email} ) ).success:
                raise exception.AuthenticationError( "User email has already registered with us!", 403 )
            
            query = await config.authcollection.insert_one(
                { "id": "$auto", "name": userSchema.name, "email": userSchema.email, "avatar": "None",
                  "password": crypter.hashpw(userSchema.password), "created_at": "$datetime" }
            )
            
            if not query.success:
                raise exception.AuthenticationError( "500: Internal server error! Interact :: Database" )
            
            return JsonResponse( {"res": f"Congratulation! {userSchema.name}, Your account has been successfully created!"} )
            
        except exception.AuthenticationError as ae:
            return JsonResponse( content = {"res": ae.response}, status = ae.code, headers = ae.header )
        

blogyRegistration: BlogyRegistrationCls = BlogyRegistrationCls()