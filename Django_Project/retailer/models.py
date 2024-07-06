from django.db import models

class Retailer(models.Model):
    cid = models.CharField(max_length=100)
    cname = models.CharField(max_length=100)
    rtime = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=20)
    companyemail = models.CharField(max_length=40)
    companymobile = models.CharField(max_length=20)

    class Meta:
        db_table = 'Retailer'
