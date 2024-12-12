from django.urls import path

from .views import (index, other_page,
                    BBLoginView, profile, BBLogoutView, ProfileEditView,
                    PasswordEditView, RegisterDoneView, RegisterView)

app_name = 'main'

urlpatterns = [
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/password/edit/', PasswordEditView.as_view(), name='password_edit'),
    path('accounts/profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('<str:page>', other_page, name='other'),
    path('', index, name='index'),
]
