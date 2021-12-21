from django.shortcuts import render


# Create your views here.

def index_view(request):
    print(request.GET.get('title'))
    context = {"name": "Vasya", "title": "laalala"}
    return render(request, 'index.html', context)


def create_articles_views(request):
    if request.method == 'GET':
        return render(request, 'article_create.html')
    else:
        context = {
            'title': request.POST.get('title'),
            'content': request.POST.get('content'),
            'author': request.POST.get('author')
        }
        return render(request, 'article_view.html', context)
