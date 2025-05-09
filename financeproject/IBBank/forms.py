from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DepositForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

class WithdrawForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

class LoanEstimatorForm(forms.Form):
    age = forms.IntegerField(label='Age', min_value=18, max_value=100)
    monthly_income = forms.DecimalField(label='Monthly Income', max_digits=10, decimal_places=2)
    credit_score = forms.IntegerField(label='Credit Score', min_value=300, max_value=850)
    loan_tenure = forms.IntegerField(label='Loan Tenure (in months)', min_value=1, max_value=360)
    existing_loan_amount = forms.DecimalField(label='Existing Loan Amount', max_digits=10, decimal_places=2)
    number_of_dependents = forms.IntegerField(label='Number of Dependents', min_value=0)