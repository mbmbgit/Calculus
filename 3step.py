def generate_advanced_tier_proposal():
    print("="*60)
    print(" 🚀 最新B2Bロジック：バリューベース『松竹梅』見積り生成AI")
    print("="*60)

    try:
        client_budget = int(input("クライアントの提示上限予算 (例: 200000): "))
        # クライアントがこのデータを使って浮くコスト、または稼ぐ利益（月額）
        client_monthly_value = int(input("このシステムがクライアントにもたらす『月額の経済効果(利益/コスト削減)』 (例: 500000): "))
    except ValueError:
        print("エラー: 数値で入力してください。")
        return

    # --- 最新のプライシングロジック（行動経済学 ＋ 価値ベース） ---
    
    # 【梅 (Tier 3)】相手の予算内に収める「売り切り」モデル
    # 目的: とにかく案件を逃さないための保険
    tier3_price = client_budget * 0.9  # 予算の90%
    tier3_desc = "指定データの1回限りの抽出、または手動実行スクリプトのみの納品。保守なし。"

    # 【竹 (Tier 2)】本命。相手の予算を無視し、ROI（価値）ベースで価格設定する
    # 目的: 月額の継続課金（MRR）に持ち込み、10年で4億のストックを作る
    tier2_initial = client_budget * 1.5  # 予算の1.5倍（強気）
    tier2_mrr = client_monthly_value * 0.1  # 相手の得る月額利益の10%を保守費用として頂く
    tier2_desc = "【おすすめ】完全自動化システムの構築＋クラウド定期実行。仕様変更への無償対応・死活監視込み。"

    # 【松 (Tier 1)】アンカー。極端に高く設定し、竹を安く見せる
    # 目的: まれに予算が潤沢な大企業がこれを買うと一撃で儲かる
    tier1_initial = client_monthly_value * 3  # 経済効果の3ヶ月分
    tier1_mrr = client_monthly_value * 0.2    # 月額利益の20%
    tier1_desc = "取得データの分析ダッシュボード(BIツール)構築、競合価格アラート機能、専任コンサルティング。"

    print("\n" + "="*60)
    print(" 📋 【提案書にそのまま使える！ 3段階(松竹梅)の見積り案】")
    print("="*60)
    print("提案のコツ: 「ご予算に合わせて、3つのプランをご用意しました」と提示してください。\n")

    print(f"🌟 【松プラン: フルマネージド＆データ活用コンサル】")
    print(f"   初期費用 : {int(tier1_initial):,} 円")
    print(f"   月額保守 : {int(tier1_mrr):,} 円 / 月")
    print(f"   内容     : {tier1_desc}")
    print(f"   (※この価格でも、御社の見込み利益 {client_monthly_value:,}円/月 を考えれば数ヶ月でペイします)\n")

    print(f"👍 【竹プラン: 完全自動化＆運用サポート】(★あなたが売りたい本命)")
    print(f"   初期費用 : {int(tier2_initial):,} 円 (※予算オーバーですが提案します)")
    print(f"   月額保守 : {int(tier2_mrr):,} 円 / 月")
    print(f"   内容     : {tier2_desc}\n")

    print(f"🌱 【梅プラン: スクリプト納品のみ】(予算厳守プラン)")
    print(f"   初期費用 : {int(tier3_price):,} 円")
    print(f"   月額保守 : なし (売り切り)")
    print(f"   内容     : {tier3_desc}\n")

    print("-"*60)
    print("💡 経営的インサイト:")
    print("1つの価格（点の勝負）をやめ、3つの価格（面の勝負）にすることで、")
    print("相手は「依頼するかどうか」ではなく「どのプランにするか」に思考が切り替わります。")
    print(f"竹プランの月額保守({int(tier2_mrr):,}円)を獲得し続けることが、4億への最短ルートです。")

if __name__ == "__main__":
    generate_advanced_tier_proposal()
