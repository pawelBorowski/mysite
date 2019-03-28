from django.shortcuts import render

posts = [
    {
        "author": "Maciek",
        "title": "First one post",
        "content": "First post",
        "date_publish": "March 24, 2019"
    },
    {
        "author": "Tomek",
        "title": "Sec one post",
        "content": "Sec post",
        "date_publish": "March 25, 2019"
    }
]

def home(request):
    context = {
        "posts": posts
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {"title": "About"})
