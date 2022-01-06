from django.shortcuts import render, redirect
from .models import Post, PostImage, Video
from django.views.generic import ListView
from django.contrib import messages
from django.core.paginator import Paginator, InvalidPage
from django.http import HttpResponseNotFound


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


def home(request, page=1):
    posts = Post.objects.all()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'posts': posts,
        'num_visits': num_visits
    }

    return render(request, 'blog/home.html', context)


def post(request, id):
    if request.method == 'POST':
        try:
            postpk = Post.objects.filter(
                title=request.POST['postname']).first().pk
            print(postpk)
            return redirect('blog-post', postpk)
        except:
            return redirect('blog-home')
    try:
        post = Post.objects.filter(id=id).first()
        pictures = PostImage.objects.filter(post=post.pk)
    except:
        return HttpResponseNotFound("Sorry, this page doesn't exist ):")

    first = Post.objects.order_by('date_posted').first()
    last = Post.objects.order_by('date_posted').last()
    context = {
        'post': post,
        'last': last,
        'first': first,
        'pictures': pictures
    }
    return render(request, 'blog/post.html', context)


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def music(request):
    videos = Video.objects.all()
    return render(request, 'blog/music.html', {'videos': videos[::-1]}) #reverse the list videos
