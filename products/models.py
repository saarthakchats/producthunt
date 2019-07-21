from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    url = models.TextField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    pubdate = models.DateTimeField()
    voters = models.ManyToManyField(User,through="PostVoter")
    # voters = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def preview(self):
        return self.body[:100]
    def pretty_date(self):
        return self.pubdate.strftime('%b %e, %Y')

class PostVoter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("product", "user")
