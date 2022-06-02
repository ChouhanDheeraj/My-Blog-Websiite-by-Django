from django.db import models
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    content = models.TextField()
    email = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return 'Message from '+ self.name + '--time--'+ str(self.timestamp)
    


# Create your models here.
