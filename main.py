import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def show_basic_calculus():
    """1. 微分積分の基本とグラフ化（山の頂点と面積）"""
    print("\n=== 1. 微分積分の基本可視化 ===")
    x = sp.Symbol('x')
    f = x**2

    df = sp.diff(f, x)
    area = sp.integrate(f, (x, 0, 2))
    
    print(f"関数: f(x) = {f}")
    print(f"微分: f'(x) = {df} (傾き)")
    print(f"x=0から2までの積分(面積): {area:.2f}")

    x_vals = np.linspace(-1, 3, 100)
    y_vals = x_vals**2

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label="f(x) = x^2", color='blue')
    plt.fill_between(x_vals, y_vals, where=(x_vals>=0)&(x_vals<=2), color='orange', alpha=0.3, label="Integral Area (0 to 2)")
    plt.scatter([0], [0], color='red', label="Minimum (Derivative=0)")
    
    plt.title("Basic Calculus: Differentiation and Integration")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

def calc_optimal_price(cost=10):
    """2. 利益最大化の最適価格シミュレーション"""
    print(f"\n=== 2. 最適価格の算出 (原価 {cost}円の場合) ===")
    p = sp.Symbol('p')
    q = 100 - 2*p  # 需要関数
    revenue = p * q
    total_cost = cost * q
    profit = revenue - total_cost

    d_profit = sp.diff(profit, p)
    best_price = sp.solve(d_profit, p)[0]
    max_profit = profit.subs(p, best_price)

    print(f"利益関数: {sp.simplify(profit)}")
    print(f"利益の微分 (限界利益): {d_profit}")
    print(f"-> 利益が最大になる最適価格: {best_price} 円")
    print(f"-> その時の予想利益: {max_profit} 円")

def analyze_freelance_goals():
    """3. フリーランスの10年目標（4億円）ギャップ分析"""
    print("\n=== 3. 目標達成（10年で4億）へのロードマップ ===")
    current_price = 61405
    current_orders_per_year = 14
    current_yearly_revenue = current_price * current_orders_per_year
    target_total = 400_000_000
    
    commission = 0.10
    yearly_expense = 150_000 * 12

    x, a = sp.symbols('x a')
    
    # 現状維持の10年積分
    current_total_profit = (current_yearly_revenue * (1 - commission) - yearly_expense) * 10
    
    # 目標達成に必要な成長曲線 (f(x) = a*x^2 + 現在の売上)
    yearly_rev_func = a * x**2 + current_yearly_revenue
    total_profit_func = sp.integrate((yearly_rev_func * (1 - commission)) - yearly_expense, (x, 0, 10))
    required_a = sp.solve(total_profit_func - target_total, a)[0]

    print(f"[現状] 現在の年商: {current_yearly_revenue/10000:.1f} 万円")
    print(f"[現状] 現状維持での10年総利益: {current_total_profit/10000:.1f} 万円")
    print("\n[目標] 4億円達成に必要な『月商目標』の推移（加速モデル）:")
    for year in [1, 3, 5, 10]:
        rev = float(required_a) * year**2 + current_yearly_revenue
        print(f" {year:>2}年目: 月商 {rev/12/10000:>6.1f} 万円")

def compare_business_models():
    """4. 働き方の積分比較（単発 vs ストック型）"""
    print("\n=== 4. 働き方の積分比較 (10年=120ヶ月) ===")
    x = sp.Symbol('x')
    months = 120

    # パターンA：単発 (月約6.6万円)
    monthly_rev_A = 66000
    total_A = sp.integrate(monthly_rev_A, (x, 0, months))

    # パターンB：毎月5000円分ずつ継続契約が増えていくモデル
    monthly_rev_B = 66000 + 5000 * x
    total_B = sp.integrate(monthly_rev_B, (x, 0, months))

    print(f"パターンA (単発案件のみ) : 10年総売上 約 {total_A/10000:.0f} 万円")
    print(f"パターンB (継続案件蓄積) : 10年総売上 約 {total_B/10000:.0f} 万円")
    print("-> 継続契約（積分の底上げ）を取り入れると、資産の積み上がり方が劇的に変わります。")

def main():
    """メインメニュー"""
    while True:
        print("\n" + "="*40)
        print(" ビジネス微積シミュレーター メニュー")
        print("="*40)
        print("1: 微分積分の基本とグラフ表示")
        print("2: 最適価格の算出 (利益最大化)")
        print("3: 目標達成(4億円)へのロードマップ分析")
        print("4: 単発 vs ストック型ビジネスの総収益比較")
        print("0: 終了")
        print("-" * 40)
        
        choice = input("実行したい番号を入力してください: ")
        
        if choice == '1':
            show_basic_calculus()
        elif choice == '2':
            cost_input = input("想定する原価(コスト)を数字で入力してください (デフォルト10): ")
            cost = float(cost_input) if cost_input.strip() else 10
            calc_optimal_price(cost)
        elif choice == '3':
            analyze_freelance_goals()
        elif choice == '4':
            compare_business_models()
        elif choice == '0':
            print("シミュレーターを終了します。目標達成に向けて頑張ってください！")
            break
        else:
            print("無効な入力です。0〜4の数字を入力してください。")

if __name__ == "__main__":
    main()
