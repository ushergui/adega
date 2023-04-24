from django.urls import path
from .views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, LoginUserView, PaginaInicial
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('', PaginaInicial.as_view(), name='index'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]
