from rest_framework import serializers
from .models import Artist, Music, Comment

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'title']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']

class ArtistDetailSerializer(serializers.ModelSerializer):
    musics = MusicSerializer(source='music_set', many=True)
    musics_count = serializers.IntegerField(source='music_set.count')

    class Meta:
        model = Artist
        fields = ['id', 'name', 'musics', 'musics_count']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'music_id']

class MusicDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(source='comment_set', many=True)
    class Meta:
        model = Music
        fields = ['id', 'title', 'comments']