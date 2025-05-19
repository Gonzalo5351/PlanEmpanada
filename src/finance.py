# src/finances.py

def calculate_daily_profit(empanadas_sold, sale_price, unit_cost):
    revenue = empanadas_sold * sale_price
    cost = empanadas_sold * unit_cost
    return revenue - cost

def calculate_weekly_profit(daily_profit, working_days=7):
    return daily_profit * working_days

def calculate_payback_days(initial_investment, daily_profit):
    if daily_profit <= 0:
        return float('inf')
    return round(initial_investment / daily_profit, 2)

def calculate_monthly_profit(weekly_profit):
    return weekly_profit * 4

def calculate_loan_installment(amount, monthly_rate, months):
    if monthly_rate == 0:
        return amount / months
    return amount * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)

def calculate_monthly_ending_balance(monthly_profit, monthly_installment):
    return monthly_profit - monthly_installment
