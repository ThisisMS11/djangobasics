from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('capfirst',views.capfirst, name='capfirst'),
    path('analyze',views.analyze, name='analyze')
] 
