import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# 1. 数式の定義
x = sp.Symbol('x')
f = x**2

# --- 微分 ---
df = sp.diff(f, x)  # f(x)を微分
print(f"微分: f'(x) = {df}")

# --- 積分 (面積) ---
# 0から2までの範囲の面積を求める（定積分）
area = sp.integrate(f, (x, 0, 2))
print(f"x=0から2までの面積: {area} (約 {float(area):.2f})")

# --- グラフの描画 ---
x_vals = np.linspace(-1, 3, 100)
y_vals = x_vals**2

plt.plot(x_vals, y_vals, label="f(x) = x^2", color='blue')
# 面積（積分の範囲）を塗りつぶす
plt.fill_between(x_vals, y_vals, where=(x_vals>=0)&(x_vals<=2), color='orange', alpha=0.3, label="Area (0 to 2)")
# 微分=0の点（山や谷）をプロット
plt.scatter([0], [0], color='red', label="Minimum (f'(x)=0)")

plt.legend()
plt.grid(True)
plt.show()
