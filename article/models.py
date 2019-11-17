from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class ArticlePost(models.Model):
    # 文章作者。参数 on_delete 用于指定数据删除的方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 文章标题
    title = models.CharField(max_length=100)

    # 文章正文
    body = models.TextField()

    # 文章创建时间
    created = models.DateTimeField(default=timezone.now)

    # 文章更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
    