from api.auth_user.routers import router
from django.urls import path, include
from api.auth_user.views import user
from api.auth_user.views.authorization import LogOutTokenView, LoginTokenView

user_urlpatterns = [
    path('createWithList/', user.UserCreateBulk.as_view(), name='createWithList'),
    path('user/login/', LoginTokenView.as_view(), name='login'),
    path('user/logout/', LogOutTokenView.as_view(), name='logout'),
    path('', include(router.urls)),
]
