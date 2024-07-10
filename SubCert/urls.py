from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name='registration'),
    path('Admin_login', views.Admin_login, name='Admin_login'),
    path('myAdmin', views.myAdmin, name='myAdmin'),
  
    path('confirm_request/', views.confirm_request, name='confirm_request'),
    # Remove the 'check_request_status' URL pattern
    path('prompt-page/', views.prompt_page, name='prompt_page'),
    path('login', views.login, name='login'),
    path('view_request_details',views.view_request_details, name='view_request_details')
]