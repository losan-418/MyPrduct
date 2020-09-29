"""MyPrduct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from MyPrduct import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name="index"),
    path('admin_home/',views.admin_home,name="admin_home"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_products/',views.admin_products,name="admin_products"),
    path('save_product/',views.save_product,name="save_product"),
    path('admin_login_check/',views.admin_login_check,name="admin_login_check"),
    path('user_register/',views.user_register,name="user_register"),
    path('save_user/',views.save_user,name="save_user"),
    path('user_data/',views.user_data,name="user_data"),
    path('update/',views.update,name="update"),
    path('delete/',views.delete,name="delete"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_login_check/',views.user_login_check,name="user_login_check"),
    path( 'user_detail/',views.user_detail,name="user_detail"),
    path('user_home/',views.user_home,name="user_home"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)