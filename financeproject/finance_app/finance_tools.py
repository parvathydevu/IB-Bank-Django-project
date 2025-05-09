import math

def validate_positive_float(value, name):
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError(f"{name} must be a positive number.")
    return float(value)

def validate_positive_int(value, name):
    if not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a positive integer.")
    return value

def calculate_emi(principal, annual_rate, tenure_years):
    """
    Calculate EMI (Equated Monthly Installment).

    Parameters:
    - principal (float): Loan principal amount.
    - annual_rate (float): Annual interest rate in percentage.
    - tenure_years (int): Loan tenure in years.

    Returns:
    - float: Monthly EMI
    """
    principal = validate_positive_float(principal, "Principal")
    annual_rate = validate_positive_float(annual_rate, "Interest rate")
    tenure_years = validate_positive_int(tenure_years, "Tenure")

    monthly_rate = annual_rate / (12 * 100)
    tenure_months = tenure_years * 12
    emi = (principal * monthly_rate * (1 + monthly_rate)**tenure_months) / ((1 + monthly_rate)**tenure_months - 1)
    return round(emi, 2)

def calculate_sip(monthly_investment, annual_rate, years):
    """
    Calculate maturity amount from SIP.

    Parameters:
    - monthly_investment (float): Monthly investment amount.
    - annual_rate (float): Annual return rate in percentage.
    - years (int): Investment period in years.

    Returns:
    - float: Maturity amount
    """
    monthly_investment = validate_positive_float(monthly_investment, "Monthly investment")
    annual_rate = validate_positive_float(annual_rate, "Interest rate")
    years = validate_positive_int(years, "Years")

    monthly_rate = annual_rate / (12 * 100)
    months = years * 12
    maturity = 0
    for i in range(months):
        maturity += monthly_investment * ((1 + monthly_rate)**(months - i))
    return round(maturity, 2)

def calculate_fd(principal, annual_rate, years):
    """
    Calculate maturity amount for fixed deposit.

    Parameters:
    - principal (float): Initial deposit.
    - annual_rate (float): Annual interest rate in percentage.
    - years (int): Duration in years.

    Returns:
    - float: Maturity amount
    """
    principal = validate_positive_float(principal, "Principal")
    annual_rate = validate_positive_float(annual_rate, "Interest rate")
    years = validate_positive_int(years, "Years")

    compounding_frequency = 4  # Quarterly
    maturity = principal * (1 + annual_rate / (100 * compounding_frequency))**(compounding_frequency * years)
    return round(maturity, 2)

def calculate_rd(monthly_deposit, annual_rate, years):
    """
    Calculate maturity amount for recurring deposit.

    Parameters:
    - monthly_deposit (float): Monthly deposit amount.
    - annual_rate (float): Annual interest rate in percentage.
    - years (int): Duration in years.

    Returns:
    - float: Maturity amount
    """
    monthly_deposit = validate_positive_float(monthly_deposit, "Monthly deposit")
    annual_rate = validate_positive_float(annual_rate, "Interest rate")
    years = validate_positive_int(years, "Years")

    n = years * 12
    r = annual_rate / (12 * 100)
    maturity = monthly_deposit * n + monthly_deposit * n * (n + 1) / 2 * r
    return round(maturity, 2)

def estimate_retirement_corpus(current_savings, monthly_contribution, annual_rate, years):
    """
    Estimate retirement corpus.

    Parameters:
    - current_savings (float): Current savings amount.
    - monthly_contribution (float): Monthly contribution.
    - annual_rate (float): Expected annual return rate.
    - years (int): Number of years to retirement.

    Returns:
    - float: Future corpus
    """
    current_savings = validate_positive_float(current_savings, "Current savings")
    monthly_contribution = validate_positive_float(monthly_contribution, "Monthly contribution")
    annual_rate = validate_positive_float(annual_rate, "Interest rate")
    years = validate_positive_int(years, "Years")

    r = annual_rate / (12 * 100)
    n = years * 12
    future_value = current_savings * (1 + r)**n + monthly_contribution * (((1 + r)**n - 1) * (1 + r)) / r
    return round(future_value, 2)

def estimate_home_loan_eligibility(monthly_income, monthly_expenses, loan_tenure_years, annual_rate):
    """
    Estimate maximum loan amount eligible.

    Parameters:
    - monthly_income (float): Monthly income.
    - monthly_expenses (float): Monthly expenses.
    - loan_tenure_years (int): Loan tenure in years.
    - annual_rate (float): Annual interest rate.

    Returns:
    - float: Maximum loan eligibility
    """
    monthly_income = validate_positive_float(monthly_income, "Monthly income")
    monthly_expenses = validate_positive_float(monthly_expenses, "Monthly expenses")
    loan_tenure_years = validate_positive_int(loan_tenure_years, "Tenure")
    annual_rate = validate_positive_float(annual_rate, "Interest rate")

    max_emi = (monthly_income - monthly_expenses) * 0.6
    r = annual_rate / (12 * 100)
    n = loan_tenure_years * 12
    if r == 0:
        loan = max_emi * n
    else:
        loan = max_emi * ((1 + r)**n - 1) / (r * (1 + r)**n)
    return round(loan, 2)

def calculate_credit_card_balance(balance, annual_rate, months, min_payment_percent):
    """
    Calculate balance when only minimum payments are made.

    Parameters:
    - balance (float): Outstanding balance.
    - annual_rate (float): Annual interest rate.
    - months (int): Number of months to calculate.
    - min_payment_percent (float): Minimum payment percent.

    Returns:
    - float: Final balance after months
    """
    balance = validate_positive_float(balance, "Balance")
    annual_rate = validate_positive_float(annual_rate, "Interest rate")
    months = validate_positive_int(months, "Months")
    min_payment_percent = validate_positive_float(min_payment_percent, "Minimum payment percent") / 100

    monthly_rate = annual_rate / (12 * 100)
    for _ in range(months):
        interest = balance * monthly_rate
        min_payment = balance * min_payment_percent
        balance = balance + interest - min_payment
    return round(balance, 2)

def calculate_taxable_income(gross_income, deductions):
    """
    Calculate taxable income after deductions.

    Parameters:
    - gross_income (float): Total gross income.
    - deductions (float): Total deductions.

    Returns:
    - float: Taxable income
    """
    gross_income = validate_positive_float(gross_income, "Gross income")
    deductions = validate_positive_float(deductions, "Deductions")

    taxable_income = max(0, gross_income - deductions)
    return round(taxable_income, 2)

def plan_budget(income, expenses):
    """
    Suggest savings and investments based on income and expenses.

    Parameters:
    - income (float): Monthly income.
    - expenses (float): Monthly expenses.

    Returns:
    - dict: Suggested savings and investment allocation
    """
    income = validate_positive_float(income, "Income")
    expenses = validate_positive_float(expenses, "Expenses")

    surplus = income - expenses
    plan = {
        "savings": round(surplus * 0.5, 2),
        "investments": round(surplus * 0.5, 2),
    }
    return plan

def calculate_net_worth(assets, liabilities):
    """
    Calculate net worth.

    Parameters:
    - assets (float): Total assets.
    - liabilities (float): Total liabilities.

    Returns:
    - float: Net worth
    """
    assets = validate_positive_float(assets, "Assets")
    liabilities = validate_positive_float(liabilities, "Liabilities")

    return round(assets - liabilities, 2)
