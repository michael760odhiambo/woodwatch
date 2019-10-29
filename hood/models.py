from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime



class Neighbourhood(models.Model):
    hood = models.CharField(max_length=40)
    
    def __str__(self):
        return self.hood

    def save_hood(self):
        self.save()

    @classmethod
    def delete_hood(cls, hood):
        cls.objects.filter(hood=hood).delete()

class Notifications(models.Model):
    title = models.CharField(max_length=40)
    message = HTMLField() 
    priority = models.CharField(max_length=200) 
    author = models.CharField(User,max_length=30)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

class Services(models.Model):
    healthservices = models.CharField(max_length=40)
    mamamboga = models.CharField(max_length=40)
    otherservices = models.CharField(max_length=40)

    def __str__(self):
        return self.healthservices

    def save_services(self):
        self.save()

    @classmethod
    def delete_services(cls, Services):
        self.delete()

class Business(models.Model):
   logo = models.ImageField(upload_to='media')
   description = HTMLField()
   owner = models.CharField(max_length=40)
   hood = models.CharField(max_length=40)
   name = models.CharField(max_length=30)
   email = models.EmailField()
   address = models.CharField(max_length=40)
   contact = models.IntegerField()

   def __str__(self):
       return self.name

# class Authorities(models.Model):
#     hood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
#     name =models.CharField(max_length=100)
#     email = models.EmailField()
#     contact = models.IntegerField()
#     address =models.CharField(max_length=100)

#     def __str__(self):
#         return self.name       

# class Profile(models.Model):
#     avatar = models.ImageField(upload_to='media')
#     description = HTMLField()
#     hood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
#     username = models.ForeignKey(User,on_delete=models.CASCADE)
#     name =models.CharField(max_length=100)
#     email = models.EmailField()
#     #pub_date = models.DateField()

#     def __str__(self):
#         return self.name

# class Post(models.Model):
#     title = models.CharField(max_length=150)
#     image = models.ImageField(upload_to='media')
#     post = HTMLField()
#     username = models.ForeignKey(User,on_delete=models.CASCADE)
#     hood= models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
#     post_date = models.DateTimeField(auto_now_add=True)
#     avatar = models.ImageField(upload_to='media')

#     def __str__(self):
#         return self.title

#     @classmethod
#     def search_blogpost(cls,search_term):
#         blogs = cls.objects.filter(Q(username__username=search_term) | Q(neighbourhood__neighbourhood=search_term) | Q(title__icontains=search_term))
#         return blogs    

# class Comment(models.Model):
#     comment = models.CharField(max_length=300)
#     username = models.ForeignKey(User,on_delete=models.CASCADE)
#     post = models.ForeignKey(Post,on_delete=models.CASCADE)

# class Hoods(models.Model):
#     name = models.CharField(max_length=40)
#     location = models.CharField(max_length=40)
#     address = models.IntegerField()
#     city = models.CharField(max_length=30)
#     #pic = models.ImageField(upload_to='media')
#     def __str__(self):
#         return self.name

#     def save_name(self):
#         self.save()

# class Joinhood(models.Model):
#     your_name = models.CharField(max_length=30)
#     phone_number = models.IntegerField()
#     date_of_birth = models.IntegerField()
#     your_estate = models.CharField(max_length=30)

#     def __str__(self):
#         return self.your_name

#     def save_your_name(self):
#         self.save()

# # Create your models here.
