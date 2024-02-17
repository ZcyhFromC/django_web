from django import forms
from .models import ResourceNode


class ResourceNodeForm(forms.ModelForm):
    class Meta:
        model = ResourceNode
        fields = {'name',  'text',  'parent', 'tags', 'link'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

# ~ class GroupForm(forms.ModelForm):
    # ~ class Meta:
        # ~ model = Resource
        # ~ fields = {'is_group', 'name', 'topic', 'text', 'resources'}
        # ~ widgets = {'text': forms.Textarea(attrs={'cols': 80})}

# ~ class ResourceForm(forms.ModelForm):
    # ~ class Meta:
        # ~ model = Resource
        # ~ fields = {'parent', 'is_group', 'name', 'topic', 'text', 'user', 'url', 'resources'}

# ~ class CommentForm(forms.ModelForm):
    # ~ class Meta:
        # ~ model = Comment
        # ~ fields = {'text'}
        # ~ widgets = {'text': forms.Textarea(attrs={'cols': 80})}

