"""
URL configuration for uiumetamesh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from metamesh import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , views.indexPage, name="login"),
    path("signup/", views.signupPage, name="signup"),
    path("post_signup/", views.post_sign, name="po_sign"),
    path("validate/", views.validate_user, name='validate'),
    path("dashboard/<str:user>", views.dashboard, name='dashb'),
    path("postit/<str:user>", views.postText, name='postit'),
    path("likeit/", views.likeit, name='likeit'),
]