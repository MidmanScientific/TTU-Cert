from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('registration', views.registration, name='registration'),
    path('Admin_login', views.Admin_login, name='Admin_login'),
    path('myAdmin', views.myAdmin, name='myAdmin'),
    path('check_request_status', views.check_request_status, name='check_request_status'),
    path('confirm_request/', views.confirm_request, name='confirm_request'),
    # Remove the 'check_request_status' URL pattern
    path('prompt-page', views.prompt_page, name='prompt_page'),
    path('prompt-page/?request_id=1', views.prompt_page, name='prompt_page'),
    path('login', views.login, name='login'),
    path('view_request_details',views.view_request_details, name='view_request_details'),
    path('verification', views.verification, name='verification'),
    path('result',views.result,name='result')
    
]