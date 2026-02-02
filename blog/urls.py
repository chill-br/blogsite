from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('edit/<int:id>/', views.edit_post, name='edit_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),

    path('register/', views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),

    path('logout/', views.logout_view, name='logout'),
]
