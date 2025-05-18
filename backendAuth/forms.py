# forms.py
from allauth.account.forms import ResetPasswordForm
from django.conf import settings

class CustomResetPasswordForm(ResetPasswordForm):
    def save(self, request, **kwargs):
        # Set the custom base URL in the request temporarily
        request.custom_reset_base_url = getattr(settings, 'PASSWORD_RESET_BASE_URL', None)
        return super().save(request, **kwargs)