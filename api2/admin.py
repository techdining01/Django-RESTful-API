from django.contrib import admin
from .models import CustomUser



admin.site.site_header = 'API ADMIN'
admin.site.site_title = 'API Portal'
admin.site.index_title = 'Welcome to API Admin'
admin.site.register(CustomUser)
# admin.site.register(User)