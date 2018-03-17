"""productivediscussion URL Configuration."""
from django.contrib import admin
from django.urls import path
from productivediscussion.views import HomeView
from django.conf.urls import include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('accounts/', include('registration.backends.hmac.urls')),
    path('debate/', include('debate.urls')),
]
