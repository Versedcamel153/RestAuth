# tokens.py
from django.contrib.auth.tokens import PasswordResetTokenGenerator
   
class PersistentTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + user.password + str(timestamp)


persistent_token_generator = PersistentTokenGenerator()