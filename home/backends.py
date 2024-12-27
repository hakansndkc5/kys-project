# myapp/backends.py
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # get_user_model() fonksiyonu ile özel kullanıcı modelini alıyoruz
            User = get_user_model()
            user = User.objects.get(email=username)  # E-posta adresi ile kullanıcıyı buluyoruz
            if user.check_password(password):  # Şifreyi kontrol ediyoruz
                return user
        except User.DoesNotExist:
            return None
