from  django.db import  models
from django.contrib.auth.models import User

class Board(models.Model):
    name=models.CharField(max_length=25)
    description=models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_boards')
    members=models.ManyToManyField(User, related_name='boards', blank=True)

    def __str__(self):
        return self.name        

class List(models.Model):
    name=models.CharField(max_length=20)
    board=models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')
    created_at=models.DateTimeField(auto_now_add=True)
    position=models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']
    def __str__(self):
        return self.name

class Card(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='cards')
    position = models.PositiveIntegerField() # To maintain the order of cards within a list
    # For user assignment (Advanced Feature)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='assigned_cards')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['position'] 

    def __str__(self):
        return self.title

class Comment(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} on {self.card.title}" 

class Attachment(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for {self.card.title} - {self.file.name}"

class ActivityLog(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='activity_logs')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activity_logs')
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.action} on {self.card.title} at {self.timestamp}"
    
class Label(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)  # e.g., 'red', 'blue', etc.
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='labels')

    def __str__(self):
        return f"{self.name} ({self.color})"

