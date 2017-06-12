from django import forms

from .models import Topic


class TopicForm(forms.ModelForm):
    """docstring for TopicForm"""
    class Meta(object):
        model = Topic
        fields = ['text']
        labels = {'text': ''}
