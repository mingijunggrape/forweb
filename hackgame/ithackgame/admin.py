from django.contrib import admin
from .models import Board, Comment, Notice
# Register your models here.

admin.site.register(Board)
admin.site.register(Comment)
admin.site.register(Notice)