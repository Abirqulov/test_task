from django.urls import path
from .views import home, about, news, contact, register, login, logout_user


urlpatterns = [
    path('', home, name='index'),
    path('about', about, name='about'),
    path('news', news, name='news'),
    path('contact', contact, name='contact'),
    path('register', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('login', login, name='login'),

    # path('data', Data.as_view)
]