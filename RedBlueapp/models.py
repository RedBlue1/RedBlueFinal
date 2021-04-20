from django.db import models
# Create your models here.
class nifty_50(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    d_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ema26 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ema13 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ema05 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    d_vol = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    macd_height = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ema_height = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ema_score = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    macd_score = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vol_score = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rsi = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'nifty_50'