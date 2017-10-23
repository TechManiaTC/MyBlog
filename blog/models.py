import markdown
from django.utils.html import strip_tags
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# Category 是 Post 的外键，外键类必须写在上面，否则读不到...
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    excerpt = models.CharField(max_length=100, blank=True)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category, null=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    # 用于生成 Post 的 URL
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    # 自动生成摘要
    def save(self, *args, **kwargs):
            if not self.excerpt:
                md = markdown.Markdown(extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                ])
                self.excerpt = strip_tags(md.convert(self.body))[:80]
            super(Post, self).save(*args, **kwargs)

        # 统计阅读量
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        ordering = ['-created_time', 'title'] #　默认倒序排列
