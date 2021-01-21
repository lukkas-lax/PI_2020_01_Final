"""pi URL Configuration

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
from django.contrib import admin
from django.urls import path
from equipamento import views  

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('emp', views.emp),
    path('empf', views.empf), 
    path('empAloc', views.empAloc), 
    path('show',views.show),
    path('showf',views.showf),
    path('showAloc',views.showAloc),
    path('showMan',views.showMan),
    path('edit/<int:id>', views.edit), 
    path('det/<int:id>', views.det),
    path('editf/<int:id>', views.editf),
    path('update/<int:id>', views.update),  
    path('updatef/<int:id>', views.updatef), 
    path('delete/<int:id>', views.destroy),
    path('deletef/<int:id>', views.destroyf),
    path('email/<int:id>', views.email),
    path('emailMan/<int:id>', views.emailMan),
    path('conc/<int:id>', views.conc),
    
]
