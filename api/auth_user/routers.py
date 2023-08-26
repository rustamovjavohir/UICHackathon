from api.auth_user.views import user
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('user', user.UserViewSet, basename='user')
