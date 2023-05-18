from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('update/', views.putDataIntoDb, name='update'),
    path('api/', views.PkdViewSet.as_view()),

]