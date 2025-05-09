# FinanceProject

## Setup Instructions

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/financeproject.git
    ```

2. **Navigate to the project directory**:
    ```sh
    cd financeproject
    ```

3. **Create a virtual environment**:
    ```sh
    python -m venv env
    ```

4. **Activate the virtual environment**:
    - On Windows:
        ```sh
        env\Scripts\activate
        ```
    
    

5. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

6. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

7. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

8. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

9. **Access the application**:
    Open your browser and navigate to `http://127.0.0.1:8000/`.

## Feature Summary

- **User Registration and Login**: Users can register and log in to access their accounts.
- **Dashboard**: Displays current balance, transaction history, and financial tools.
- **Deposit and Withdraw**: Users can deposit and withdraw money from their accounts.
- **Financial Tools**: Includes EMI Calculator, SIP Calculator, FD Calculator, RD Calculator, Retirement Savings Estimator, Home Loan Eligibility Estimator, Credit Card Interest Calculator, Taxable Income Calculator, Budget Planner, and Net Worth Calculator.
- **Transaction History**: Users can view their transaction history.
- **Logout**: Users can log out of their accounts.

## Testing

- **Unit Tests**: Includes tests for registration, login, deposit, withdraw, and financial tools.
- **Code Coverage**: Ensure minimum 80% code coverage using `coverage.py`.

## License

This project is licensed under the MIT License.
