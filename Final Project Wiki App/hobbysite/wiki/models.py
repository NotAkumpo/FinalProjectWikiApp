from django.db import models
from datetime import datetime
from django.urls import reverse
from django.conf import settings

# Create your models here.

class ArticleCategory(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Article Category'
        verbose_name_plural = 'Article Categories'


class Article(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey('user_management.Profile', on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    category = models.ForeignKey('ArticleCategory', on_delete = models.SET_NULL, null = True, blank = True)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    header_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
           return reverse('wiki:wiki-detail', args=[self.pk])
    

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

class Comment(models.Model):
    author = models.ForeignKey('user_management.Profile', on_delete = models.SET_NULL, null = True)
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['created_on']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"Comment by {self.author.username} in {self.article.title}"