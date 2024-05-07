from datetime import datetime
from django.db import models
from django.urls import reverse

# Create your models here.


class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    peopleRequired = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
           return self.title

    def get_absolute_url(self):
           return reverse('commissions:commission-detail', args=[self.pk])

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Commission'
        verbose_name_plural = 'Comissions'


class Comment(models.Model):
    commission = models.ForeignKey('Commission', on_delete=models.CASCADE, related_name='comments')
    entry = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'