from django import forms
from tinymce import TinyMCE
from .models import Post, Comment


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class PostForm(forms.ModelForm):
	title = forms.CharField()
	text = forms.CharField(widget=TinyMCEWidget(attrs={'cols': 60, 'rows': 15}))

	class Meta:
		model = Post
		fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)