from .models import PostFile
from .models import Comments
from django import forms


class PostForm(forms.ModelForm):

    class Meta:
        model = PostFile
        fields = ('file',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('comment',)




