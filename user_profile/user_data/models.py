from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ExcelModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    excelfile = models.FileField(upload_to='file/', null=True, verbose_name="")

    def __str__(self):
        return self.pk


class UserModel(models.Model):
    ex_file = models.ForeignKey(ExcelModel, on_delete=models.CASCADE)
    unique_id = models.IntegerField()
    username = models.IntegerField(null=True)
    social_platform = models.CharField(max_length=20,null=True)
    media = models.IntegerField(null=True)
    followers = models.IntegerField(null=True)
    following = models.IntegerField(null=True)
    engagement = models.IntegerField(null=True)
    authenticity = models.IntegerField(null=True)
    highlight_reel_count = models.IntegerField(null=True)
    is_business_account = models.IntegerField(null=True)
    is_private = models.IntegerField(null=True)
    is_verified = models.IntegerField(null=True)
    is_barter = models.IntegerField(null=True)
    business_category = models.CharField(max_length=30,null=True)
    join_date = models.DateTimeField(null=True)
    last_updated_on = models.DateTimeField(null=True)
    status = models.IntegerField(null=True)
    price_per_pic_post = models.IntegerField(null=True)
    cost_per_engagement = models.DecimalField(max_digits=15, decimal_places=4)

    def __str__(self):
        return self.username
