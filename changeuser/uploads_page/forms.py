from .models import PostFile
from .models import Comments
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = PostFile
        fields = ("file",)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("comment",)
        exclude = 'author',

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    def clean(self):
        self.cleaned_data = super().clean()
        if self.data['user']:
            self.cleaned_data['author_id'] = 38
            # self.cleaned_data['author'] = self.data['user']

        print( self.cleaned_data)
        return self.cleaned_data


class AdminForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = PostFile