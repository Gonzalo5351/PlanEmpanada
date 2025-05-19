# PlanEmpanada

## Financial Simulator for Street Vendor Microbusinesses

PlanEmpanada is a simple Python-based tool designed to assess the economic viability of small street vending businesses. It calculates weekly profits, payback periods, and simulates loans with monthly installments. Ideal for beach vendors, market stall operators, and micro-entrepreneurs who need to make quick, data-driven decisions.

---

## Features

- Profit and loss simulation based on customizable sales scenarios.
- Calculation of break-even points (days to amortize initial investment).
- Loan simulation with flexible installments and durations.
- Simple and editable CSV input for testing different sales strategies.
- Clean and extensible Python codebase.

---

## File Structure

.
├── data/
│ └── scenarios.csv # Input data: business scenarios (editable)
├── src/
│ ├── finance.py # Monthly loan amortization logic
│ ├── simulator.py # Main simulation logic per scenario
│ ├── run_simulations.py # Entry point for executing all simulations
├── tests/ # (Optional) Add your test scripts here

---

## How to Use

1. **Install Python**  
   Make sure you have Python 3 installed in your environment.

2. **Customize your scenarios**  
   Edit the CSV file at `data/scenarios.csv`. Each row represents a business scenario with the following columns:

scenario_name,daily_units_sold,unit_sale_price,unit_cost_price

Example:

baseline,30,10,6
high sales volume,50,10,6
loan scenario 6x1000,30,10,6

3. **Run the simulations**

```bash
python3 src/run_simulations.py

This will print the simulation results to the console for each scenario, including:

    Daily income

    Daily cost

    Daily profit

    Days to break even (assuming a fixed initial investment)

    Loan amortization tables (if scenario name starts with loan)

Example Output

--- Scenario: loan scenario 6x1000 ---
Daily income: R$300.00
Daily cost: R$180.00
Daily profit: R$120.00
Days to break even: 50.0

Loan of R$6000.00 over 6 months:
Monthly payment: R$1083.00
Total repayment: R$6498.00

Notes

    You can define as many scenarios as you like in the scenarios.csv file.

    Loan scenarios must have names starting with loan (e.g., loan scenario 6x1000) to trigger loan calculations.

    The initial investment amount is inferred from the loan amount (e.g., 6x1000 = R$6000).

License

MIT License
