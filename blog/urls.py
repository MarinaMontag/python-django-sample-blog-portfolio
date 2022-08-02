from django.urls import path
from blog import views


app_name = 'blog'


urlpatterns = [
    path("", views.all_posts, name="all_posts"),
    path("<int:pk>/", views.blog_details, name="blog_details"),
    path("<category>/", views.category_posts, name="category_posts"),
]