from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Gift, Occasion, Recipient

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'name', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class GiftSerializer(serializers.ModelSerializer):
    recipient_name = serializers.CharField(source='recipient.name', read_only=True)
    occasion_name = serializers.CharField(source='occasion.name', read_only=True)

    class Meta:
        model = Gift
        fields = ['id', 'name', 'price', 'currency', 'description', 'occasion', 'datebought', 'status', 'recipient', 'created_at', 'updated_at', 'recipient_name', 'occasion_name']

class OccasionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occasion
        fields = ['id', 'name', 'date']

class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = ['id', 'name', 'relation']

class UserRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user