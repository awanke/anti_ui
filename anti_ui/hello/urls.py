from django.conf.urls import include, url
# from django.contrib import admin
from views import current_dt

urlpatterns = [
    url(r'^time/$', current_dt),
]
