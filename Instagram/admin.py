from django.contrib import admin

from . models import UserFollower
from . models import post
from . models import Profile_Picture
from . models import Comments



admin.site.register(UserFollower)
admin.site.register(post)
admin.site.register(Profile_Picture)
admin.site.register(Comments)
