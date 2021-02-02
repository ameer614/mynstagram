from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete = models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(upload_to='posts')
    

class Like(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete = models.CASCADE,related_name='user_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='post_like')

    
    class Meta:
        unique_together = ['user','post']

class Comment(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete = models.CASCADE,related_name='user_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='post_comment')
    comment= models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)