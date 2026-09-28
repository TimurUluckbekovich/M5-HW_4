from rest_framework import serializers
from .models import Mixin, Human, Post, Client

class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = "__all__"

MixinSerializer = HumanSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id', 'created')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ('id', 'created')