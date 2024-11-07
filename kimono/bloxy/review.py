from aquilify.wrappers import Request
from aquilify.responses import JsonResponse

from . import schema
from . import config

class BloxyUserReview:

    def __init__(self) -> None:
        pass

    async def main( self, request: Request ):

        jsonData = await request.json()
        userReviewSchema = schema.UserBlogReview( jsonData )

        checkEmailQuery = await config.userReviewCollection.find_one(
            { "email": userReviewSchema.email }
        )

        if checkEmailQuery.success:
            return JsonResponse(
                { "error": f"Dear {checkEmailQuery.data["name"]}, your response has already been taken." },
                status = 401
            )
        
        query = await config.userReviewCollection.insert_one(
            { "id": "$auto", "datetime": "$datetime", **userReviewSchema.dump() }
        )

        if not query.success:
            return JsonResponse(
                { "error": "Somthing went wrong! while storing your feedback." },
                status = 401
            )
        
        return JsonResponse(
            { "message": "Thank you for your feedback! We appreciate your time." }
        )

userReview: BloxyUserReview = BloxyUserReview()