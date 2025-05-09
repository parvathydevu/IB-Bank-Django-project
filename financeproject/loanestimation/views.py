from django.shortcuts import render
from django.http import JsonResponse
import pickle
import numpy as np
from .forms import LoanEstimationForm

# Load the trained model
with open('scripts/trained_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def loan_estimation(request):
    if request.method == 'POST':
        form = LoanEstimationForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            monthly_income = form.cleaned_data['monthly_income']
            credit_score = form.cleaned_data['credit_score']
            loan_tenure = form.cleaned_data['loan_tenure']
            existing_loan_amount = form.cleaned_data['existing_loan_amount']
            number_of_dependents = form.cleaned_data['number_of_dependents']

            # Prepare the input data for prediction
            input_data = np.array([[age, monthly_income, credit_score, loan_tenure, existing_loan_amount, number_of_dependents]])
            
            # Predict the loan amount
            predicted_loan_amount = model.predict(input_data)[0]

            return JsonResponse({'predicted_loan_amount': predicted_loan_amount})

    else:
        form = LoanEstimationForm()

    return render(request, 'loanestimation/loan_estimation.html', {'form': form})
