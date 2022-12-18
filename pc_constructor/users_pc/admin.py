from django.contrib import admin

from users_pc.models import UsersPcModel, UserMonitorModel, UserVideoCardModel

# Register your models here.
admin.site.register(UsersPcModel)
admin.site.register(UserMonitorModel)
admin.site.register(UserVideoCardModel)