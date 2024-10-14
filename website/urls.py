"""los URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from store import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView


urlpatterns = [  
    path('', views.index, name='index'), 
    path('verify_signature/', views.verify_signature, name='verify_signature'),    
    path('game_create/', views.game_create, name='game_create'),  
    path('game_next/', views.game_next, name='game_next'),  
    path('all_games/', views.all_games, name='all_games'), 
    path('game/<str:game_id>/', views.view_game, name='view_game'), 
    path('api/add-handle/', views.add_social_media_handle, name='api_add_handle'),
    path('toggle_handle/<int:handle_id>/', views.toggle_handle_status, name='toggle_handle_status'),
    path('add-token-marketing/', views.TokenMarketingContentCreateView.as_view(), name='add_token_marketing'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('forward-to-x/', views.forward_to_x, name='forward_to_x'),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
