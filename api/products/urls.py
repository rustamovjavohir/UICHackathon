from django.urls import path, include
from api.products.routers import router

urlpatterns = [
    path('', include(router.urls)),
]
