from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


# def blog(request):
#     print('Blog')
#     return HttpResponse('Blog App')

def blog(request):
    print('Blog')

    context = {
        'text': 'Olá Blog',
        'title': 'Site de Exemplo'
    }
    return render(
        request,
        'blog/index.html',
        context
    )
