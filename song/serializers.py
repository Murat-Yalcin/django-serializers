from rest_framework import serializers
from .models import (
    Album, 
    Artist, 
    Lyric, 
    Song,
    )


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
        
class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField(many=True)
    class Meta:
        model = Album
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    album = serializers.StringRelatedField()
    artist = serializers.StringRelatedField()
    class Meta:
        model = Song
        fields = '__all__'


class LyricSerializer(serializers.ModelSerializer):
    song = serializers.StringRelatedField()
    class Meta:
        model = Lyric
        fields = '__all__'


class SongWithLyricsSerializer(serializers.ModelSerializer):
    album = serializers.StringRelatedField()
    artist = serializers.StringRelatedField()
    lyric = LyricSerializer()
    class Meta:
        model = Song
        fields = ['artist', 'album', 'name', 'released', 'lyric']


class AlbumWithSongsSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)
    num_of_songs = serializers.SerializerMethodField()
    artist = serializers.StringRelatedField(many=True)
    class Meta:
        model = Album
        fields = ('name', 'artist', 'num_of_songs', 'released', 'songs')

    def get_num_of_songs(self, obj):
        return Song.objects.filter(album_id=obj.id).count()