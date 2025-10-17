from django.urls import path
from rest_framework.authtoken import views
from .Api.login import UserRegistrationView, UserLoginView, UserLogoutView, UserAPIView
from .Api.expense_route import ExpenseGetView, ExpenseCreateView, ExpenseUpdateDeleteView, ExpenseTotalView, ExpenseTotalEssentialView, ExpenseTotalDiscretionaryView
from .Api.income_route import IncomeGetView, IncomeCreateView, IncomeUpdateDeleteView, IncomeTotalView
from .Api.debt_route import DebtGetView, DebtCreateView, DebtUpdateView, DebtDeleteView, DebtTotalView, DebtPaymentView
from .Components.get_profile import MyProfileView


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token, name = 'api_token_auth'),   #API for server to send client an auth token after sucessful login.
    path('register/', UserRegistrationView.as_view(), name = 'registrationView'),
    path('login/', UserLoginView.as_view(), name = 'loginView'),
    path('logout/', UserLogoutView.as_view(), name = 'logoutView'),
    path('getUser/', UserAPIView.as_view(), name = 'getUserView'),
    path('profile/', MyProfileView.as_view(), name = 'profileView'),
    path('expense/get', ExpenseGetView.as_view(), name = 'expenseGetView'),
    path('expense/create', ExpenseCreateView.as_view(), name='expenseCreateView'),
    path('expense/<int:pk>', ExpenseUpdateDeleteView.as_view(), name = 'expenseUpdateDeleteView'),
    path('expense/get/total', ExpenseTotalView.as_view(), name = 'expenseTotalView'),
    path('expense/get/totaldiscretionary', ExpenseTotalDiscretionaryView.as_view(), name = 'expenseTotalDiscretionaryView'),
    path('expense/get/totalessential', ExpenseTotalEssentialView.as_view(), name="expenseTotalEssentialView"),
    path('income/get', IncomeGetView.as_view(), name = 'incomeGetView'),
    path('income/create', IncomeCreateView.as_view(), name='incomeCreateView'),
    path('income/<int:pk>', IncomeUpdateDeleteView.as_view(), name = 'incomeUpdateDeleteView'),
    path('income/get/total', IncomeTotalView.as_view(), name = 'incomeTotalView'),
    path('debt/get', DebtGetView.as_view(), name = 'debtGetView'),
    path('debt/create', DebtCreateView.as_view(), name='debtCreateView'),
    path('debt/update/<int:pk>', DebtUpdateView.as_view(), name = 'debtUpdateView'),
    path('debt/delete/<int:pk>', DebtDeleteView.as_view(), name = 'debtDeleteView'),
    path('debt/get/total', DebtTotalView.as_view(), name = 'debtTotalView'),
    path('debt/get/payment', DebtPaymentView.as_view(), name='debtPaymentView'),
]