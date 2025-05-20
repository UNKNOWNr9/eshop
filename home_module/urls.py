from django.urls import path
from home_module.views import home_page

urlpatterns = [
    path('', home_page),
]