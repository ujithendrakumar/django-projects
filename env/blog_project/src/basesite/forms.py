from django import forms
from basesite.models  import Post,Comment



class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control textinputClass'}),
            'text':forms.Textarea(attrs={'class':'form-control editable medium-editor-textarea postconent'}),
        }
class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')
        widgets = {
            'author':forms.TextInput(attrs={'class':'form-control textinputClass'}),
            'text':forms.Textarea(attrs={'class':'form-control editable medium-editor-textarea postconent'}),
        }
