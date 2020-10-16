from django.conf.urls import url, include
from rest_framework.authtoken import views as auth_views
from django.urls import path, include
from api.router import router
from api.viewsets import UserAPIView, RegisterAPIView, LoginAPIView 


urlpatterns = [
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('api/auth/user', UserAPIView.as_view()),
    path('api/auth/register', RegisterAPIView.as_view()),
    path('api/auth/login', LoginAPIView.as_view()),
    url(r'^api/', include(router.urls))
]
