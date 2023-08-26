from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.mixins import HandleExceptionMixin
from utils.responses import Response
from drf_spectacular.utils import extend_schema
from api.auth_user.serializers.authorization import (TokenLoginSerializer, TokenLogOutSerializer)
from apps.auth_user import constants
from utils.swagger_tags import Web


class LoginTokenView(HandleExceptionMixin, GenericAPIView):
    serializer_class = TokenLoginSerializer

    @extend_schema(tags=[Web.User.PREFIX], summary='Log in user into the system')
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data, message=constants.USER_LOG_IN, status=status.HTTP_200_OK)


class LogOutTokenView(HandleExceptionMixin, GenericAPIView):
    serializer_class = TokenLogOutSerializer
    permission_classes = [IsAuthenticated, ]

    @extend_schema(tags=[Web.User.PREFIX], summary='Log out current logged in user session')
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(message=constants.USER_LOG_OUT, status=status.HTTP_205_RESET_CONTENT)

#
# class VerifyTokenView(HandleExceptionMixin, APIView):
#     permission_classes = [AllowAny, ]
#     user_services = UserServices()
#
#     @extend_schema(tags=[Web.User.PREFIX])
#     def get(self, request, *args, **kwargs):
#         token = request.GET.get('token')
#         # _token = Token.objects.filter(token=token, is_active=True).first()
#         _token = 'dasd'
#         if _token:
#             password = generate_password()
#             self.user_services.deactivate_token(_token)
#             self.user_services.set_user_password(_token.user, password)
#             return Response(data={'new_password': password}, message=constants.TOKEN_IS_VALID,
#                             status=status.HTTP_200_OK)
#         return Response(message=constants.TOKEN_IS_INVALID_OR_EXPIRED,
#                         success=False, status=status.HTTP_400_BAD_REQUEST)
