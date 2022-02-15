# users/serializers.py
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from . import models

class UserCreateSerializer(UserCreateSerializer):
    
    reviews = serializers.HyperlinkedRelatedField(
    view_name='review_detail', many=True, read_only=True)

    # site_name = serializers.SlugRelatedField(
    # queryset=Review.objects.all(), slug_field='name', source='review')

    # comments = serializers.SlugRelatedField(
    # queryset=Review.objects.all(), slug_field='comments', source='reviews')

    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'email', 'username', 'password', 'reviews')