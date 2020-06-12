from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post

# Create your views here.
# sınıf bazlı view listview ı extend eder
class BlogListWiev(ListView):
    # gönderilecek model
    model = Post

    # gönderilecek template
    template_name = 'home.html'

    # model takma ismi html içerisinde kullanılacak isim
    context_object_name = 'blog_list'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    # template e gönderilecek veririn ismi
    context_object_name = 'post_detail' 