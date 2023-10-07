from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    address = models.CharField(max_length=255,default="")

class Excerpt(models.Model):
    user_excerpt = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userexcerpt")
    excerpt_date = models.CharField(max_length=64)
    excerpt_text = models.CharField(max_length=255)
    author = models.CharField(max_length=64)
    book = models.CharField(max_length=64)
    genre = models.CharField(max_length=64)
    likes = models.ManyToManyField("User", related_name="likes")

    def __str__(self):
        return f"{self.author}, {self.book} (by {self.user_excerpt}) "
    
    def serialize(self):
        return {
            "id": self.id,
            "text": self.excerpt_text,
            "author": self.author,
            "book": self.book,
            "nbr_likes": self.likes.all().count(),
        }
        
class TopBook(models.Model):
    user_topbook = models.ManyToManyField("User", related_name="usertopbook")
    title_topbook =models.CharField(max_length=64)
    author_topbook =models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title_topbook}, {self.author_topbook}  "

    def serialize(self):
        return {
            "id": self.id,
            "author": self.author_topbook,
            "title": self.title_topbook,
            
        }

class Reward(models.Model):
    user_reward = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userreward")
    reward_date = models.CharField(max_length=64)
    reward_book = models.CharField(max_length=64)
    reward_author =  models.CharField(max_length=64)
    reward_sent = models.BooleanField(default=False) 
    ship_track =  models.CharField(max_length=64,default="no shipping")
    def __str__(self):
        return f"winner : {self.user_reward} "
        
    def serialize(self):
        return {
            "id": self.id,
            "user": self.user_reward.username,
            "title": self.reward_book,
            "author": self.reward_author,
            "date": self.reward_date,
            "address": self.user_reward.address,
            "tracking": self.ship_track,
        }