from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Product(models.Model):

    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to="images/")
    icon = models.ImageField(upload_to="images/")
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    upvoted_by = ArrayField(base_field=models.IntegerField(), default=list)
    # title
    # url
    # pub_date
    # votes_total
    # image
    # icon
    # body

    def pub_date_pretty(self):
        return self.pub_date

    def summary(self):
        str_body = str(self.body)
        if len(str_body.split()) < 10:
            return str_body
        else:
            return " ".join(str_body.split()[:10]) + "..."

    def __str__(self):
        return self.title
