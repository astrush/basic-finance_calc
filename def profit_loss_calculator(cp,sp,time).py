print("welcome to ashfilings!, it is your personal accountant")
revenue=int(input("enter annual revenue"))
cogs=int(input("enter cost of goods sold"))
gross_profit=revenue-cogs
Deprecation=int(input("enter depreciation amount"))
amortization=int(input("enter ammortization amount"))


def gross_profit_margin_calc(gross_profit,revenue):
    return gross_profit/revenue
general_expenses=int(input("enter general expenses"))
repairs=int(input("enter repair expenses"))
rnd=int(input("enter research and development expenses"))
total_expenses=cogs+general_expenses+repairs+rnd
ebitda=revenue-total_expenses
abc=(total_expenses+Deprecation+amortization)

def ebitda_calculator(revenue,total_expenses):
    return revenue-total_expenses
def ebitda_margin_calculator(ebitda,revenue):
    return ebitda / revenue
ebit=(revenue)-(total_expenses+Deprecation+amortization)
def ebit_calculator(revenue,abc):
    return revenue-abc
def ebit_margin_calculator(revenue,abc):
    return ebit / abc

print("\n--- Financial Summary ---")
print(f"Gross Profit: {gross_profit}")
print(f"Gross Profit Margin: {gross_profit_margin_calc:.2%}")
print(f"EBITDA: {ebitda_calculator(ebitda, revenue)}")
print(f"EBITDA Margin: {ebitda_margin_calculator(ebitda, revenue):.2%}")
print(f"EBIT: {ebit_calculator(revenue, abc)}")
print(f"EBIT Margin: {ebit_margin_calculator(ebit_calculator(revenue, abc), revenue):.2%}")

