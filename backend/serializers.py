from django.contrib.auth.models import User
from rest_framework import serializers

from backend.models import Board, List, Card, Comment, Attachment, ActivityLog, Label
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields =['id', 'username','email']

class BoardSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, write_only=True
    )
    members_details = UserSerializer(source='members', many=True, read_only=True)
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Board
        fields = '__all__' 
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['members'] = rep.pop('members_details')
        return rep

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'

class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = '__all__'

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'



