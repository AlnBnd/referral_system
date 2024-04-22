from django.urls import path
from .views import SendVerificationView, VerifyView, UserProfileView, InviteesListView

urlpatterns = [
    path('send-verification-code/', SendVerificationView.as_view(), name='send-verification-code'),
    path('verify-code/', VerifyView.as_view(), name='verify-code'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('invitees/', InviteesListView.as_view(), name='invitees-list'),
]