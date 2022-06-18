from django.db import models

# Create your models here.
class Posts(models.Model):
    image = models.ImageField(upload_to = 'posts/',default='IMAGE')
    title =  models.CharField(max_length =30)
    description = models.TextField()
    

    def __str__(self):
        return self.title
