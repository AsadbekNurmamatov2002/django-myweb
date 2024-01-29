from django.urls import path
from .feeds import LatestPostsFeed
from .views import *

app_name="myapp"
urlpatterns = [
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('', Home, name="home"),
    path('post-details/<slug:slug>/<str:year>/<str:month>/<str:day>/',Post_details, name='Post_details'),
    path("post-list/", post_list, name='post_list'),
    # user urls
    path('login/',loginPage, name="login"),
    path('logout/',logoutUser, name="logout"),
    path('register/',registerPage, name="register"),
    path('update-user/',updateUser, name="update-user"),
    path('profile/<str:pk>/',userProfile, name="user-profile"),
]
