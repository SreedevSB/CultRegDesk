"""regdesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from login.views import default, lo

urlpatterns = [
	url(r'^$', default, name='default'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include(('login.urls','login'), namespace="login")),
    url(r'^add_event/', include(('add_event.urls','add_event'), namespace="add_event")),
    url(r'^logout/', lo, name='logout'),
    url(r'^register/', include(('register.urls','register'), namespace="register")),
    url(r'^home/', include(('home.urls','home'), namespace="home")),
]
