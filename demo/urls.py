"""demo URL Configuration

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
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.IndexView.as_view(), name='index'),
    path('user/<str:guid>/', include([
        path('', views.UserInfo.as_view(), name='user_info'),
        path('connections_ui/', views.UIConnectionsView.as_view(), name='connections_ui'),
        path('connect/<str:driver_id>/', views.ConnectView.as_view(), name='connect'),
        path('data_lake/<str:driver_id>/<int:account_id>/', views.DataLakeView.as_view(), name='data_lake'),
    ])),
]
