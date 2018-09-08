from django.db import models

# Create your models here.
class Item(models.Model):
    class Meta:
        ordering = ['-id']
        
    title = models.CharField(
        verbose_name = '件名',
        max_length = 100,
        default = '',
        blank=True
    )

    body = models.TextField(
        verbose_name='本文',
        default='',
        blank=True
    )
    price = models.IntegerField(
        verbose_name='予算',
        default=5000,
        blank=False,
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    def __str__(self):
        return self.title