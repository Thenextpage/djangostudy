#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TweetModel

# Register your models here.
admin.site.register(TweetModel)