import sympy as sp

def run_calculus_freelance_calculator():
    print("="*55)
    print(" フリーランス収益シミュレーター (実績直接入力・微分積分版)")
    print("="*55)

    # 1. 現状のヒアリング（より直感的な入力へ変更）
    try:
        current_price = int(input("過去1年間の「平均受注単価」を入力してください (例: 61405): "))
        
        # 改善点: 年間の件数を直接入力
        yearly_orders = int(input("過去1年間の「総受注件数」を入力してください (例: 14): "))
        current_orders_per_month = yearly_orders / 12  # プログラム内で月平均に変換
        
        monthly_expense = int(input("毎月の「経費・生活費」を入力してください (例: 150000): "))
        commission_rate = float(input("手数料率を小数で入力してください (10%なら 0.1): "))
        target_amount = int(input("10年後の「目標手取り額(純利益)」を入力してください (例: 400000000): "))
    except ValueError:
        print("エラー: 数値で入力してください。")
        return

    # 現状の月間利益
    current_revenue = current_price * current_orders_per_month
    current_profit = (current_revenue * (1 - commission_rate)) - monthly_expense

    # --- 微分積分による成長曲線の計算 ---
    x = sp.Symbol('x') # 経過月数
    a = sp.Symbol('a') # 毎月の利益成長スピード（傾き）

    # 利益関数: 現在の利益 + a * x
    profit_func = current_profit + a * x

    # 積分: 10年間(120ヶ月)の総利益
    months = 120
    total_profit_expr = sp.integrate(profit_func, (x, 0, months))

    # 目標金額になるような a (成長スピード) を解く
    required_a = sp.solve(total_profit_expr - target_amount, a)[0]
    
    # 微分: 利益関数の変化率（毎月の成長必須額）
    final_profit_func = current_profit + required_a * x
    derivative_func = sp.diff(final_profit_func, x)

    # --- 結果の出力 ---
    print("\n" + "="*55)
    print(" 【解析結果：10年で4億円達成へのロードマップ】")
    print("="*55)
    
    print(f"[現状分析]")
    print(f"・現在の月間平均受注件数: 約 {current_orders_per_month:.2f} 件 (年間{yearly_orders}件換算)")
    print(f"・現在の平均月商: 約 {int(current_revenue):,} 円")
    
    if current_profit <= 0:
         print(f"・現在の月間純利益: 約 {int(current_profit):,} 円 ⚠️現在赤字ペースです")
    else:
         print(f"・現在の月間純利益: 約 {int(current_profit):,} 円")

    print(f"\n[微分の視点：毎月必要な成長ペース（変化率）]")
    print(f"・目標達成のためには、毎月の純利益を【 {int(derivative_func):,} 円 】ずつ増やし続ける必要があります。")
    
    revenue_increase_per_month = float(derivative_func) / (1 - commission_rate)
    print(f"・手数料({commission_rate*100:.0f}%)を考慮すると、売上ベースでは毎月【 {int(revenue_increase_per_month):,} 円 】の増加が必要です。")
    
    print(f"\n[積分の視点：マイルストーン（受注ペースを変えない場合の目標単価）]")
    print(f"※現在の月間約 {current_orders_per_month:.2f} 件のペースを維持して単価だけを上げる場合")
    
    for month in [1, 12, 36, 60, 120]:
        target_rev = current_revenue + (revenue_increase_per_month * month)
        target_unit_price = target_rev / current_orders_per_month
        
        # 表示の調整 (1ヶ月後, 1年後...)
        if month < 12:
            years_label = f"{month}ヶ月後"
        elif month % 12 == 0:
            years_label = f"{month//12}年後"
        else:
            years_label = f"{month//12}年{month%12}ヶ月後"
            
        print(f" ・{years_label:<8}: 目標単価 約 {int(target_unit_price):>9,} 円/件 (月商目標: 約 {int(target_rev):,} 円)")

if __name__ == "__main__":
    run_calculus_freelance_calculator()