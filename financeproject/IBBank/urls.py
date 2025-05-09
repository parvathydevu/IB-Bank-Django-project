from django.urls import path
from . import views
 
urlpatterns = [
    #new path
    path('', views.register, name='home'),
    #path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('deposit/',views.deposit,name='deposit'),
    path('withdraw',views.withdraw, name='withdraw'),
    path('finance-tools',views.financial_tools,name='finance-tools'),
    path('loanestimator/',views.loan_estimator, name='loanestimator'), 
    path('emi/', views.emi_view, name='emi_calculator'),
    path('sip/', views.sip_calculator_view, name='sip_calculator'),
    path('fd/', views.fd_calculator_view, name='fd_calculator'),
    path('rd/', views.rd_calculator_view, name='rd_calculator'),
    path('retirement/', views.retirement_savings_view, name='retirement_calculator'),
    path('home-loan-eligibility/', views.home_loan_eligibility_view, name='home_loan_eligibility'),
    path('credit-card-interest/', views.credit_card_interest_view, name='credit_card_interest'),
    path('taxable-income/', views.taxable_income_view, name='taxable_income'),
    path('budget-planner/', views.budget_planner_view, name='budget_planner'),
    path('net-worth/', views.net_worth_view, name='net_worth_calculator'),
]