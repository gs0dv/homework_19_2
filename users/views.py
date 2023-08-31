from random import randint

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_verification_key = ''.join([str(randint(0, 9)) for _ in range(15)])

        self.object = form.save()
        self.object.verification_key = new_verification_key
        self.object.is_active = False
        self.object.save()

        site = 'http://127.0.0.1:8000'
        url = reverse_lazy('users:verify', kwargs={'verification_key': new_verification_key})

        send_mail(
            subject='Верификация пользователя',
            message=f'Подтвердить адрес почты: {site}{url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object]
        )
        return super().form_valid(form)


def verification(request, verification_key):
    try:
        user_obj = User.objects.filter(verification_key=verification_key).first()
        if user_obj:
            user_obj.is_active = True
            user_obj.save()
            return render(request, 'users/confirm_success.html')
        else:
            return render(request, 'users/confirm_failed.html')

    except Exception as e:
        pass


def recovery_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            new_password = ''.join([str(randint(0, 9)) for _ in range(12)])
            send_mail(
                subject='Восстановление пароля',
                message=f'Ваш новый пароль: {new_password}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email]
            )

            user.set_password(new_password)
            user.save()
            return redirect(reverse('users:login'))
        except Exception:
            pass

    return render(request, 'users/recovery_password.html')
