from aquilify.core.routing import rule, include

import views

# ROUTER configuration.

# The `ROUTER` list routes URLs to views.
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to ROUTER:  rule('/', views.home, name='home')
# Including another ROUTING
#     1. Import the include() function: from aquilify.core.routing import include, rule
#     2. Add a URL to ROUTER:  rule('/blog', include = include('blog.routing'))

ROUTER = [
    rule( "/", views.homeview ),
    rule( "/review", views.userReview ),
    rule( "/bloxy", include = include("bloxy.routing"), methods = ["GET", "POST"], name = "BLOXY | HOME" ),
]
