import sympy as sp

# --- 設定値 ---
target_total = 400_000_000  # 10年で4億
years = 10
commission = 0.10          # 手数料10%
monthly_expense = 150_000   # 月支出
unit_price = 500_000        # 仮の案件単価（50万円/件）

# --- 1. 成長曲線の算出 (積分を使用) ---
x = sp.Symbol('x')
a = sp.Symbol('a')
# 年間利益 = (年間売上 * 0.9) - 年間支出
# 年間売上を a * x^2 (加速モデル) と仮定
yearly_revenue_formula = a * x**2
yearly_profit_formula = (yearly_revenue_formula * (1 - commission)) - (monthly_expense * 12)

# 10年間の総利益を積分で計算
total_profit_integral = sp.integrate(yearly_profit_formula, (x, 0, years))

# 総利益 = 4億円 となる a を解く
required_a = sp.solve(total_profit_integral - target_total, a)[0]

# --- 2. 各年ごとの数値を表示 ---
print(f"{'経過年':<5} | {'月次売上(目標)':<12} | {'月次受注量':<10} (単価{unit_price/10000:.0f}万円の場合)")
print("-" * 55)

for year in range(1, years + 1):
    # 年間売上 = a * x^2
    yearly_rev = float(required_a) * (year**2)
    monthly_rev = yearly_rev / 12
    monthly_orders = monthly_rev / unit_price
    
    print(f"{year:>3}年目 | {monthly_rev/10000:>8.1f} 万円 | {monthly_orders:>8.2f} 件")
