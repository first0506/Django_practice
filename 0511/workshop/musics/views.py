from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Artist, Music, Comment
from .serializers import ArtistSerializer, ArtistDetailSerializer, MusicSerializer, CommentSerializer, MusicDetailSerializer

# Create your views here.
@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)

@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicDetailSerializer(music)
    return Response(serializer.data)

@api_view(['POST'])
def comments_create(request, music_pk):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=music_pk)
    # return Response(serializer.data)
    return Response({'message':'댓글이 작성됐습니다.'})

@api_view(['PUT', 'DELETE'])
def comment_update_and_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': '성공적으로 수정되었습니다.'})
    else:
        comment.delete()
        return Response({'message': '삭제 완료!'})