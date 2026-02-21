import numpy as np

# 池の縁を計測したデータ（x座標と、その地点での池の縦幅 y）
# 例: 0m地点から10m地点まで、2mおきに池の縦幅を測ったとする
x_data = np.array([0, 2, 4, 6, 8, 10]) 
y_data = np.array([0, 3, 5, 4, 2, 0]) # 池の縦幅（深いところや浅いところがある）

# numpyの台形公式を使って面積を計算
pond_area = np.trapz(y_data, x_data)

print(f"池の推定面積: {pond_area} 平方メートル")
