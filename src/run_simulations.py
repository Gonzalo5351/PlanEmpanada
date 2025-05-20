import csv

def run_csv_simulations(file_path, initial_investment=6000):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for idx, row in enumerate(reader, 1):
            name = row["scenario_name"]
            units = int(row["daily_units_sold"])
            price = float(row["unit_sale_price"])
            cost = float(row["unit_cost_price"])
            loan_months = int(row["loan_months"])
            loan_payment = float(row["loan_monthly_payment"])
            

            daily_income = units * price
            daily_cost = units * cost
            daily_profit = daily_income - daily_cost

            # Si hay préstamo, sumar el pago diario proporcional
            loan_total = loan_months * loan_payment if loan_months > 0 else 0
            total_investment = initial_investment + loan_total
            days_to_break_even = int(total_investment // daily_profit) if daily_profit > 0 else float("inf")

            print(f"\n--- Escenario {idx}: {name} ---")
            print(f"Empanadas por día: {units}")
            print(f"Precio por unidad: R${price}")
            print(f"Costo por unidad: R${cost}")
            print(f"Ingreso diario: R${daily_income}")
            print(f"Costo diario: R${daily_cost}")
            print(f"Ganancia diaria: R${daily_profit}")
            if loan_months > 0:
                print(f"Préstamo: {loan_months} cuotas de R${loan_payment} (Total: R${loan_total})")
            print(f"Días para recuperar la inversión: {days_to_break_even}")

if __name__ == "__main__":
    run_csv_simulations("data/scenarios.csv")
