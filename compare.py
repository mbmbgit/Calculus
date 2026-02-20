"""
Python：現状維持 vs 目標達成の比較
"""



import sympy as sp

# --- 現状データ ---
current_unit_price = 61_405
current_orders_per_year = 14
current_yearly_revenue = current_unit_price * current_orders_per_year

# --- 10年目標 ---
target_total = 400_000_000
commission = 0.10
monthly_expense = 150_000
yearly_expense = monthly_expense * 12

# 1. 現状維持の10年積分 (単純な合計)
current_total_profit = (current_yearly_revenue * (1 - commission) - yearly_expense) * 10

# 2. 目標達成に必要な「成長」を逆算 (2次関数モデル f(x) = a*x^2 + current_revenue)
x = sp.Symbol('x')
a = sp.Symbol('a')
yearly_rev_func = a * x**2 + current_yearly_revenue
total_profit_func = sp.integrate((yearly_rev_func * (1 - commission)) - yearly_expense, (x, 0, 10))
required_a = sp.solve(total_profit_func - target_total, a)[0]

print(f"--- 現状分析 ---")
print(f"現在の年商: {current_yearly_revenue/10000:.1f} 万円")
print(f"現状維持での10年後の純利益: {current_total_profit/10000:.1f} 万円 (目標まで約3.9億円不足)")

print(f"\n--- 4億円達成へのロードマップ ---")
for year in [1, 5, 10]:
    rev = float(required_a) * year**2 + current_yearly_revenue
    print(f"{year:>2}年目: 月商目標 {rev/12/10000:>6.1f} 万円")
