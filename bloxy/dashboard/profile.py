from aquilify.wrappers import Request
from aquilify.responses import JsonResponse
from aquilify import shortcuts

from .. import (
    config
)

class UserProfile:
    
    def __init__(self) -> None:
        pass
    
    async def userMainProfile(self, request: Request):
        
        if not "_id" in request.session:
            return await shortcuts.redirect("/bloxy/login", 302)
        
        if request.method == "GET":
            userSessionId = request.session["_id"]
            
            userQuery = await config.authcollection.find_one(
                {"_id": str(userSessionId)},
                projection = ["name", "email", "avatar", "last_login"]
            )
            if not userQuery.success:
                return JsonResponse({ "error": "User Not Found or Session Breach." }, 403)
            
            return await shortcuts.render(request, "profile.html", {"userProfile": userQuery.data}) 
        
profile = UserProfile()