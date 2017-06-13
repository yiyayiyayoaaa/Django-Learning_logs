from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    """docstring for Toptic"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """docstring for Entry"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        """docstring for Meta"""
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[0:50] + "..."
