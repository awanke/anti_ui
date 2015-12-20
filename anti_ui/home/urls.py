from django.conf.urls import include, url
from django.contrib import admin
from anti_ui.views.views_hello import hello, current_dt, hours_ahead

urlpatterns = [
    url(r'^hello/$', hello),
    url(r'^time/$', current_dt),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
]
