from django.urls import path
from .views import Home, DepositDetail, DepositCreate, DepositUpdate, DepositDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('deposit/<int:pk>/', DepositDetail.as_view(), name='deposit'),
    path('deposit-create/', DepositCreate.as_view(), name='deposit-create'),
    path('deposit-update/<int:pk>/', DepositUpdate.as_view(), name='deposit-update'),
    path('deposit-delete/<int:pk>/', DepositDelete.as_view(), name='deposit-delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]