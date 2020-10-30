from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('convert',views.convertToShort),
    path('viewsite',views.get_long_url),
    path('match',views.get_match_data),
]
