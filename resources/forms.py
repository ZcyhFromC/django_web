from django import forms
# ~ from .models import Topic, ResourceNode, Comment

# ~ class TopicForm(forms.ModelForm):
    # ~ class Meta:
        # ~ model = Topic
        # ~ fields = {'text', 'description'}
        # ~ labels = {}

# ~ class ResourceForm(forms.ModelForm):
    # ~ class Meta:
        # ~ model = Resource
        # ~ fields = {'is_group', 'name', 'topic', 'text', 'url', 'parent'}
        # ~ widgets = {'text': forms.Textarea(attrs={'cols': 80})}

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

