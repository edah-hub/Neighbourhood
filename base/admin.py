from django.contrib import admin
from .models import User, Post, NeighbourHood, Business
# Register your models here.

admin.site.register(User)
admin.site.register(NeighbourHood)
admin.site.register(Business)
admin.site.register(Post)