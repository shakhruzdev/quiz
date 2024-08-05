from django.urls import path
from .views import RegisterViewSet, LoginViewSet

register_view = RegisterViewSet.as_view({'post': 'create'})
login_view = LoginViewSet.as_view({'post': 'create'})

urlpatterns = [
    path('register/', register_view),
    path('login/', login_view),
]
