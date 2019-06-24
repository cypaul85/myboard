from django.db import models
from datetime import datetime

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    writer = models.CharField(null=False,max_length=50)
    title = models.CharField(null=False, max_length=80)
    content = models.TextField(null=False)
    post_date=models.DateTimeField(default=datetime.now, blank=True)
    hit_count=models.IntegerField(default=0)

    def hit_up(self):
        self.hit_count += 1

