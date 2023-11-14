from django import forms
from .models import Article


# 일반 장고폼 @GET
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
    
    
# 장고 모델폼 @POST
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'