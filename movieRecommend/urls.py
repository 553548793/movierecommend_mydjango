from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    # path('login/', views.data),
    path('get_csrf_token', views.get_csrf_token,name='get_csrf_token'),
    path('test/', views.test),
    path('search/', views.search)
]
