from django.urls import path
from user_manager.views import login, login_validate, join_page

urlpatterns = [
    path('login/', login),
    path('login/validate', login_validate),
    path('join/', join_page)
]
