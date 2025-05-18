from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 3ce4b0e (FIxes)
from django.conf import settings

class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.CALLBACK_URL
<<<<<<< HEAD
    client_class = OAuth2Client
=======
    client_class = OAuth2Client
=======
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from rest_framework import status
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .tokens import persistent_token_generator
from .serializers import CustomPasswordResetSerializer, CustomPasswordResetConfirmSerializer
from dj_rest_auth.serializers import PasswordResetConfirmSerializer


from rest_framework.response import Response
from django.conf import settings

User = get_user_model()

class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.CALLBACK_URL
    client_class = OAuth2Client

class CustomPasswordResetView(PasswordResetView):
    def post(self, request, *args, **kwargs):
        # Custom logic before reset
        response = super().post(request, *args, **kwargs)
        # Custom logic after reset
        return response


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    serializer_class = CustomPasswordResetConfirmSerializer
>>>>>>> 82b70b0 (Fixes)
>>>>>>> 3ce4b0e (FIxes)
