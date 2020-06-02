from django.db import models
from django.conf import settings

# Create your models here.
class Vote(models.Model):
    title = models.CharField(max_length=100)
    issue_a = models.CharField(max_length=150)
    issue_b = models.CharField(max_length=150)
    a_cnt = models.IntegerField(default=0)
    b_cnt = models.IntegerField(default=0)

class Comment(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    LE = 'LEFT'
    RI = 'RIGHT'
    VOTES = (
        (LE, 'LEFT'),
        (RI, 'RIGHT'),
    )
    votes = models.CharField(
        max_length=5,
        choices=VOTES,
        default=LE,
    )
    content = models.CharField(max_length=200)