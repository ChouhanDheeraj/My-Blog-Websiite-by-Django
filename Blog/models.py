from django.db import models
from django.db.models.fields import AutoField

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    author = models.CharField(max_length=30)
    slug = models.CharField(max_length=130)
    timestamp = models.DateTimeField(blank=True)
    def __str__(self) :
        return 'Message : '+ self.title + '_Serial number-' + str(self.sno)