from django.db import models

class Blog(models.Model):
    # title
    title = models.CharField(max_length=255)
    # pub_date: publication date (of the post)
    pub_date = models.DateTimeField()
    # body: actual text, the blog post
    body = models.TextField()
    # image: image connected to this blog post
    image = models.ImageField(upload_to='images/')
