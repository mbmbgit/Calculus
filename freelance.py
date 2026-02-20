import sympy as sp

# 変数の定義 (x: 経過年数)
x = sp.Symbol('x')

# 目標：10年で4億円 (400,000,000)
target = 400_000_000

# 条件
commission_rate = 0.10  # 手数料10%
monthly_expense = 150_000
yearly_expense = monthly_expense * 12

# 成長モデルの定義 (例: 売上が年々加速すると仮定 f(x) = a * x^2)
# この a (成長係数) を積分を使って逆算します
a = sp.Symbol('a')
yearly_revenue = a * (x**2) # 年間の売上推移モデル
yearly_profit = (yearly_revenue * (1 - commission_rate)) - yearly_expense

# 10年間の利益の合計（積分）
total_profit = sp.integrate(yearly_profit, (x, 0, 10))

# 合計が4億円になる「成長係数 a」を解く
required_a = sp.solve(total_profit - target, a)[0]

print(f"10年で4億稼ぐための成長係数 a: {required_a:.2f}")

# 1年目、5年目、10年目に必要な「月間売上」を算出
def calc_monthly_revenue(year):
    return (float(required_a) * (year**2)) / 12

print(f"--- 必要な月間売上の目安 ---")
print(f"1年目: 約 {calc_monthly_revenue(1)/10000:.1f} 万円 / 月")
print(f"5年目: 約 {calc_monthly_revenue(5)/10000:.1f} 万円 / 月")
print(f"10年目: 約 {calc_monthly_revenue(10)/10000:.1f} 万円 / 月")
