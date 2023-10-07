from django.contrib import admin
from .models import User, Excerpt, TopBook, Reward

# Register your models here.
admin.site.register(User)
admin.site.register(Excerpt)
admin.site.register(TopBook)
admin.site.register(Reward)