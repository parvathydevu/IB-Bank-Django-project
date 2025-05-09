import unittest
from finance_tools import *

class TestFinanceTools(unittest.TestCase):
    def test_emi_calculator(self):
        self.assertAlmostEqual(calculate_emi(100000, 10, 1), 8791.59, places=2)

    def test_sip_calculator(self):
        self.assertAlmostEqual(calculate_sip(1000, 12, 2), 27243.2, places=2)

    def test_fd_calculator(self):
        self.assertAlmostEqual(calculate_fd(50000, 7, 5), 70738.91, places=2)

    def test_rd_calculator(self):
        self.assertAlmostEqual(calculate_rd(2000, 6, 3), 78660.0, places=2)

    def test_retirement_savings_estimator(self):
       self.assertAlmostEqual(estimate_retirement_corpus(100000, 5000, 10, 20), 4561291.91, places=2)

    def test_home_loan_eligibility_estimator(self):
        self.assertAlmostEqual(estimate_home_loan_eligibility(80000, 30000, 20, 7), 3869475.19, places=2)

    def test_credit_card_interest_calculator(self):
       self.assertAlmostEqual(calculate_credit_card_balance(10000, 24, 12, 5), 6938.42, places=2)

    def test_taxable_income_calculator(self):
        self.assertEqual(calculate_taxable_income(800000, 150000), 650000.0)

    def test_simple_budget_planner(self):
        result = plan_budget(50000, 30000)
        self.assertEqual(result, {"savings": 10000.0, "investments": 10000.0})

    def test_net_worth_calculator(self):
        self.assertEqual(calculate_net_worth(1000000, 400000), 600000.0)

if __name__ == '__main__':
    unittest.main()