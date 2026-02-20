import sympy as sp

# 変数の定義 (p: 価格)
p = sp.Symbol('p')

# 1. 需要関数（価格pのときに売れる個数q）は変わらないと仮定
q = 100 - 2*p

# 2. 売上関数 (単価p × 個数q)
revenue = p * q

# 3. 新しいコスト関数 (1個20円に値上がり)
new_cost = 20 * q

# 4. 新しい利益関数
new_profit = revenue - new_cost

# 5. 利益を微分（変化率を求める）
d_new_profit = sp.diff(new_profit, p)

# 6. 微分 = 0 となる最適価格を解く
new_best_price = sp.solve(d_new_profit, p)

print(f"新コストでの利益の式: {sp.simplify(new_profit)}")
print(f"新コストでの利益の微分: {d_new_profit}")
print(f"--- 結論 ---")
print(f"原材料費が20円のときの最適価格は: {new_best_price[0]} 円")
