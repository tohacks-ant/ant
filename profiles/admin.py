from django.contrib import admin

# Register your models here.
from .models import StuProfile, OrgProfile, Profile_relationship

admin.site.register(StuProfile)
admin.site.register(OrgProfile)
admin.site.register(Profile_relationship)
