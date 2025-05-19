# tests/test_integration.py

from simulator import simulate_scenario
import subprocess
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

def test_simulation_without_loan():
    result = simulate_scenario(
        empanadas_per_day=40,
        sale_price=10,
        unit_cost=6,
        initial_investment=6000
    )
    assert result['daily_profit'] == 160
    assert result['weekly_profit'] == 1120
    assert result['monthly_profit'] == 4480
    assert result['payback_days'] == 37.5

def test_simulation_with_loan():
    result = simulate_scenario(
        empanadas_per_day=40,
        sale_price=10,
        unit_cost=6,
        initial_investment=6000,
        loan_installments=6
    )
    assert 'monthly_installment' in result
    assert 'monthly_balance' in result

def test_run_simulations_script_runs_successfully():
    script_path = os.path.join("src", "run_simulations.py")
    result = subprocess.run(["python", script_path], capture_output=True, text=True)
    assert result.returncode == 0, f"Script failed: {result.stderr}"
    assert "--- Scenario 1:" in result.stdout  # Check some output expected from script
