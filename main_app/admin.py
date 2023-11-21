from django.contrib import admin
from .models import Gift, Recipient, Occasion

# Register your models here.
admin.site.register(Gift)
admin.site.register(Recipient)
admin.site.register(Occasion)