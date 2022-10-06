import imp
from django.urls import path,re_path
from TS  import views

from django.conf.urls.static import static
from django.conf import settings

app_name = 'data'

urlpatterns = [
    path('', views.main, name='main'),
    path('user_info/', views.user_info, name='user_info'),
    path(r"activity", views.activityApi),
    re_path(r"activity/([0-9]+)$",views.activityApi),
    path(r"heart", views.heartApi),
    re_path(r"heart/([0-9]+)$",views.heartApi),
    path(r"sleep", views.sleepApi),
    re_path(r"sleep/([0-9]+)$",views.sleepApi),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)