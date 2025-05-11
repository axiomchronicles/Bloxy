from aquilify.core.schematic.routing import rule

from . import main
from . import review
from . import comments
from .auth import (
    register,
    login
)
from .dashboard import (
    profile
)

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
    rule( "/register", main.bloxy.register ),
    rule( "/dashboard", main.bloxy.main ),
    rule( "/single", main.bloxy.single ),
    rule( "/login", main.bloxy.login ),
    rule( "/writer", main.bloxy.writer ),
    rule( "/user/dashboard", profile.profile.userMainProfile, methods = ["GET"] ),
    rule( "/api/search", main.bloxy.search ),
    rule( "/api/newsletter", main.bloxy.newsLetter, methods = ["POST"] ),
    rule( "/api/writer", main.bloxy.create_blog_post, methods = ["POST"] ),
    rule( "/api/register", register.blogyRegistration.main, methods = ["POST"] ),
    rule( "/api/comments", comments.commentsManager.main, methods = ["POST"] ),
    rule( "/api/login", login.blogyLogin.main, methods = ["POST"] ),
    rule( "/api/review", review.userReview.main, methods = ["POST"] ),
]
