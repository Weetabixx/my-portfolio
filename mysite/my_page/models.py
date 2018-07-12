from django.db import models
from django.utils import timezone

class Post(models.Model):
    post_type = models.CharField(max_length=30)  #for example 'art' or 'code'
    post_title = models.CharField(max_length=30)
    post_html_text = models.CharField(max_length=5000)
    post_description = models.CharField(max_length=30)
    post_date = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        # On save, update timestamps
        if not self.id:
            self.date = timezone.now()
        return super(Post, self).save(*args, **kwargs)