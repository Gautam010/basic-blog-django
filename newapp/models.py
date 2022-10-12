from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()
    image=models.FileField(upload_to="pic",null=True,blank=True)
    created_on=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title

