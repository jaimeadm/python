from django.shortcuts import render
# from django.http import HttpResponse


def home(request):
    print('Home')

    context = {
        'text': 'Olá Home',
        'title': 'Site de Exemplo'
    }

    return render(
        request,
        'home/index.html',
        context
    )


# def exemplo(request):
#     print('Exemplo')
#     return HttpResponse('Exemplo App')

def exemplo(request):
    print('Exemplo')

    context = {
        'text': 'Olá Exemplo',
        'title': 'Site de Exemplo'
    }
    return render(
        request,
        'home/exemplo.html',
        context
    )
