from django.db import models

class SeatAllotment(models.Model):
    Institute_name = models.CharField(max_length=500,default = "null")
    year = models.IntegerField(default=2022)
    branch = models.CharField(max_length=100,default="null")
    category = models.CharField(max_length=100,default="Open")
    gender = models.CharField(max_length=100,default="Neutral")
    opening_rank = models.IntegerField(default=0)
    closing_rank = models.IntegerField(default=0)
    round_no = models.IntegerField(default=1)
    
    
    
    # Add more fields based on your CSV columns
