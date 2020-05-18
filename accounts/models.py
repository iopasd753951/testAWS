from django.db import models
from django.urls import reverse


class Accounts(models.Model):
    pk_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, unique=True)
    nick_name = models.CharField(max_length=16, unique=True)
    id = models.CharField(max_length=16)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 해당 레코드 생성시 현재 시간 자동저장
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = "accounts"

    def __Str__(self):
        return self.nick_name