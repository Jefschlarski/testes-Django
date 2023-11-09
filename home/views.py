
from django.shortcuts import render
context = {
    'texto':'olá',
    'title':'Home',
}
# Create your views here.
def home(request):
    print('home')
    return render(request,'home/index.html', context,)