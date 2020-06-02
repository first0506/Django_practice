from django.shortcuts import render
import random

# Create your views here.
# def index(request):
#     return render(request, 'index.html')
def lotto(request):
    result = random.sample(range(1, 46), 6)

    # 템플릿 페이지로 결과값 넘겨주기
    context = {
        'result':result,
    }
    return render(request, 'lotto.html', context)