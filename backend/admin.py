from django.contrib import admin

from  backend.models import Board,List,Card,Comment,Attachment,ActivityLog,Label

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_at')
    search_fields = ('name', 'owner__username')
    list_filter = ('created_at',)
