import numpy as np
import matplotlib.pyplot as plt

# 1. シミュレーションの設定
n_points = 10000  # まく砂の数（点）
x = np.random.uniform(-1, 1, n_points)  # -1から1までの間にランダムにxを配置
y = np.random.uniform(-1, 1, n_points)  # -1から1までの間にランダムにyを配置

# 2. 「いびつな池」の判定条件
# ここでは例として「原点からの距離が1以内（円）」を池とします
# 複雑な数式も、これだけで判定可能です
inside_pond = x**2 + y**2 <= 1

# 3. 面積の計算
# (池に入った点 / 全部の点) * 枠の面積(2x2 = 4)
estimated_area = (np.sum(inside_pond) / n_points) * 4

print(f"1万粒の砂をまいた結果の推定面積: {estimated_area}")
print(f"理論上の円の面積(π): {np.pi}")

# 4. 可視化
plt.figure(figsize=(6, 6))
plt.scatter(x[inside_pond], y[inside_pond], color='blue', s=1, label='Inside Pond')
plt.scatter(x[~inside_pond], y[~inside_pond], color='gray', s=1, alpha=0.3, label='Outside')
plt.title(f"Monte Carlo Method: Estimated Area = {estimated_area:.3f}")
plt.legend()
plt.show()
