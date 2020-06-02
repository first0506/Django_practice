from django.shortcuts import render

# Create your views here.
def ping(request):
    return render(request, 'articles/ping.html')

def pong(request):
    data = request.GET.get('data')
    context = {
        'data' : data
    }
    return render(request, 'articles/pong.html', context)