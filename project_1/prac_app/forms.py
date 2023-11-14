from django import forms
from .models import Article, Comment


# 일반 장고폼 @GET
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
    
    
# 장고 모델폼 @POST
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','content')
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)