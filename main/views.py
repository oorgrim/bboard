from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import get_template
from django.urls import reverse_lazy
<<<<<<< Updated upstream
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView
=======
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.base import TemplateView
>>>>>>> Stashed changes

from main.forms import ProfileEditForm, RegisterForm
from main.models import AdvUser


def index(request):
    return render(request, 'main/index.html')


def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


class BBLoginView(LoginView):
    template_name = 'main/login.html'


@login_required
def profile(request):
    return render(request, 'main/profile.html')


class BBLogoutView(LogoutView):
    pass


class ProfileEditView(SuccessMessageMixin, LoginRequiredMixin,
                      UpdateView):
    model = AdvUser
    template_name = 'main/profile_edit.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('main:profile')
    success_message = 'Данные пользователя изменены'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class PasswordEditView(SuccessMessageMixin, LoginRequiredMixin,
                       PasswordChangeView):
    template_name = 'main/password_edit.html'
    success_url = reverse_lazy('main:profile')
    success_message = 'Пароль пользователя изменён'

<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
class RegisterView(CreateView):
    model = AdvUser
    template_name = 'main/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('main:register_done')

<<<<<<< Updated upstream

class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'
=======
class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'
    
>>>>>>> Stashed changes
