from .models import Post


def add_variable_to_context(request):
    posts = Post.objects.all()
    return {
        'posttitles':  posts
    }
