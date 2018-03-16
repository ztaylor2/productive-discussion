"""productivediscussion URL Configuration."""
from django.contrib import admin
from django.urls import path
from productivediscussion.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', HomeView.as_view(), name='home'),

]
