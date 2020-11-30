from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from agent.serializers import CustomTokenObtainPairSerializer

TOKEN_OBTAIN_PAIR = 'token-obtain-pair'
TOKEN_REFRESH = 'token-refresh'

urlpatterns = [
    path('auth/knock-knock/', TokenObtainPairView.as_view(serializer_class=CustomTokenObtainPairSerializer),
         name=TOKEN_OBTAIN_PAIR),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name=TOKEN_REFRESH),
]
