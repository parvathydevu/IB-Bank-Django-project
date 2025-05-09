from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile,Transaction
from finance_app.finance_tools import *

class RegistrationTestCase(TestCase):
    def test_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'Paru@123',
            'email': 'parvatht2412@gmail.com',
            'password1': 'P24122000blue2707',
            'password2': 'P24122000blue2707'
        })
        if response.status_code != 302:
            print(response.context['form'].errors)  # Print form errors if not redirecting
        self.assertEqual(response.status_code, 302)  # Check for redirect after successful registration
        self.assertTrue(User.objects.filter(username='Paru@123').exists())
        self.assertTrue(Profile.objects.filter(user__username='Paru@123').exists())

class LoginTestCase(TestCase):
    def test_login(self):
        User.objects.create_user(username='Paru@123', password='P24122000blue2707')
        response = self.client.post(reverse('login'), {
            'username': 'Paru@123',
            'password': 'P24122000blue2707'
        })
        self.assertEqual(response.status_code, 302)  # Check for redirect after successful login
        self.assertTrue(response.wsgi_request.user.is_authenticated)

class DepositWithdrawTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.profile = Profile.objects.create(user=self.user, balance=1000)
def test_deposit(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('deposit'), {'amount': 500})
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.balance, 1500)
        self.assertEqual(response.status_code, 302)  # Check for redirect after successful deposit
def test_withdraw(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('withdraw'), {'amount': 500})
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.balance, 500)
        self.assertEqual(response.status_code, 302)  # Check for redirect after successful withdrawal
#Financial_tools test
 
class FinancialToolsTestCase(TestCase):
    def test_emi_calculator(self):
        response = self.client.post(reverse('emi_calculator'), {
            'principal': 100000,
            'rate': 7.5,
            'tenure': 12
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('emi', response.context)
        self.assertTrue(response.context['success'])
 
    def test_sip_calculator(self):
        response = self.client.post(reverse('sip_calculator'), {
            'monthly_investment': 5000,
            'annual_rate': 12,
            'years': 10
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('maturity', response.context)
        self.assertTrue(response.context['success'])
 
    def test_fd_calculator(self):
        response = self.client.post(reverse('fd_calculator'), {
            'principal': 100000,
            'annual_rate': 6.5,
            'years': 5
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('maturity', response.context)
        self.assertTrue(response.context['success'])
 
    def test_rd_calculator(self):
        response = self.client.post(reverse('rd_calculator'), {
            'monthly_deposit': 2000,
            'annual_rate': 7.0,
            'years': 3
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('maturity', response.context)
        self.assertTrue(response.context['success'])
 
    def test_retirement_savings_estimator(self):
        response = self.client.get(reverse('retirement_calculator'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on the functionality of the Retirement Savings Estimator
 
    def test_home_loan_eligibility_estimator(self):
        response = self.client.get(reverse('home_loan_eligibility'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on the functionality of the Home Loan Eligibility Estimator
 
    def test_credit_card_interest_calculator(self):
        response = self.client.get(reverse('credit_card_interest'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on the functionality of the Credit Card Interest Calculator
 
    def test_taxable_income_calculator(self):
        response = self.client.get(reverse('taxable_income'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on the functionality of the Taxable Income Calculator
 
    def test_budget_planner(self):
        response = self.client.get(reverse('budget_planner'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on the functionality of the Budget Planner
 
    def test_net_worth_calculator(self):
        response = self.client.get(reverse('net_worth_calculator'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on the functionality of the Net 