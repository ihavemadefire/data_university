from django.db.models import fields
from rest_framework import serializers
from .models import *

class PresenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presenter
        fields = ['name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class SessionSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    presenter = PresenterSerializer(read_only=True, many=True)
    class Meta:
        model = Session
        fields = ['title','subtitle', 'presenter', 'tags', 'video_link', 'date_recorded', 'date_added', 'difficulty', 'slug']

