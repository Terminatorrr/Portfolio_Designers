from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Ask(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
    customer_email = models.EmailField(max_length=64 ,blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    subject = models.CharField(max_length=100, blank=True, null=True, default=None)
    message = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return  "Message %s %s %s" % (self.id, self.customer_name, self.customer_email)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'




