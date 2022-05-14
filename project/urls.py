"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app.views import ViewContactGroup, ViewContact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ViewContact.home, name='home'),

    path('contact-group/list/', ViewContactGroup.list, name='list'),
    path('contact-group/form/', ViewContactGroup.form, name='form'),
    path('contact-group/create/', ViewContactGroup.create, name='create'),
    path('contact-group/view/<int:pk>', ViewContactGroup.view, name='view'),
    path('contact-group/edit/<int:pk>/', ViewContactGroup.edit, name='edit'),
    path('contact-group/update/<int:pk>/', ViewContactGroup.update, name='update'),
    path('contact-group/delete/<int:pk>/', ViewContactGroup.delete, name='delete'),

    path('contact/list/', ViewContact.list, name='list'),
    path('contact/form/', ViewContact.form, name='form'),
    path('contact/create/', ViewContact.create, name='create'),
    path('contact/view/<int:pk>', ViewContact.view, name='view'),
    path('contact/edit/<int:pk>/', ViewContact.edit, name='edit'),
    path('contact/update/<int:pk>/', ViewContact.update, name='update'),
    path('contact/delete/<int:pk>/', ViewContact.delete, name='delete'),
]
