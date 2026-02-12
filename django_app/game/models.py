from django.db import models
from django.contrib.auth.models import User


class Story(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_page_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Page(models.Model):
    story_id = models.IntegerField()
    text = models.TextField()
    is_ending = models.BooleanField(default=False)
    ending_label = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"Page {self.id} (Story {self.story_id})"


class Choice(models.Model):
    page_id = models.IntegerField()
    text = models.CharField(max_length=200)
    next_page_id = models.IntegerField()

    def __str__(self):
        return self.text


class Play(models.Model):
    story_id = models.IntegerField()
    ending_page_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} → Story {self.story_id} → Ending {self.ending_page_id}"


class Rating(models.Model):
    story_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()

    def __str__(self):
        return f"{self.story_id} rated {self.stars}"


class Comment(models.Model):
    story_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Report(models.Model):
    story_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class AuthorStory(models.Model):
    story_id = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
