from django.contrib import admin

from  backend.models import Board,List,Card,Comment,Attachment,ActivityLog,Label

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_at')
    search_fields = ('name', 'owner__username')
    list_filter = ('created_at',)

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'board', 'created_at', 'position')
    search_fields = ('name', 'board__name')
    list_filter = ('created_at', 'board')
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'list', 'position', 'created_at', 'assigned_to')
    search_fields = ('title', 'list__name', 'assigned_to__username')
    list_filter = ('created_at', 'list', 'assigned_to')