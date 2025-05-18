from dj_rest_auth.registration.serializers import RegisterSerializer
<<<<<<< HEAD
from django.contrib.auth import get_user_model
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
=======
from dj_rest_auth.serializers import LoginSerializer, PasswordResetSerializer, PasswordResetConfirmSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .forms import CustomResetPasswordForm
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext as _

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data.update({
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        })
        return data
    
>>>>>>> 3ce4b0e (FIxes)
    def validate_email(self, email):
        UserModel = get_user_model()
        if UserModel.objects.filter(email=email).exists():
            raise serializers.ValidationError("A user is already registered with this email address.")
        return email
    
<<<<<<< HEAD
=======

class CustomLoginSerializer(LoginSerializer):
    username = None  # Remove username field
    email = serializers.EmailField(required=True)

class CustomPasswordResetSerializer(PasswordResetSerializer):
    password_reset_form_class = CustomResetPasswordForm
    
    def get_email_options(self):
        return {
            'subject_template_name': 'account/email/password_reset_subject.txt',
            'email_template_name': 'account/email/password_reset_message.txt',
            'html_email_template_name': 'account/email/password_reset_message.html',
            'extra_email_context': {
                'request': self.context.get('request'),
            },
        }
 
from allauth.account.forms import default_token_generator

class CustomPasswordResetConfirmSerializer(PasswordResetConfirmSerializer):
    def validate(self, attrs):
        # Decode UID (base64) and get user
        try:
            uid = force_str(urlsafe_base64_decode(attrs['uid']))
            self.user = User.objects.get(pk=uid)
        except (TypeError, ValueError, User.DoesNotExist):
            raise ValidationError({'uid': ['Invalid user ID']})

        # Validate token (Django's generator)
        if not default_token_generator.check_token(self.user, attrs['token']):
            raise ValidationError({'token': ['Invalid or expired token']})

        # Validate password
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )
        if not self.set_password_form.is_valid():
            raise ValidationError(self.set_password_form.errors)
        
        return attrs

    def save(self):
        if not self.user:
            raise AttributeError("User not set. Did validation fail?")
        self.user.set_password(self.validated_data['new_password1'])
        self.user.save()  # Only called if everything is valid
>>>>>>> 3ce4b0e (FIxes)
