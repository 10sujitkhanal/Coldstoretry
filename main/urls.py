from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path('add',views.farmersave,name='farmersave'),
    path('farmers/<int:id>',views.farmers,name='farmers'),
    path('seat/<int:id>',views.seat,name='seat'),
    path('booked',views.booked,name='booked'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)