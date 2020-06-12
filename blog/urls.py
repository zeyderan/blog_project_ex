from django.urls import path
from .views import BlogListWiev, BlogDetailView #import view

# www.site.com
urlpatterns = [
    path('', BlogListWiev.as_view(), name='home'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
]
