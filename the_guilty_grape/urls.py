"""the_guilty_grape URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from allauth.account import views as accountviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', accountviews.signup, name="account_signup"),
    path('accounts/login/', accountviews.login, name="account_login"),
    path('accounts/logout/', accountviews.logout, name="account_logout"),
    path('accounts/password/change/', accountviews.password_change, name="account_change_password"),
    path('accounts/password/set/', accountviews.password_set, name="account_set_password"),
    path('accounts/confirm-email/', accountviews.email_verification_sent, name="account_email_verification_sent"),
    re_path('accounts/r"^confirm-email/(?P<key>[-:\w]+)/$', accountviews.confirm_email, name="account_confirm_email"),
    path('accounts/password/reset/', accountviews.password_reset, name="account_reset_password"),
    path('accounts/password/reset/done/', accountviews.password_reset_done, name="account_reset_password_done"),
    re_path('accounts/r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$', accountviews.password_reset_from_key, name="account_reset_password_from_key"),
    path('accounts/password/reset/key/done/', accountviews.password_reset_from_key_done, name="account_reset_password_from_key_done"),
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
