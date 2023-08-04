from django.urls import path
from .views import UserCreateView, UserLoginView, RideCreateView, RideDetailView, RideListView, RideUpdateStatusView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('rides/', RideCreateView.as_view(), name='ride-create'),
    path('rides/<int:pk>/', RideDetailView.as_view(), name='ride-detail'),
    path('rides/list/', RideListView.as_view(), name='ride-list'),
    path('rides/<int:pk>/update/', RideUpdateStatusView.as_view(), name='ride-update-status'),
]