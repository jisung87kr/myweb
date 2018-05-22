from django.db import models
from django.utils import timezone

# Create your models here.
class Cate(models.Model):
    cate = models.CharField(max_length = 200)

    def __str__(self):
        return self.cate

class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    cate = models.ForeignKey(Cate, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    upload_file = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.title
