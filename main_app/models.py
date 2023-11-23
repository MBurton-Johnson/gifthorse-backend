from django.db import models

class Gift(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  currency = models.CharField(max_length=3, default='GBP')
  description = models.TextField(max_length=250)
  occasion = models.ForeignKey('Occasion', on_delete=models.CASCADE)
  datebought = models.DateField()
  status = models.CharField(max_length=10, choices=[('Bought', 'Bought'), ('Given', 'Given'), ('Wish List', 'Wish List')], default='Pending')
  recipient = models.ForeignKey('Recipient', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Occasion(models.Model):
  name = models.CharField(max_length=100)
  date = models.DateField()

class Recipient(models.Model):
  name = models.CharField(max_length=100)
  relation = models.CharField(max_length=100)