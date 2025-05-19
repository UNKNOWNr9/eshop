from django.urls import path
from blog_module.views import Home


urlpatterns = [
    path('', Home.as_view(), name='home')
]