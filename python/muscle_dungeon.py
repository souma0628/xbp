#定義
import random
import time
def ask_yes_no(prompt):
    """はい or いいえ で答える関数"""
    while True:
        ans = input(prompt + " (はい/いいえ)")
        if ans in ["はい", "yes", "y"]:
            return True
        elif ans in ["いいえ", "no", "n"]:
            return False
        else:
            print("「はい」か「いいえ」で答えてください。")
def main():
    print("=== 💪 筋肉ダンジョンへようこそ！ ===")
    name=input("あなたの名前を入力してください")
    print(f"\nようこそ、{name}！筋肉伝説が始まる...\n")
    time.sleep(1)

 # レベル選択
    print("レベルを選んでください：")
    print("1. 初級（ライトメニュー）")
    print("2. 中級（ガチメニュー）")
    print("3. 上級（地獄メニュー）")

    level = input("レベル番号を半角数字で入力：")

    if level == "1":
        menu = ["腕立て伏せ ×10回", "スクワット ×15回", "腹筋 ×10回"]
    elif level == "2":
        menu = ["腕立て伏せ ×20回", "スクワット ×30回", "腹筋 ×20回", "プランク ×30秒"]
    elif level == "3":
        menu = ["腕立て伏せ ×50回", "スクワット ×50回", "腹筋 ×40回", "プランク ×60秒", "バーピー ×20回"]
    else:
        print("無効なレベルです。初級に設定します。")
        menu = ["腕立て伏せ ×10回", "スクワット ×15回", "腹筋 ×10回"]

    print("\n=== 今日の筋トレメニュー ===")
    for m in menu:
        print("👉", m)
        time.sleep(0.8)
# トレーニング開始
    print("\nトレーニング開始！🔥")
    time.sleep(20)

 # YES/NO 
 # トレーニング終了の確認
    if ask_yes_no("\nトレーニングは終わりましたか？疲れたらYes、続けるならNoを選んでください。 (yes/no):"):
        print("\nお疲れさまでした。💪")
        comments = [
            "筋肉が歓喜している！",
            "あなたの上腕二頭筋が輝いている！",
            "筋肉痛は成長の証だ！",
            "プロテインがあなたを待っている！",
            "筋肉がすべてを解決する！"
        ]
        print("\n💬", random.choice(comments))
        print("\n=== GAME CLEAR ===")
# トレーニング続行
    else:
        print("\nまだ鍛え足りないようですね…💀")
        print("もう1セットいってみましょう！🔥")
        time.sleep(2)
        for m in menu:
            print("💪", m)
        time.sleep(1)        
        print("\n限界突破！あなたは真の筋肉勇者だ！🏆")
        print("お疲れ様です!")
        print("\n=== GAME CLEAR ===")


# ゲーム終了
if __name__ == "__main__":
    main()
