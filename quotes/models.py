from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="本のタイトル")
    author = models.CharField(max_length=100, verbose_name="著者")
    isbn = models.CharField(max_length=20, blank=True, verbose_name="ISBN")
    url = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="本のリンク"
    )
    added_by = models.ForeignKey(
        User, blank=True, on_delete=models.CASCADE, verbose_name="登録者"
    )
    added_at = models.DateTimeField(default=timezone.now, verbose_name="登録日")
    category = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="カテゴリー"
    )

    class Meta:
        verbose_name = "本"
        verbose_name_plural = "本"

    def __str__(self):
        return f"{self.title} - {self.author}"


class Quote(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="book", verbose_name="本"
    )
    content = models.TextField(verbose_name="本文")
    page = models.IntegerField(null=True, blank=True, verbose_name="ページ")
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="ユーザー")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    # reactions = models.ManyToManyField(Reaction)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "引用"
        verbose_name_plural = "引用"

    def __str__(self):
        return f"{self.book.title} - {self.content[:20]}..."


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="タグ名")
    quotes = models.ManyToManyField(Quote, related_name="quotes", verbose_name="引用")

    class Meta:
        verbose_name = "タグ"
        verbose_name_plural = "タグ"

    def __str__(self):
        return self.name


class Connection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follow = models.ManyToManyField(User, related_name="follow", blank=True)

    class Meta:
        verbose_name = "フォロー"
        verbose_name_plural = "フォロー"

    def __str__(self):
        return self.user.username
