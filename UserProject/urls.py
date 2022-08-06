
from django.contrib import admin
from django.urls import path
from talent_labs.views import JobApplicationHandler
from allusers.views import UserHandler
from botmanager.views import BotManagerHandler, JobAdHandler

urlpatterns = [
    path('admin/', admin.site.urls),
    path('botmanager/<str:name>', BotManagerHandler),
    path('job/<str:botmanager>/<str:adId>', JobAdHandler),
    # path('bot/<str:botname >', BotHandler),
    path('user/<str:name>', UserHandler),
    path('store-job-application-form/', JobApplicationHandler),
]
