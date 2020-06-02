from django.shortcuts import render
import random
# Create your views here.
def lotto(request):
    result = random.sample(range(1, 46), 6)
    context = {
        'result': result,
    }
    return render(request, 'lotto.html', context)