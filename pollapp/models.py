from django.db import models
from django.urls import reverse

# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    total_votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse("poll_detail", args=(self.id,))
    


class Variant(models.Model):
    text = models.CharField(max_length=500)
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE, related_name='variants')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.text}'