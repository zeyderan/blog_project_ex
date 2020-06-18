from django.urls import path
from .views import BlogListWiev, BlogDetailView,BlogCreateView#import view

# www.site.com
urlpatterns = [
    path('', BlogListWiev.as_view(), name='home'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
    path('post/new/',BlogCreateView.as_view(),name='post_new'),
]
