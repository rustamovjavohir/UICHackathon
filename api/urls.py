from django.urls import path, include
from api.auth_user.urls import user_urlpatterns as user_urls
from api.products.urls import urlpatterns as product_urls
urlpatterns = [
    path('', include(user_urls)),
    path('', include(product_urls)),
]
