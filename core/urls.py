from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('signup/', views.UserRegisterView.as_view(), name='user_regster'),
    path('verify/', views.UserRegisterCodeView.as_view(),name='user_regster'),
]
