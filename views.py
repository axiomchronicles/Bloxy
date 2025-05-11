from aquilify.shortcuts import render, redirect

# Define all your views here.

async def homeview() -> None:
    return await redirect( "/bloxy/dashboard", 302 )

async def userReview(request):
    return await render(request, "review.html")