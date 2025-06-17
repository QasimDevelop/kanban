from django.contrib.auth.models import User
# Create your views here.
from backend.models import Board, List, Card, Comment, Attachment, ActivityLog, Label
from rest_framework import viewsets
from .serializers import (
    UserSerializer, BoardSerializer, ListSerializer, CardSerializer,
    CommentSerializer, AttachmentSerializer, ActivityLogSerializer, LabelSerializer
)
#from rest_framework import permissions
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class BoardViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows boards to be viewed or edited.
    """
    queryset = Board.objects.all()
    serializer_class = BoardSerializer 
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

class ActivityLogViewSet(viewsets.ModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer

class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer