from django import forms

from mainblog.models import Post


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(max_length=60)
    text = forms.CharField(max_length=255)

    class Meta:
        model = Post
        fields = ('title', 'text')
        template_name = 'create.html'


class PostUpdateForm(forms.ModelForm):
    title = forms.CharField(max_length=60)
    text = forms.CharField(max_length=255)

    class Meta:
        model = Post
        fields = ('title', 'text')
        template_name = 'update.html'
