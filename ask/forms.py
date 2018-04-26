from django import forms
from ask.models import Article

class ArticleAdd(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title", "author", "text", "image")
