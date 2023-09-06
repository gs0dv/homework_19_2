from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.decorators.cache import never_cache

from users.apps import UsersConfig
from users.views import RegisterView, verification, recovery_password

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', never_cache(RegisterView.as_view()), name='register'),
    path('verify/<verification_key>', verification, name='verify'),
    path('recovery/', never_cache(recovery_password), name='recovery'),
]
