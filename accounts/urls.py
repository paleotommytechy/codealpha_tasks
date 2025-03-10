from django.urls import path, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .views import login_view,logout_view,register_view
from django.contrib.auth import views as auth_view


app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='password_reset_form.html', success_url=reverse_lazy('accounts:password_reset_done'), email_template_name='password_reset_email.html'), name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )