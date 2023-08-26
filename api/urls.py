from django.urls import path, include
from api.auth_user.urls import user_urlpatterns as user_urls

urlpatterns = [
    path('', include(user_urls)),
]
