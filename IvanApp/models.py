from django.db import models

class MyInput(models.Model):
    stockticker = models.CharField(max_length=10)
    lasttradeday = models.CharField(max_length=10)
    lastprice = models.CharField(max_length=10)
    dailypnl = models.CharField(max_length=10)
    mtdpnl = models.CharField(max_length=10)
    ytdpnl = models.CharField(max_length=10)

class MyOutput(models.Model):
    stockticker = models.CharField(max_length=10)
    lasttradeday = models.CharField(max_length=10)
    lastprice = models.CharField(max_length=10)
    dailypnl = models.CharField(max_length=10)
    mtdpnl = models.CharField(max_length=10)
    ytdpnl = models.CharField(max_length=10)

    def __str__(self):
        return self.text