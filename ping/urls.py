from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('ping/', views.ping_servers, name='ping_servers'),
    # path('server-groups/', views.get_server_groups, name='server_groups'),
    path('<slug:game_name>/', views.game_page, name='game_page'),
]
