from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts') # 저자
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)  # 저자 프로필
    title = models.CharField(max_length=128)    # 제목
    category = models.CharField(max_length=128) # 카테고리
    body = models.TextField()   # 본문
    image = models.ImageField(upload_to='post/', default='default.png') # 이미지
    likes = models.ManyToManyField(User, related_name='like_posts', blank=True)    # 좋아요
    published_date = models.DateTimeField(default=timezone.now) # 글이 올라간 시간

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()