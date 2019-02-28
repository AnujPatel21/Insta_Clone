from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('loginuser/', views.loginuser, name = 'loginuser'),
path('signup/', views.signup, name = 'signup'),
path('signout/', views.signout, name = 'signout'),
path('following/', views.following, name = 'following'),
path('follower/', views.follower, name = 'follower'),
path('follow_Unfollow/<int:num>/', views.follow_Unfollow, name = 'follow_Unfollow'),
path('upload/', views.upload, name = 'upload'),
path('timeline/', views.timeline, name='timeline'),
path('pro_picture/', views.pro_picture, name='pro_picture'),
path('like/<int:num>/',views.like, name = 'like'),
path('comment/<int:num>/',views.comment, name = 'comment'),
path('<str:username>/', views.profile , name = 'profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
