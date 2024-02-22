from django.db import models

# Create your models here.
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
class Board(models.Model):
    CATEGORY_CHOICES = [
        ('free', '자유게시판'),
        ('pc', 'pc 게임'),
        ('moblie', '모바일 게임'),
        ('embed', '임베디드 게임'),
        ('anti', '안티포렌식'),

    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100, unique=False)
    titel = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    board_text = RichTextUploadingField(null = True)
    def __str__(self):
        return self.name
    

class Comment(models.Model):
    lecture = models.ForeignKey(Board, on_delete= models.CASCADE)
    comment = models.CharField(max_length=3000)
    user = models.CharField(max_length=100)
    parent_comment = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.comment
    
class Notice(models.Model):
    name = models.CharField(max_length=100)
    board_text = RichTextUploadingField(null = True)