from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import Index

urlpatterns = [
    path('', views.index),
    path('data/', Index.as_view()),

]

