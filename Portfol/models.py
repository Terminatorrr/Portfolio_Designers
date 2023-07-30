from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Portfolio(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    image = models.ImageField(upload_to=('portfolio_images/'), blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return  "%s" % (self.name)

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'



# class PortfolioImage(models.Model):
#     portfolio = models.ForeignKey("Portfolio", blank=True, null=True, default=None, on_delete=models.CASCADE)
#
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#
#
#     def __str__(self):
#         return  "%s" % self.id
#
#     class Meta:
#         verbose_name = 'Photo'
#         verbose_name_plural = 'Photo'

