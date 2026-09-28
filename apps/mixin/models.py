from django.db import models

class Mixin(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Human(Mixin):
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['id']
        abstract = True
        
# DRY = Dont repeat yorself

class Post(Mixin):
    # title = models.CharField(max_length=120)
    # description = models.TextField()
    category = models.CharField(max_length=120)
    views_count = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    # created = models.DateTimeField(auto_now_add=True)
    
class Client(Human):
    # full_name = models.CharField(max_length=120)
    # notes = models.TextField()
    # email = models.EmailField(blank=True, null=True)
    # phone = models.CharField(max_length=20)
    # address = models.CharField(max_length=255, blank=True, null=True)
    # is_active = models.BooleanField(default=True)
    # created = models.DateTimeField(auto_now_add=True)
    pass