# src/simulator.py

from finance import (
    calculate_daily_profit,
    calculate_weekly_profit,
    calculate_monthly_profit,
    calculate_payback_days,
    calculate_loan_installment,
    calculate_monthly_ending_balance
)

def simulate_scenario(empanadas_per_day, sale_price, unit_cost, initial_investment,
                     annual_interest_rate=0.3, loan_installments=None):
    daily_profit = calculate_daily_profit(empanadas_per_day, sale_price, unit_cost)
    weekly_profit = calculate_weekly_profit(daily_profit)
    monthly_profit = calculate_monthly_profit(weekly_profit)
    payback_days = calculate_payback_days(initial_investment, daily_profit)

    result = {
        'daily_profit': daily_profit,
        'weekly_profit': weekly_profit,
        'monthly_profit': monthly_profit,
        'payback_days': payback_days
    }

    if loan_installments:
        monthly_rate = annual_interest_rate / 12
        installment = calculate_loan_installment(initial_investment, monthly_rate, loan_installments)
        balance = calculate_monthly_ending_balance(monthly_profit, installment)
        result['monthly_installment'] = installment
        result['monthly_balance'] = balance

    return result
