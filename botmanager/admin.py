from django.contrib import admin
from .models import AdModel, BotModel, BotManager, SubmittedJobApplications
# Register your models here.

admin.site.register(AdModel)
admin.site.register(BotModel)
admin.site.register(BotManager)
admin.site.register(SubmittedJobApplications)
