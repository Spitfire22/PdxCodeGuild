from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.views import generic
from.models import BlogPost, BlogComment

class IndexView(generic.ListView):
    template_name = 'myblog/index.html'
    context_object_name = 'latest_blog_posts'

    def get_queryset(self):
        return BlogPost.objects.order_by('-timestamp')[:5]

def new_user(request):
    group = get_object_or_404(Group, name="Commenter")
    user = User.objects.create_user(username, password, email)
    group.user_list.add(user)


class BlogPostView(generic.DetailView):
    model = BlogPost, BlogComment
    template_name = 'myblog/postview.html'

