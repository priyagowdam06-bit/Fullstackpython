from django.db import models
from django.conf import settings

# Create your models here.
class Books(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    cover=models.ImageField(upload_to='covers/',blank=True,null=True)
    description=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='books'

    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Review(models.Model):
        book=models.ForeignKey('Books', on_delete=models.CASCADE,related_name='review')
        user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        rating=models.IntegerField()
        comment=models.TextField()
        created_at=models.DateTimeField(auto_now_add=True)
        
        def __str__(self):
            return f"{self.user.username}-{self.book.title}"