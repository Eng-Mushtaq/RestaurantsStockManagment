from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('', views.home_view, name='home'),
    path('bakeds/', views.bakeds_view, name='bakeds'),
    path('contact/', views.contact_view, name='contact'),
    path('drinks/', views.drinks_view, name='drinks'),
    path('fastFood/', views.fastFood_view, name='fastFood'),
    path('orders/', views.orders_view, name='orders'),
    path('sweets/', views.sweets_view, name='sweets'),
    # path('login/', views.login_view, name='login'),
    # path('', views.home_view, name='home'),
]
