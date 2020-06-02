from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Music
from .serializers import MusicSerializer

# Create your views here.
@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()    # queryset (리스트)
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)