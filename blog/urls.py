

from django.urls import path, re_path
from . import views


urlpatterns = [
    path ("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("user/<str:username>/", views.user_profile, name="user_profile"),
    re_path(r'^article/(?P<year>[0-9]{4})/$',views.article_by_year, name='article_by_year'),
    path("article/<int:year>/<int:month>/", views.article_detail, name="article_detail"),
    path("post_list/", views.post_list, name="post_list"),
]
