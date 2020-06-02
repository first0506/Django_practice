from django.shortcuts import render

# Create your views here.
def dinner(request, food, ppl):
    context = {
        'food':food,
        'ppl':ppl
    }
    return render(request, 'dinner.html', context)