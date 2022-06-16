from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profile_photo = CloudinaryField('profile_photo')
    bio = models.CharField(max_length=60)
    user = models.OneToOneField(User, related_name = 'profile',on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete('all')
class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=30)
    caption = models.TextField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.name 

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls,id):
        return cls.objects.get(id=id)

    @classmethod
    def search_username(cls,search_term):
        username = cls.objects.filter(name__icontains=search_term)
        return username

class Comment(models.Model):
    content = models.TextField()
    post = models.OneToOneField(Image, related_name='img',on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content