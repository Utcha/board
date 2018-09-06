from django.urls import path
from post_service.views import post_list

urlpatterns = [
    path('', post_list),
]
