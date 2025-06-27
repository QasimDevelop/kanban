from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from celery.result import AsyncResult
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

from .tasks import example_task, example_task_with_error

def simpleTask(request):
    print("This is a simple task")
    result= example_task.delay(10,20)
    print(f"Task ID: {result.id}")
    return render(request, 'backend/simple_task.html', {"result": result, "status": "Task started"})

def taskWithError(request):
    print("This is a task that will raise an error")
    try:
        result = example_task_with_error.delay(10, 20)
        print(f"Task ID: {result.id}")
        return JsonResponse({"task_id": result.id, "status": "Task started"})
    except Exception as e:
        print(f"Error occurred: {e}")
        return JsonResponse({"error": str(e)}, status=500)
def task_result(request, task_id):
    result = AsyncResult(task_id)
    return render(request,"backend/task_result.html", {"result": result})

def websocket_view(request):
    return render(request, 'backend/websocket.html')