from allauth.core.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.urls import reverse
from urllib.parse import urljoin
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
>>>>>>> 82b70b0 (Fixes)
>>>>>>> 3ce4b0e (FIxes)

User = get_user_model()

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        email = sociallogin.account.extra_data.get("email")
        if not email:
            return  # Continue the normal flow if no email

        try:
            existing_user = User.objects.get(email=email)

            if sociallogin.is_existing:
                return  # Allow normal login

            # Link the social account to the existing user
            sociallogin.connect(request, existing_user)

            # Generate JWT tokens
            refresh = RefreshToken.for_user(existing_user)
            access_token = str(refresh.access_token)

            # Return tokens instead of redirecting
            raise ImmediateHttpResponse(
                Response(
                    {
                        "refresh": str(refresh),
                        "access": access_token,
                        "user": {
                            "id": existing_user.id,
                            "email": existing_user.email,
                        },
                    },
                    status=200,
                )
            )

        except User.DoesNotExist:
<<<<<<< HEAD
            pass  # Continue the normal signup process
=======
<<<<<<< HEAD
            pass  # Continue the normal signup process
=======
            pass  # Continue the normal signup process

from allauth.account.forms import default_token_generator  # Allauth's generator

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_reset_password_from_key_url(self, key):
        try:
            user_id = key.split("-")[0]
            user = User.objects.get(pk=user_id)
            
            # Generate Django's token + base64 UID
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            if settings.FRONTEND_RESET_URL:
                return f"{settings.FRONTEND_RESET_URL}/{uid}/{token}/"
        except Exception as e:
            print(f"Error generating reset URL: {e}")
        return super().get_reset_password_from_key_url(key)
>>>>>>> 82b70b0 (Fixes)
>>>>>>> 3ce4b0e (FIxes)
