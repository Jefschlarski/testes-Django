
from django.shortcuts import render


blog_context = {
    'texto':'Acessando o blog',
    'title':'Blog',
}

exemplo_context = {
    'texto':'esse é um exemplo',
    'title':'Exemplo',
}

# Create your views here.
def blog(request):
    print('blog')
    return render(request, 'blog/index.html', blog_context)

def example(request):
    print('example')
    return render(request, 'blog/exemplo.html' , exemplo_context)