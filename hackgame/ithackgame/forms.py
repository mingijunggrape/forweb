# forms.py
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Board

class YourModelForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['category', 'titel', 'board_text']

    board_text = forms.CharField(widget=CKEditorUploadingWidget())
